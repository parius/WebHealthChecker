from ..src.SettingsProvider import SettingsProvider

class TestSettingsProvider:
    def test_read_success(self):
        p = SettingsProvider('tests/sample_config.json')
        assert p.getCheckInterval() == 30
        assert p.getDBDatabase() == "testdb"
        assert p.getDBHost() == "localhost/db"
        assert p.getDBPassword() == "notapassword"
        assert p.getDBPort() == "14450"
        assert p.getDBUser() == "postgres"
        assert p.getKafkaCAFile() == "cert/ca.pem"
        assert p.getKafkaCertFile() == "cert/service.cert"
        assert p.getKafkaKeyFile() == "cert/service.key"
        assert p.getKafkaServerURL() == "localhost/kafka:14452"
        assert p.getKafkaTopic() == "kafka-topic"