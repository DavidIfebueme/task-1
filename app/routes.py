import json
from flask import Blueprint, request, Response
from .geolocation import get_geolocation, get_client_ip
from .weather import get_weather

main = Blueprint('main', __name__)


@main.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name')
    client_ip = get_client_ip()
    city = get_geolocation()
    temperature = get_weather(city)

    if temperature is None:
        temperature_str = 'No whyne me. I take God beg you'
    else:
        temperature_str = f'{temperature} degrees Celsius'

    greeting = f'Hello, {visitor_name}!, the temperature is {temperature_str} in {city}'

    response = {
        'client_ip': client_ip,
        'location': city,
        'greeting': greeting,
    }

    response_str = json.dumps(response, indent=2)
    return Response(response=response_str, mimetype='application/json')

