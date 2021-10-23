import requests
import os

SHEET_PRICES_ENDPOINT = os.environ["API_ENDPOINT"]


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEET_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
