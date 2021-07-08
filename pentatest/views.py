from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
import requests

class FetchIpData(APIView):

    def get(self, request, *args, **kwargs):
        ip = self.kwargs['action']
        error = False

        try:
            r = requests.get(f'http://ip-api.com/json/{ip}')
        except Exception as e:
            error = str(e)

        rjson = r.json()

        res = {
              "action": "track",
              "info": {
                "ip": ip,
                "resolution": {
                  "width": 0, #no idea here
                  "height": 0
                }
              },
              "location": {
                "longitude": rjson['lon'],
                "latitude": rjson['lat'],
                "city": rjson['city'],
                "region": rjson['regionName'],
                "country": rjson['country'],
                "country_code": rjson['countryCode']
              },
              "action_date": datetime.datetime.now()
            }

        if error:
            return Response({'error':error})
        else:
            return Response(res)
