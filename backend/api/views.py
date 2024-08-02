from django.http import JsonResponse 
import datetime

def api_home(request, *args, **kwargs):
    return JsonResponse({
        "message": "Hi there, This is Django Json Response",
        "Author": "Prashant Kumar Gupta",
    }) 