import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry
import json
from src.utils.config_handler import ConfigHandler
from src.utils.LoggerHandler import LoggerHandler

logger = LoggerHandler.get_instance()


class RequestHandler:

    def __init__(self):
        self.session = requests.Session()
        self.main_url = ConfigHandler.get_config().get_base_api_url()

    def post_request(self, endpoint, body):
        logger.info("RequestHandler:: POST  {}, {}, {}".format(endpoint, json.dumps(body), self.session.headers))
        response = self.requests_retry_session(session=self.session).post(endpoint, json.dumps(body))
        logger.info("RequestHandler:: POST RESPONSE:: {}, {}".format(response.status_code, response.json()))
        return response

    def get_request(self, endpoint):
        logger.info("RequestHandler:: GET  {}".format(endpoint))
        response = self.requests_retry_session(session=self.session).get(endpoint)
        logger.info("RequestHandler:: GET RESPONSE:: {}, {}".format(response.status_code, response.json()))
        return response

    def delete_request(self, endpoint):
        logger.info("RequestHandler:: DELETE  {}".format(endpoint))
        response = self.requests_retry_session(session=self.session).delete(endpoint)
        return response

    @property
    def main_url(self):
        return self.main_url

    def requests_retry_session(
            retries=3,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 504),
            session=None):
        """used to process a request retry if their response is 500, 502, or 504 """
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
