import configparser
config = configparser.ConfigParser()
config.read('/Users/olatundeolawoyin/PycharmProjects/Assessmentpart1/Configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsermail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password





