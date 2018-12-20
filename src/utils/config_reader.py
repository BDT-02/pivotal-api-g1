import yaml


class ConfigReader:

    def __init__(self, path='./config.yml'):
        self.__path = path
        self.config = yaml.load(open(self.__path))

    def get_config(self):
        return self.config

    def get_log_path(self):
        return self.config["api"]["log_path"]

    def get_base_api_url(self):
        return self.config["api"]["base_url"]

    def get_token(self):
        return self.config["api"]["token"]
