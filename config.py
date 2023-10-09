class Config:
    def __init__(self,
                 host_name: str = "localhost",
                 server_port: int = 8080,
                 templates_folder: str = 'templates'
                 ):
        self.templates_folder = templates_folder
        self.serverPort = server_port
        self.hostName = host_name


config = Config()
