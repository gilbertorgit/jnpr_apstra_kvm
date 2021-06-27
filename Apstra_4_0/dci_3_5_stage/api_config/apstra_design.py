"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import requests
import json
from time import sleep
import base_apstra as ba
import urls_base_apstra as url_ba

requests.packages.urllib3.disable_warnings()


def create_logical_device(name, data):

    print(f'--------------------Creating Logical Devices: {name}')

    url = f'{url_ba.apstra_url}{url_ba.logical_device_design_url}'
    data = data
    response = ba.apstra_post(url=url, data=data)
    return response


def create_interface_map(name, data):

    print(f'--------------------Creating Interface Maps: {name}')

    url = f'{url_ba.apstra_url}{url_ba.interface_maps_url}'
    data = data
    response = ba.apstra_post(url=url, data=data)
    return response


def create_rack_type(name, data):

    print(f'--------------------Creating Racks: {name}')

    url = f'{url_ba.apstra_url}{url_ba.rack_design_url}'
    data = data
    response = ba.apstra_post(url=url, data=data)
    return response


def create_template(name, data):

    print(f'--------------------Creating Templates: {name}')

    url = f'{url_ba.apstra_url}{url_ba.template_design_url}'
    data = data
    response = ba.apstra_post(url=url, data=data)
    return response
