import pytest
from main import get_weather

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'sunny'}],
        'main': {'temp': 10.0}
    }
    api_key = '493015191bcb9ed0d50cde1ac4c34ae7'
    city = 'Moscow'
    weather_data = get_weather(api_key, city)
    assert weather_data == {'weather': [{'description': 'sunny'}], 'main': {'temp': 10.0}}


def test_get_weather_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404
    api_key = '493015191bcb9ed0d50cde1ac4c34ae7'
    city = 'Moscow'
    weather_data = get_weather(api_key, city)
    assert weather_data == None
