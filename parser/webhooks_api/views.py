from django.shortcuts import render
from pprint import pprint
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .parsing import Parser
from .webhook import WebHook
from .ftp_client import Comnnection

@api_view(['POST'])
def add_new_post(request):
    post_id = WebHook.get_id_new_post()
    print(post_id)
    # if post_id:
    #     ftp_links = Parser(post_id).parse_ftp_link
    #     Comnnection.get_files(ftp_links)
    return Response(status.HTTP_200_OK)
