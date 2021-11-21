import requests

class FlightSearch:

    def __init__(self):
        self.iata_search_base_url = 'https://tequila-api.kiwi.com/locations/query'
        self.hed = {
            'accept': 'application / json',
            'apikey': '<>'
        }

    def iata_search(self,loc):
        params={
            'term' : loc,
            'locale' : 'en-US',
            'location_types' : 'airport',
            'active_only': 'true',
            'limit':10
        }
        response = requests.get(self.iata_search_base_url,headers=self.hed,params=params)
        return response.json()

    def flight_search(self,fly_to):
        url = 'https://tequila-api.kiwi.com/v2/search'
        params = {
            'fly_from':'EWR',
            'fly_to':fly_to,
            'dateFrom':'01/12/2021',
            'dateTo' : '10/01/2022',
            "curr" : "USD"
        }
        res = requests.get(url,headers=self.hed,params=params)
        return res.json()