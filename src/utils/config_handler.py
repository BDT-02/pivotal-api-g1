from src.utils.config_reader import ConfigReader


class ConfigHandler:
    config = None

    @staticmethod
    def get_config():
        if ConfigHandler.config is None:
            ConfigHandler.config = ConfigReader()
        return ConfigHandler.config
