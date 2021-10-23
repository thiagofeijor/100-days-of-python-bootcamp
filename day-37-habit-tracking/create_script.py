import requests
from constants import *

# CREATE USER
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Study English",
    "unit": "h",
    "type": "float",
    "color": "ajisai"
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
