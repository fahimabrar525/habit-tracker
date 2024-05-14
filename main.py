import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "thisissecret"
USER_NAME = "abrar"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# # print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

graph_value_params = {
    "date": formatted_today,
    "quantity": input("How many kilometers you cycling today?: ")
}

response = requests.post(url=pixel_creation_endpoint, json=graph_value_params, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today}"

pixel_update_params = {
    "quantity": "4.5"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_today}"

# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)

