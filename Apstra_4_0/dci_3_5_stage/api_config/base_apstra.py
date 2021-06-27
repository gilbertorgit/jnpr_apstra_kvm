"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import requests
import json
import urls_base_apstra as url_ba


requests.packages.urllib3.disable_warnings()


"""
--------------------------------------------------------------------------------------------------------
Basic GET, PUT, Token etc.
"""


def get_token():
    data = {'username': url_ba.username, 'password': url_ba.password}
    auth_resp = requests.post(f'{url_ba.apstra_url}{url_ba.login_url}', data=json.dumps(data), verify=False)

    return auth_resp.json()['token']


def apstra_get(url):
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'AUTHTOKEN': get_token()}
    response = requests.get(url, headers=headers, verify=False)
    return response


def apstra_post(url, data):
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'AUTHTOKEN': get_token()}
    response = requests.post(url, data=data, headers=headers, verify=False)
    return response


def apstra_put(url, data):
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'AUTHTOKEN': get_token()}
    response = requests.put(url, data=data, headers=headers, verify=False)
    return response


def apstra_patch(url, data):
    headers = {'Content-Type': 'application/json', 'Cache-Control': 'no-cache', 'AUTHTOKEN': get_token()}
    response = requests.patch(url, data=data, headers=headers, verify=False)
    return response
