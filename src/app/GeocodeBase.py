import requests
import re

from elasticsearch import Elasticsearch
from abc import ABC, abstractmethod

from src.configuration import Config
from src import log
from src.app.geocoders.es_controller import search_by_index_and_id, add_to_index


class GeocodeBase(ABC):

    def __init__(self):
        self.config = Config()
        self.es = Elasticsearch(['http://' + self.config.es_user + ':' + self.config.es_pass + '@' + self.config.es_host + ':' + self.config.es_port])
        self.logger = log.setup_custom_logger('BASE_CONTROLLER')

    @abstractmethod
    def get_code(self, address):
        pass

    def geocode_lookup(self, address):
        try:
            return search_by_index_and_id(es=self.es, _index=self.config.es_index, _id=self.conv_address_to_id(address))
        except Exception as e:
            return False

    def add_new_geocode(self, address, body):
        return add_to_index(es=self.es, _index=self.config.es_index, _id=self.conv_address_to_id(address), body=body)

    @staticmethod
    def conv_address_to_id(address):
        return  re.sub('[^0-9a-zA-Z]+', '_', address)