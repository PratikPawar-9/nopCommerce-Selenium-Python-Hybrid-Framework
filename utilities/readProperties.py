import configparser

config = configparser.RawConfigParser()
config.read('.\\Configurations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password


 #static method : methods which can access directly without making objs
# used this so no need to create the obj to call the method inside class