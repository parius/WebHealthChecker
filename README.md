![Build](https://github.com/parius/WebHealthChecker/workflows/Build/badge.svg) [![codecov](https://codecov.io/gh/parius/WebHealthChecker/branch/master/graph/badge.svg)](https://codecov.io/gh/parius/WebHealthChecker)



# Website Health Checker

System that monitors website availability over the
network, produces metrics about this and passes these events through an
Kafka instance into an PostgreSQL database.

----
Basic architecture and intended usage

python agent.py config.json sites.json

python server.py config.json

----
Code snippets for working with Kafka were taken from 
https://help.aiven.io/en/articles/489572-getting-started-with-aiven-kafka
