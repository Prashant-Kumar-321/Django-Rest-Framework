import requests 

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything" 

response = requests.get(endpoint, json={"query": "Hello World!"})
# print(response.text) 
# print(response.json()) 
# print(response.status_code)

