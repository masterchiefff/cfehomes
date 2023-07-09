import json
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import productSerializer

@api_view(["GET"])
def api_home(req, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}

    if instance:
        data = productSerializer(instance).data
    return Response(data)