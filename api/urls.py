from django.conf.urls import include
from django.urls import path

app_name='api'

urlpatterns = [
    path('ws/v1/', include('api.v1.urls', namespace='ws/v1'))
]