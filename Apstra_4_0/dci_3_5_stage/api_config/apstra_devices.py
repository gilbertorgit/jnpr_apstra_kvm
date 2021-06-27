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
from ipaddress import ip_address

requests.packages.urllib3.disable_warnings()


def create_ip_list(start, end):

    start_int = int(ip_address(start).packed.hex(), 16)
    end_int = int(ip_address(end).packed.hex(), 16)
    return [ip_address(ip).exploded for ip in range(start_int, end_int)]


def create_offbox_device(start_ip, end_ip, username=f'lab', password=f'lab123', platform=f'junos',
                         agent_type='offbox', operation_mode='full_control'):

    print(f'--------------------Creating Offbox Devices')
    url = f'{url_ba.apstra_url}{url_ba.system_gent_url}'

    mgmt_list = create_ip_list(start_ip, end_ip)
    response_list = []
    for ip in mgmt_list:
        print(f'--------------------Creating offbox device: {ip}')
        data = f'''{{
        "username": "{username}",
        "password": "{password}",
        "job_on_create": "check",
        "platform": "{platform}",
        "management_ip": "{ip}",
        "agent_type": "{agent_type}",
        "operation_mode": "{operation_mode}"
        }}'''
        response = ba.apstra_post(url=url, data=data)
        response_list.append(response)
        sleep(2)
    return response_list


def manage_device(system_id, model):

    url = f'{url_ba.apstra_url}{url_ba.systems_batch_update}'

    data = f'''{{"{system_id}": 
    {{"user_config": 
    {{
    "aos_hcl_model": "{model}", 
    "admin_state": "normal"
    }}
    }}
    }}'''
    response = ba.apstra_post(url=url, data=data)
    return response


def manage_device_all():

    device_list_url = f'{url_ba.apstra_url}{url_ba.systems_url}'
    device_list_response = ba.apstra_get(device_list_url).json()

    device_list_all = []

    for device in device_list_response['items']:

        print(f"--------------------Managing Device: {device['status']['hostname']} IP: {device['facts']['mgmt_ipaddr']}")

        system_id = device['id']
        model = device['facts']['aos_hcl_model']
        response = manage_device(system_id, model)
        device_list_all.append(response)

    return device_list_all