# core/configManager.py
import os
import yaml

class ConfigManager:
    _config = None

    @classmethod
    def load(cls, config_path=None):
        if cls._config is not None:
            return cls._config
        base = os.path.join(os.path.dirname(__file__), "..", "config")
        cfg = config_path or os.path.join(base, "config.yaml")
        with open(cfg, "r") as f:
            cls._config = yaml.safe_load(f)
        return cls._config

    @classmethod
    def get(cls, key, default=None):
        if cls._config is None:
            cls.load()
        return cls._config.get(key, default)

    @classmethod
    def get_url(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("urls", {}).get(key)

    @classmethod
    def get_credential(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("credentials", {}).get(key)

    @classmethod
    def get_timeout(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("timeouts", {}).get(key)

    @classmethod
    def get_retry_count(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("retries", {}).get(key, 1)
    
    @classmethod
    def get_shipping(cls, address_type):
        if cls._config is None:
            cls.load()
        return cls._config.get("shippingDetails", {}).get(address_type)
    
    @classmethod
    def get_billing(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("billingDetails", {}).get(key)
    
    @classmethod
    def get_claim_code(cls, key):
        if cls._config is None:
            cls.load()
        return cls._config.get("claimCode", {}).get(key)
    


