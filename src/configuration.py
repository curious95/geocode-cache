import os


class Config:
    """
    Configuration class to store all the env vars
    """

    def __init__(self):
        self.driver = os.getenv('SOURCE', 'geckodrivermac')
        self.index = os.getenv('API_KEY', 'zoning_data')
        self.es_user = os.getenv('ESUSER', 'elastic')
        self.es_host = os.getenv('ESHOST', '35.223.3.40')
        self.es_pass = os.getenv('ESPASS', '7aFypVtVPbFcWdF')
        self.es_port = os.getenv('ESPORT', '9200')
