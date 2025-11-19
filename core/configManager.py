import yaml
import os

class ConfigManager:

    def __init__(self, env="dev"):
        base_path = "config"

        # Load base config
        with open(f"{base_path}/config.yaml", "r") as f:
            self.base = yaml.safe_load(f)

        # Override with environment file
        with open(f"{base_path}/env_{env}.yaml", "r") as f:
            self.env = yaml.safe_load(f)

    def get_url(self, key):
        return self.env["urls"][key]

    def get_credential(self, key):
        return self.env["credentials"][key]

    def get_base(self, key):
        return self.base.get(key)
