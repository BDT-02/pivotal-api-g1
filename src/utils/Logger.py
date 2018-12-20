import logging

from src.utils.config_handler import ConfigHandler


class Logger:
    """
    This class is to logs.
    """

    # filename read from properties.
    def __init__(self):
        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=ConfigHandler.get_config().get_log_path())
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

    @staticmethod
    def debug(msg):
        """Return a message type debug.
            @msg receive a text.
        """
        logging.debug(msg)

    @staticmethod
    def error(msg):
        """Return a message type error.
            @msg receive a text.
        """
        logging.error(msg)

    @staticmethod
    def info(msg):
        """Return a message type info.
            :msg receive a text.
        """
        logging.info(msg)

    @staticmethod
    def warning(msg):
        """Return a message type warning.
            :msg receive a text.
        """
        logging.warning(msg)

    @staticmethod
    def critical(msg):
        """Return a message type critical.
            :msg receive a text.
        """
        logging.critical(msg)
