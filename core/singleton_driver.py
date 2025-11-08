class SingletonDriver:
    _instances = {}

    @classmethod
    def get_instance(cls, key, creator):
        if key not in cls._instances:
            cls._instances[key] = creator()
        return cls._instances[key]

    @classmethod
    def reset(cls):
        cls._instances.clear()
