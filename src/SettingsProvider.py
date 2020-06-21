import json

class SettingsProvider:
    def __init__(self, filename):
        with open(filename) as config_file:
            self.data = json.load(config_file)

    def getKafkaTopic(self):
        return self.data['KafkaTopic']

    def getKafkaServerURL(self):
        return self.data['KafkaServerURL']

    def getKafkaCAFile(self):
        return self.data['KafkaCAFile']

    def getKafkaCertFile(self):
        return self.data['KafkaCertFile']

    def getKafkaKeyFile(self):
        return self.data['KafkaKeyFile']

    def getDBUser(self):
        return self.data['DBUser']

    def getDBPassword(self):
        return self.data['DBPassword']

    def getDBHost(self):
        return self.data['DBHost']

    def getDBPort(self):
        return self.data['DBPort']

    def getDBDatabase(self):
        return self.data['DBDatabase']

    def getCheckInterval(self):
        return int(self.data['HealthCheckIntervalSec'])
