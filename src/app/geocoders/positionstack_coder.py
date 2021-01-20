import json
import http.client, urllib.parse

from src.app.GeocodeBase import GeocodeBase
from src import log


class PstackCoder(GeocodeBase):

    def __init__(self):
        super().__init__()
        self.conn = http.client.HTTPConnection('api.positionstack.com')
        self.logger = log.setup_custom_logger('PSTACK_API_CONTROLLER')
        self.params = None

    def get_code(self, address):

        geo_dict = dict()

        self.logger.info(f'Looking up address <{address}>')

        is_address_present = self.geocode_lookup(address=address)

        if is_address_present:
            self.logger.info(f'Cached geocodes found for address <{address}>')
            self.logger.info(is_address_present)
            geo_dict['latitude'] = is_address_present['_source']['latitude']
            geo_dict['longitude'] = is_address_present['_source']['longitude']
        else:
            self.logger.info(f'Address <{address}> not present in cache :: Fetching it Freshly')
            try:
                self.params = urllib.parse.urlencode({
                    'access_key': self.config.pstack_key,
                    'query': address,
                    'limit': 1,
                    'output': 'json'
                })

                self.conn.request('GET', '/v1/forward?{}'.format(self.params))

                res = self.conn.getresponse()
                geocodes = res.read()

                geocodes = json.loads(geocodes.decode('utf-8'))

                if geocodes is not None:
                    geocode = geocodes['data'].__getitem__(0)
                    geo_dict['latitude'] = geocode['latitude']
                    geo_dict['longitude'] = geocode['longitude']
            except Exception as e:
                self.logger.info(f'Failed to geocode the address <{address}>')
                geo_dict['latitude'] = 0.0
                geo_dict['longitude'] = 0.0

            self.add_new_geocode(address=address, body=geo_dict)

        self.logger.info(f'Geocodes for the address <{address}> are {geo_dict}')
        return geo_dict


gc_coder = PstackCoder()
gc_coder.get_code('SEC E Robinson Avenue & Butterfield Coach Road Springdale, AR')