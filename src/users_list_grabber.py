import requests
import json

try:
    response = requests.get('https://reqres.in/api/users?page=2', timeout=10)
    print(response)
    response.raise_for_status()
    print(response.json())
    with open("users_list.json", 'w') as f:
	    json.dump(response.json(), f, indent=4)
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)
