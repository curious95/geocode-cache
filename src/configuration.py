import os


class Config:
    """
    Configuration class to store all the env vars
    """

    def __init__(self):
        self.gmaps_key = os.getenv('GMAPKEY', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.pstack_key = os.getenv('PSTACKEY', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.opencage_key = os.getenv('OPCAGEKEY', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.es_host = os.getenv('ESHOST', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.es_port = os.getenv('ESPORT', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.es_pass = os.getenv('ESPASS', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.es_user = os.getenv('ESUSER', 'XXXXXXXXXXXXXXXXXXXXXXXX')
        self.es_index = os.getenv('EINDEX ', 'XXXXXXXXXXXXXXXXXXXXXXXX')
