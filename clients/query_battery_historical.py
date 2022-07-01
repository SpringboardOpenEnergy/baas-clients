import json
import os

import requests

from settings.loader import load_env




def retrieve_historical_data(server_url, token,  battery_id):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/baas/query-battery-data/'
    qry_payload = {
        "battery_id": battery_id,
        "from_datetime": "2022-06-12T00:00:00+02:00",
        "to_datetime": "2022-06-23T00:00:00+02:00",
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
    retrieve_historical_data(server_url, token, "28ba98df-39e2-46d3-825c-0832ec06b862")