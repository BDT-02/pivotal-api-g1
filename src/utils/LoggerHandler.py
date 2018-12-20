from src.utils.Logger import Logger


class LoggerHandler:
    # Here will be the instance stored.
    __instance = None

    """
    :return instance.
    """
    @staticmethod
    def get_instance():
        """ Static access method. """
        if LoggerHandler.__instance is None:
            LoggerHandler.__instance = Logger()
        return LoggerHandler.__instance
