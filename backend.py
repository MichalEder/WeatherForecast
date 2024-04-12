import requests


def get_data(place, api_key):
    headers = {"accept": "application/json"}
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={place}&apikey={api_key}'
    response = requests.get(url, headers=headers)

    if response.status_code == 400:
        return '400', '400'

    if response.status_code == 429:
        return '429','429'
    try:
        data = response.json()
        place_response = data['location']['name']
        data_hourly = data['timelines']['hourly']
    except KeyError:
        return None

    return data_hourly, place_response
