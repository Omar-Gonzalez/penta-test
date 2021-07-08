from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class FetchIpData(APIView):

    def get(self, request, *args, **kwargs):
        ip = self.kwargs['ip']
        error = False

        try:
            r = requests.get(f'http://ip-api.com/json/{ip}')
        except Exception as e:
            error = str(e)

        if error:
            return Response({'error':error})
        else:
            return Response(r.json())
