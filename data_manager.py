import requests
from datetime import datetime

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.read_url = '<>'
        self.update_url = '<>'
    def read_data(self):
        response = requests.get(self.read_url)
        print(response.json())
        return response.json()

    def update_data(self,id,body):
        url = f"{self.update_url}{id}"
        response = requests.put(url, json=body)
        print(response.json())
        return response.json()
