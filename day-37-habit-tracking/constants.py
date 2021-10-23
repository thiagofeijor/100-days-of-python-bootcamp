from datetime import datetime

USERNAME = "thiagofeijor"
TOKEN = "thisissecret"
GRAPH_ID = "englishstudy1995"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()
