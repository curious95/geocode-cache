import requests

from abc import ABC, abstractmethod

from src.configuration import Config


class GeocodeBase(ABC):

    def __init__(self):
        self.config = Config()

    @abstractmethod
    def get_code(self):
        pass

    def make_request(self, url, params, headers):
        
        response = requests.request("GET", url, headers=headers, params=querystring)
