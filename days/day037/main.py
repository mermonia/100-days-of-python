import requests
import datetime as dt

TOKEN = "dummytoken"
USERNAME = "dummyusername"
GRAPH_ID = "graph1"

USER_ENDPOINT = "https://pixe.la/v1/users"
GRAPHS_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
MY_GRAPH_ENDPOINT = f"{GRAPHS_ENDPOINT}/{GRAPH_ID}"

authentication_headers = {
        "X-USER-TOKEN": TOKEN
}

target_date = dt.datetime(2025, 6, 30).strftime("%Y%m%d")

TARGET_PIXEL_ENDPOINT = f"{MY_GRAPH_ENDPOINT}/{target_date}"

# User creation API
user_data = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
}
user_creation_response = requests.post(url=USER_ENDPOINT, json=user_data)

# Graph creation API:
graphs_data = {
        "id": GRAPH_ID,
        "name": "Coding Hours",
        "unit": "hour",
        "type": "float",
        "color": "ajisai"
}
graph_creation_response = requests.post(url=GRAPHS_ENDPOINT, json=graphs_data,
                                        headers=authentication_headers)

# Pixel creation API:
pixel_data = {
        "date": target_date,
        "quantity": "2.5",
}
pixel_creation_response = requests.post(url=MY_GRAPH_ENDPOINT, json=pixel_data,
                                        headers=authentication_headers)

# Pixel update API:
pixel_modification_data = {
        "quantity": "5",
}
pixel_modification_response = requests.put(url=TARGET_PIXEL_ENDPOINT,
                                           json=pixel_modification_data,
                                           headers=authentication_headers)

# Pixel deletion API:
pixel_deletion_response = requests.delete(url=TARGET_PIXEL_ENDPOINT,
                                          headers=authentication_headers)
