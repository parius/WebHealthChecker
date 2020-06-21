from setuptools import setup

setup(
   name='WebHealthCheck',
   version='0.1',
   description='Agent-Server system for collecting and aggregation of website statuses',
   packages=['src', 'tests'],
   install_requires=['kafka-python', 'requests', 'psycopg2', 'pytest'],
    entry_points={
        'console_scripts': [
            'agent=Agent:main',
            'server=Server:main',
        ],
    },
)