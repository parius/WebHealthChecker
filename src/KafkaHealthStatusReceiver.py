from kafka import KafkaConsumer
import json

class KafkaHealthStatusReceiver:
    def __init__(self, settings):
        self.consumer = KafkaConsumer(
            settings.getKafkaTopic(),
            auto_offset_reset="earliest",
            bootstrap_servers=settings.getKafkaServerURL(),
            client_id="demo-client-1",
            group_id="demo-group",
            security_protocol="SSL",
            ssl_cafile=settings.getKafkaCAFile(),
            ssl_certfile=settings.getKafkaCertFile(),
            ssl_keyfile=settings.getKafkaKeyFile(),
        )

    def receive(self):
        raw_msgs = self.consumer.poll(timeout_ms=1000)
        result = []
        for msgs in raw_msgs.values():
            for msg in msgs:
                mydata = json.loads(msg.value.decode("utf-8"))
                print("Received > ", mydata)
                result.append(mydata)
        self.consumer.commit()
        return result
