import argparse
import time

from src.KafkaHealthStatusPublisher import KafkaHealthStatusPublisher as HealthPublisher
from src.MonitoredSitesProvider import MonitoredSitesProvider
from src.SettingsProvider import SettingsProvider
from src.WebChecker import WebChecker


class Agent:
    def init(self, config_file, sites_file):
        self.settings = SettingsProvider(config_file)
        self.sitesRegister = MonitoredSitesProvider(sites_file)
        self.web = WebChecker()
        self.consumer = HealthPublisher(self.settings)

    def monitoring_step(self):
        for link in self.sitesRegister.getLinks():
            print("Checking " + link + "...", end='')
            res = self.web.checkLink(link)
            self.consumer.send(res)

    def run(self):
        print("Start health check monitoring")
        while True:
            self.monitoring_step()
            timeout = self.settings.getCheckInterval()
            print("Sleeping for " + str(timeout) + " seconds")
            time.sleep(timeout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform health status gathering and publish to Kafka')
    parser.add_argument("config", metavar="config_file")
    parser.add_argument("sites", metavar="sites_file")
    args = parser.parse_args()

    agent = Agent()
    agent.init(args.config, args.sites)
    agent.run()
