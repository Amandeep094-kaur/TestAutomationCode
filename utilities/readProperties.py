import configparser

config= configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url= config.get('common info','BaseURL')
        return url
    @staticmethod
    def getUsername():
        Username = config.get('common info', 'Username')
        return Username

    @staticmethod
    def getPassword():
        Password = config.get('common info', 'Password')
        return Password
