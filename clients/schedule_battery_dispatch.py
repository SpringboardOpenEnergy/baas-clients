import json
import os
from datetime import datetime, timedelta
import requests

from settings.loader import load_env


def schedule_battery_dispatch(server_url, token,  battery_id):
    headers = {'Authorization': 'Token ' + token}
    url= server_url + '/api/baas/schedule-battery-dispatch/'
    from_date = (datetime.now() + timedelta(hours=4)).replace(minute=0, second=0, microsecond=0)
    to_date = (datetime.today() + timedelta(hours=6)).replace(minute=0, second=0, microsecond=0)
    dispatch_payload = {
        "battery_id": battery_id,
        "from_datetime": from_date.strftime('%Y-%m-%dT%H:%M:%S%z'),
        "to_datetime": to_date.strftime('%Y-%m-%dT%H:%M:%S%z'),
        "regulation": -32
    }
    result = requests.post(url, json=dispatch_payload, headers=headers)
    print(result)
    print(json.dumps(result.json(), indent=2))
    return result.json()


if __name__ == '__main__':
    load_env()
    token = os.environ.get("basic_auth_token")
    server_url = os.environ.get("server_url")
    schedule_battery_dispatch(server_url, token, "f8fb7967-f8c6-4b18-befd-ee6bb0e5a71c")