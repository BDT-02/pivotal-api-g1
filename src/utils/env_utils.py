import os
import inspect
import json
import uuid


class EnvironmentUtil:

    @staticmethod
    def get_root_folder_path():
        return os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), "..", "..")

    @staticmethod
    def create_json_file(file_path, file_name, data):
        json_file_path = '%s%s/%s-%s.json' % (
            EnvironmentUtil.get_root_folder_path(), file_path, file_name, uuid.uuid4())
        with open(json_file_path, 'w+') as fp:
            json.dump(data, fp=fp, indent=4, sort_keys=True)
        return json_file_path