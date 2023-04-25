
from django.urls import path

from .views import (
    add_new_post
)


app_name = 'webhooks_api'


urlpatterns = [
    path('new/', add_new_post),
]