import requests 

#endpoint = "https://httpbin.org/status/200"
#endpoint = "https://httpbin.org/anything" 
endpoint = "http://localhost:8000/api/" 

json = {
    "title": "Hello World", 
    "content": "content",
    "price": "ddfdf34.5",
    # "price": 234.54,
}

response = requests.post(endpoint, json=json)
# print(response.text)
print(response.status_code)
print(response.json()) 

# HTTP Request -> HTML 
# REST API HTTP Request -> JSON 
# Javascript Object Notation ~ Python Dict

