from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def my_view(request):
    # Your code here
    return Response("Hello, World!")

