import os
from django.template import loader
from django.http import JsonResponse
import requests as rq
import json
from .models import City_master,City_weather
from .util import *
# Create your views here.


def report(request):
    key='city'
    if request.method == 'POST':
        post_data = request.POST[key]
    else:
        post_data = request.GET[key]

    apiurl=os.getenv('WEATHER_API_URL')
    #exception delivery is in the exception middleware
    if apiurl == None:
        raise Exception('no_api_url')
    else:
        try:
            resp=rq.get(apiurl+post_data)
            status_code=resp.status_code
            apicontent=json.loads(resp.content)
            
        except Exception as e:
            if str(e).index("ConnectTimeoutError"):
                raise Exception('timeout')
            else:
                raise Exception('servererror')
 
    #to use model ,you must setting your database in setting.py
    #city = City_master.objects.create(city_id=post_data,country=apicontent['location']['country'])

    #city_weather = City_weather.objects.create(city=city,weather_information=apicontent['location']['current'],date=apicontent['location']['localtime'])
    #save the weather information to database
    #city.save()
    #city_weather.save()
    
    response = JsonResponse(apicontent,content_type='application/json;charset=UTF-8',status=status_code)   
    return response