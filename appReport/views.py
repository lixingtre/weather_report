import os
from django.shortcuts import render
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests as rq
import json
from .models import City_master,City_weather
# Create your views here.

def report(request):
    result_dic = {}
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
            resp=rq.post(apiurl+'/'+post_data)
            status_code=resp.status_code
            result_dic["api_result"]=resp.content
        except Exception as e:
            if str(e).index("ConnectTimeoutError"):
                raise Exception('timeout')
            else:
                raise Exception('servererror')

    city = City_master.objects.create(city_id=post_data,city_name=resp.content.city_name)
    city_weather = City_weather.objects.create(city=city,weather_information=resp.content.weather,date=resp.content.date)
    #save the weather information to database
    city.save()
    city_weather.save()
    result_json=json.dumps(result_dic)
    response = HttpResponse(result_json,content_type='application/json;charset=UTF-8',status=status_code)   
    return response