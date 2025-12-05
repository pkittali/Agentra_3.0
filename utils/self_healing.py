# utils/self_healing.py
import os
import re
import json
from difflib import SequenceMatcher

from bs4 import BeautifulSoup


class SelfHealingEngine:
    """
    Driver-aware self-healing engine.

    WEB/APPIUM MODE:
        - Uses HTML DOM + BeautifulSoup
        - Supports id / xpath / name / placeholder / aria-label based healing

    DESKTOP MODE:
        - Healing disabled (no BeautifulSoup, no DOM)
        - Future extension possible based on UIA tree attributes
    """

    def __init__(self, driver, log_path="reports/healing_log.json"):
        """
        Auto-detect driver type and configure healing appropriately.
        """
        # unwrap WebDriverManager if necessary
        if hasattr(driver, "driver"):
            self.driver = driver.driver
        else:
            self.driver = driver

        # check driver capability
        self.is_web = hasattr(self.driver, "page_source")
        self.is_desktop = hasattr(self.driver, "element_info") or hasattr(self.driver, "child_window")

        self.log_path = log_path
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

    # -------------------------------------------------------------------
    # HELPER: similarity score
    # -------------------------------------------------------------------
    def similarity(self, a, b):
        try:
            return SequenceMatcher(None, a.lower(), b.lower()).ratio()
        except Exception:
            return 0

    # -------------------------------------------------------------------
    # PUBLIC API: Heal locator if possible
    # -------------------------------------------------------------------
    def self_heal_locator(self, locator):
        """
        Attempts healing based on driver type.

        locator is expected as tuple: (by, value) for web.
        Desktop uses dict → healing skipped automatically.
        """

        # ----------------------------------------------------------
        # DESKTOP MODE → NO HEALING
        # ----------------------------------------------------------
        if self.is_desktop:
            return None  # pywinauto cannot use DOM healing

        # ----------------------------------------------------------
        # WEB/APPIUM MODE (requires HTML)
        # ----------------------------------------------------------
        if not self.is_web:
            return None

        if locator is None or not isinstance(locator, tuple):
            return None

        by, original_value = locator

        try:
            html = self.driver.page_source
        except Exception:
            return None

        soup = BeautifulSoup(html, "html.parser")

        # --- ID healing ---
        if by.lower() == "id":
            healed = self._heal_by_attr("id", original_value, soup)
            if healed:
                self._log(locator, healed)
                return healed

        # --- XPATH healing ---
        if by.lower() == "xpath":
            # extract attributes from xpath
            for attr in ["id", "name", "placeholder", "aria-label"]:
                match = re.search(rf"@{attr}=['\"]([^'\"]+)['\"]", original_value)
                if match:
                    healed = self._heal_by_attr(attr, match.group(1), soup)
                    if healed:
                        self._log(locator, healed)
                        return healed

        # --- fallback: similarity healing across multiple attributes ---
        for attr in ["id", "name", "placeholder", "aria-label"]:
            healed = self._heal_by_attr(attr, original_value, soup)
            if healed:
                self._log(locator, healed)
                return healed

        return None

    # -------------------------------------------------------------------
    # INTERNAL: heal by matching attribute similarities
    # -------------------------------------------------------------------
    def _heal_by_attr(self, attr, target_value, soup):
        best = None
        best_score = 0.0

        for tag in soup.find_all(attrs={attr: True}):
            candidate = tag.get(attr)
            if not candidate:
                continue

            score = self.similarity(candidate, target_value)

            if score > best_score and score >= 0.70:
                best = candidate
                best_score = score

        if not best:
            return None

        # return healed locator
        if attr == "id":
            return ("id", best)

        return ("xpath", f"//*[@{attr}='{best}']")

    # -------------------------------------------------------------------
    # LOG HEALED LOCATOR
    # -------------------------------------------------------------------
    def _log(self, old, new):
        """
        Saves old → new mapping in a JSON log file.
        """
        try:
            data = {}
            if os.path.exists(self.log_path):
                with open(self.log_path, "r") as f:
                    try:
                        data = json.load(f)
                    except Exception:
                        data = {}

            data[str(old)] = {"old": old, "new": new}

            with open(self.log_path, "w") as f:
                json.dump(data, f, indent=4)

        except Exception:
            pass  # do not interfere with tests
