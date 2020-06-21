from datetime import datetime
from ..src.Agent import Agent

class WebCheckerMock:
    def checkLink(self, link):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return (ts, SitesMock.site, 404, 10)

class KafkaPublisherMock:
    def send(self, data):
        self.result = data
class SettingsProviderMock:
    def getCheckInterval(self): return 0
class SitesMock:
    site = "localhost"
    def getLinks(self): return [self.site]

class TestAgent:
    def test_creation(self):
        agent = Agent()
        agent.init('tests/sample_config.json', 'tests/sample_sites.json')
        assert agent.consumer
        assert agent.settings
        assert agent.web
        assert agent.sitesRegister

    def test_monitoring_step_success(self):
        agent = Agent()
        agent.web = WebCheckerMock()
        agent.consumer = KafkaPublisherMock()
        agent.settings = SettingsProviderMock()
        agent.sitesRegister = SitesMock()

        agent.monitoring_step()

        assert agent.consumer.result[1] == SitesMock.site
        assert agent.consumer.result[2] == 404
        assert agent.consumer.result[3] == 10