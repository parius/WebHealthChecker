import requests
from urllib.error import URLError, HTTPError
from timeit import default_timer as timer
from datetime import datetime

class WebChecker:
    def checkLink(self, link):
        start_time = timer()
        try:
            response = requests.head(link)
            time = int((timer() - start_time ) * 1000)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            return (timestamp, link, response.status_code, time)
        except URLError as e:
            print("Problem: " + e)

