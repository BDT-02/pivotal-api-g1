import ast
import simplejson as json


class StringHandler:

    @staticmethod
    def convert_string_to_dict(string_to_dict):
        return ast.literal_eval(string_to_dict)

    @staticmethod
    def convert_string_to_json(string_to_json):
        return json.loads(string_to_json)
