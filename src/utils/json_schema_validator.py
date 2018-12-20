from jsonschema import validate

from src.utils.LoggerHandler import LoggerHandler

logger = LoggerHandler.get_instance()

def validate_json_schema(schema, json):
    try:
        validate(json, schema)
        logger.info("Validate Schema")
        return None, True
    except Exception as e:
        logger.info("FAILED JSON SCHEMA validation: {}".format(e.message))
        return False, e.message
