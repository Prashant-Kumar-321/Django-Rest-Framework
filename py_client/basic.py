import requests 

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything" 
# endpoint = "http://localhost:8000/api/" 
endpoint = "http://localhost:8000/api/echo/"

json = {
    "title": "Hello World", 
    "content": "This is description about the item",
    "price": "54.5",
}

params = {
    "lat": "23.6575655", 
    "lng": "85.946647", 
    "type": "school",
}

response = requests.patch(endpoint, params=params, json=json)
# print(response.text)
print(response.status_code)
print(response.json()) 

# HTTP Request -> HTML 
# REST API HTTP Request -> JSON 
# Javascript Object Notation ~ Python Dict

