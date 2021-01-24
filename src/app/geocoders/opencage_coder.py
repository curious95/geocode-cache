from opencage.geocoder import OpenCageGeocode

from src.app.GeocodeBase import GeocodeBase
from src import log


class OpenCageCoder(GeocodeBase):

    def __init__(self):
        super().__init__()
        self.opcoder = OpenCageGeocode(self.config.opencage_key)
        self.logger = log.setup_custom_logger('OPCAGE_API_CONTROLLER')

    def get_code(self, address):

        geo_dict = dict()

        self.logger.info(f'Looking up address <{address}>')

        is_address_present = self.geocode_lookup(address=address)

        if is_address_present:
            self.logger.info(f'Cached geocodes found for address <{address}>')
            geo_dict['latitude'] = is_address_present['_source']['latitude']
            geo_dict['longitude'] = is_address_present['_source']['longitude']
        else:
            self.logger.info(f'Address <{address}> not present in cache :: Fetching it Freshly')
            try:
                geocodes = self.opcoder.geocode(address)
                if geocodes is not None:
                    geocode = geocodes.__getitem__(0)
                    location = geocode["geometry"]
                    geo_dict['latitude'] = location['lat']
                    geo_dict['longitude'] = location['lng']
            except Exception as e:
                self.logger.info(f'Failed to geocode the address <{address}>')
                geo_dict['latitude'] = 0.0
                geo_dict['longitude'] = 0.0

            self.add_new_geocode(address=address, body=geo_dict)

        self.logger.info(f'Geocodes for the address <{address}> are {geo_dict}')
        return geo_dict


gc_coder = OpenCageCoder()
gc_coder.get_code('SEC E Robinson Avenue & Butterfield Coach Road Springdale, AR')