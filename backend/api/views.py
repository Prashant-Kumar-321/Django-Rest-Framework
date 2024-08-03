from rest_framework.response import Response
from rest_framework.decorators import api_view

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