from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .parsing import parse_last_post

@api_view(['POST'])
def add_new_post(request):
    post = parse_last_post()
    print(request.data)
    return Response(post)
