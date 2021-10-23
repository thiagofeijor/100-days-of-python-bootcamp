import requests
from constants import *

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": input("How many hours did you study today? ")
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)
