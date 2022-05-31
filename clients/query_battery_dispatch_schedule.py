import json
import os
from datetime import datetime, timedelta
import requests

from settings.loader import load_env


def query_battery_dispatch(server_url, token,  battery_id):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/baas/query-battery-dispatch-schedule/'
    query_payload = {
        "battery_id": battery_id,
    }
    result = requests.post(url, json=query_payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    return result.json()


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    query_battery_dispatch(server_url, token, "f8fb7967-f8c6-4b18-befd-ee6bb0e5a71c")