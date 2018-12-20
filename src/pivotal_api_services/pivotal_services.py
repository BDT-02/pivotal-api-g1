from abc import ABCMeta
from src.core.api.request_manager import RequestManager


class PivotalServices:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.request_handler = RequestManager.get_instance()
