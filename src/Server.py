import argparse
from src.KafkaHealthStatusReceiver import KafkaHealthStatusReceiver as HealthStatusReceiver
from src.SettingsProvider import SettingsProvider
from src.PostgreSQLWriter import PostgreSQLWriter

class Server:
    def init(self, config_file):
        settings = SettingsProvider(config_file)
        self.producer = HealthStatusReceiver(settings)
        self.consumer = PostgreSQLWriter(settings)

    def run(self):
        while True:
            msgs = self.producer.receive()
            for msg in msgs:
                print("Sending to DB:", msg)
                self.consumer.send(msg)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform health status aggegation and stoarage in DB')
    parser.add_argument("config", metavar="config_file")
    args = parser.parse_args()

    server = Server()
    server.init(args.config)
    server.run()