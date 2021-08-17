import cerridwen
from django.shortcuts import render
import pytz
from django.utils import timezone
import requests

# Create your views here.

# time = cerridwen.jd_now()
# info2 = cerridwen.jd2iso(time)
#
# print(info2)


freegeoip_response = requests.get('http://freegeoip.net/json')
freegeoip_response_json = freegeoip_response.json()
user_time_zone = freegeoip_response_json['time_zone']


timezone.activate(pytz.timezone(user_time_zone))
