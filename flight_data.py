import requests
from notification_manager import NotificationManager

class FlightData:

    def data_search(self,data,min_price):
        twilio_message = NotificationManager()
        for item in data['data']:
            if int(item['price']) < int(min_price):
               print("lowest")
               message = f"low price alert {item['flyFrom']},{item['cityFrom']} to {item['flyTo']}, {item['cityTo']} on {item['local_departure']} to {item['local_arrival']} at {item['price']} USD"
               twilio_message.send_sms(message)
