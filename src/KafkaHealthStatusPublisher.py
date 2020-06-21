from kafka import KafkaProducer
import json

class KafkaHealthStatusPublisher:
    def __init__(self, settings):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.getKafkaServerURL(),
            security_protocol="SSL",
            ssl_cafile=settings.getKafkaCAFile(),
            ssl_certfile=settings.getKafkaCertFile(),
            ssl_keyfile=settings.getKafkaKeyFile(),
            api_version=(0,11,5),
        )
        self.topic = settings.getKafkaTopic()

    def send(self, data):
        print("Sending: {}".format(data))
        self.producer.send(self.topic, json.dumps(data).encode("utf-8"))
        self.producer.flush()


