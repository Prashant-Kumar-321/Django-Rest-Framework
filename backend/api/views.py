import json
from django.http import JsonResponse 
import datetime

def api_home(request, *args, **kwargs):
    # request -> instance of HttpRequest -> Django
    # print(request.content_type) # application/json OR application/x-www-form-urlencoded
    data = {} 
    body = request.body # byte String of JSON data [json, data]
    
    # handling if body is not byte of string of json data
    try: 
        data = json.loads(body) # string of JSON data -> Python Dict
    except: 
        # print("Json data is missing");
        # return JsonResponse({
        #     "message": "", 
        #     "Author": "Prashant Kumar Gupta", 
        #     "status": "Json data is missing",
        # })
        pass 

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content-type'] = request.content_type
    
    return JsonResponse(data) 