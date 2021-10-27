import requests
from PIL import Image

endpoint = "https://dog.ceo/api/breeds/image/random"


response = requests.get(endpoint)
response.raise_for_status()
response = response.json()

raw_img = requests.get(response['message'], stream=True).raw

img = Image.open(raw_img)
img.show()
