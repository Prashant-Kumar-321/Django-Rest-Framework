from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json -> used to convert byte data into python dict
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse

from product.models import Product
from product.serializers import ProductSerializer 

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data) 
    if serializer.is_valid(raise_exception=False): 
        # instance = serializer.save() # save the instance to the data base
        # print(serializer.data)  
        return Response(serializer.data)
    
    return Response({"data": "Not a valid data"}, status=400)


@api_view(["GET", "POST", "DELETE", "PUT", "PATCH"]) 
# @csrf_exempt
def echo_users_request(request): 
    """
    if request.method == 'POST': 
        print(request.GET)
        print(json.loads(request.body)) 
        return JsonResponse({"status": "data submitted successfully"}, status=200)
        # in django based request object doesn't have data attribute like drf request object has
    """
    
    if request.content_type !='application/json': 
        return Response({"status": "request body must be 'application/json'" }, status=400)
    response = {} 
    response['method'] = request.method
    response['data'] = request.data  # Data , client has sent 
    response['content-type'] = request.content_type
    response['params'] = request.GET         # Client's request parameters

    # Query parameters
    # query_param = request.GET.get('param')

    # JSON data from the body
    # json_data = request.data

    # Form data (if any)
    # form_data = request.POST

    # print(request.GET)  
    # print(request.POST)

    return Response(response, status=200)
