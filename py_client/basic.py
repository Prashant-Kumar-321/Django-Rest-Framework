import requests 

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything" 
endpoint = "http://localhost:8000/api/" 

response = requests.get(endpoint, params={"address": "Pundag Road, 84002"}, json={"query": "Hello World!"})
# print(response.text)
print(response.json()) 
print(response.status_code)

# HTTP Request -> HTML 
# REST API HTTP Request -> JSON 
# Javascript Object Notation ~ Python Dict

