import json


class MonitoredSitesProvider:
    def __init__(self, filename):
        with open(filename) as config_file:
            self.sites = json.load(config_file)

    def getLinks(self):
        return self.sites
