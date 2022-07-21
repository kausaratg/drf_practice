from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSeriliazers

@api_view(['GET'])
def index(request):
    items = Item.objects.all()
    serializer = ItemSeriliazers(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serialier = ItemSeriliazers(data=request.data)
    if serialier.is_valid():
        serialier.save()
    return Response(serialier.data)