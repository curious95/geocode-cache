import os


class Config:
    """
    Configuration class to store all the env vars
    """

    def __init__(self):
        self.gmaps_key = os.getenv('GMAPKEY', '')
        self.pstack_key = os.getenv('PSTACKEY', '')
        self.port = os.getenv('PORT', '')
        self.db_host = os.getenv('DBHOST', '')
        self.db_port = os.getenv('DBPORT', '')
        self.db_pass = os.getenv('DBPASS', '')
        self.db_user = os.getenv('DBUSER', '')
