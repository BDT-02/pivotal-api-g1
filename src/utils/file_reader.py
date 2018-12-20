import os
from src.utils.env_utils import EnvironmentUtil

from src.utils.LoggerHandler import LoggerHandler

logger = LoggerHandler.get_instance()

class FileReader:

    @staticmethod
    def get_file_content(file_path):
        logger.info("Getting Content of file::{}".format(file_path))
        path = EnvironmentUtil.get_root_folder_path()
        file_schema = open(os.path.abspath(path + file_path))
        schema = file_schema.read()
        file_schema.close()
        return schema
