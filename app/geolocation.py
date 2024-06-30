import requests
from flask import request

def get_geolocation():
    client_ip = request.remote_addr
    api_key = '88fc2cf25b7142d69b6516596792d0de'
    base_url = 'https://ipgeolocation.abstractapi.com/v1/'
    geo_url = f'{base_url}?api_key={api_key}&ip_address={client_ip}'
    geo_response = requests.get(geo_url)
    geo_data = geo_response.json()
    return geo_data.get('city')
