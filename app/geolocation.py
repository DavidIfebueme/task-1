import requests
from flask import request

def get_client_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return ip

def get_geolocation(client_ip):
    api_key = '88fc2cf25b7142d69b6516596792d0de' #no de look my keys. its free go get your own
    base_url = 'https://ipgeolocation.abstractapi.com/v1/'
    geo_url = f'{base_url}?api_key={api_key}&ip_address={client_ip}'
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    return geo_data.get('city')


