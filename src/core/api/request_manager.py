from src.core.api.request_handler import RequestHandler
from src.utils.config_handler import ConfigHandler


class RequestManager:
    __instance = None

    @staticmethod
    def get_instance():
        if RequestManager.__instance is None:
            RequestManager.__instance = RequestHandler()
            RequestManager.__instance.session.headers.update(
                {"X-TrackerToken": ConfigHandler.get_config().get_token(),
                 "Content-Type": "application/json"})
        return RequestManager.__instance
