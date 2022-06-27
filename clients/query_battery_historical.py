import json
import os

import requests

from settings.loader import load_env




def retrieve_historical_data(server_url, token,  battery_id):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/baas/query-battery-data/'
    qry_payload = {
        "battery_id": battery_id,
        "from_datetime": "2021-05-07 00:00:00",
        "to_datetime": "2022-06-23 00:00:00",
        "resolution": "Day"
    }
    result = requests.post(url, json=qry_payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    return result.json()


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    retrieve_historical_data(server_url, token, "47a3d71e-7165-4604-a6d2-c210af8a33dd")