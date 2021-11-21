
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

sheet_api = DataManager()
kiwi_api = FlightSearch()
data_search = FlightData()
data = sheet_api.read_data()

for ele in data["prices"]:
    #print(ele['city'])
    sheet_id = int(ele['id'])
    iata_list = kiwi_api.iata_search(ele['city'])
    #print(iata_list)
    iata_code = iata_list['locations'][0]['id']
    if ele['iataCode'] == "":
        text_update = {
            'price':{
                'iataCode': iata_list['locations'][0]['id'],
            }
         }
        res = sheet_api.update_data(sheet_id, text_update)
    response = kiwi_api.flight_search(iata_code)
    data_search.data_search(response,10)

