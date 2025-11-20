import os
import yaml


class ConfigManager:
    def __init__(self):
        base_path = os.path.join(os.path.dirname(__file__), "..", "config")
        config_file = os.path.join(base_path, "config.yaml")

        with open(config_file, "r") as f:
            self.config = yaml.safe_load(f)

    def get_url(self, key):
        return self.config["urls"][key]

    def get_credential(self, key):
        return self.config["credentials"][key]

    def get_timeout(self, key):
        return self.config["timeouts"][key]

    def get(self, key):
        return self.config[key]  # generic getter
