"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""

from base_apstra import *
import urls_base_apstra as url_ba
import requests
import json
from time import sleep

requests.packages.urllib3.disable_warnings()


"""
--------------------------------------------------------------------------------------------------------
GETs
"""


def get_asn_pool():

    headers = {'Content-Type':'application/json', 'Cache-Control':'no-cache', 'AUTHTOKEN': get_token()}
    asn_pool_resp = requests.get(f'{url_ba.apstra_url}{url_ba.asn_pool_url}', headers=headers, verify=False)


def get_blueprint_device_id(blueprint_name):

    """
    Get the default device ID in the blueprint. We need this to configure the right device profile
    """
    url = f"{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/experience/web/cabling-map"
    id_list=[]
    response = apstra_get(url=url)

    for id in response.json()['links']:
        id=id['endpoints']
        for value in id:
            id_list.append(value['system'])
    return id_list


def get_blueprint_all_info(blueprint_name):

    """
    get all bluprint info
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}'
    response = apstra_get(url=url)
    return response


def get_blueprint_virtual_network(blueprint_name, vlan_name):

    """
    GET VIRTUAL NETWORK ID
    """
    virtual_network_url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.get_blueprint_virtual_networks}'
    virtual_network_response = apstra_get(url=virtual_network_url)
    virtual_network_response_json = virtual_network_response.json()
    for key, value in virtual_network_response_json['virtual_networks'].items():
        if value['label'] == vlan_name:
            vn_id = key

    return vn_id


def get_deploy_version(blueprint_name):

    """
    get version to commit
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_version_url}'
    response = apstra_get(url=url)
    return response.json()['staging_version']


def get_system_info():
    """
    get all system ids
    """
    url = f'{url_ba.apstra_url}{url_ba.systems_url}'
    response = apstra_get(url=url)
    return response


def get_security_zone(blueprint_name):

    """
    Receive blueprint name
    get and return the default routing instance id
    """

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/nodes?node_type=security_zone'
    response = apstra_get(url=url)

    for key, value in response.json()['nodes'].items():
        if value['vrf_name'] == "default":
            default_zn_id = value['id']
    return default_zn_id


def get_route_policy(blueprint_name):

    """
    Receive blueprint name
    get and return the default apstra bgp policy id
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.routing_policies_url}'
    response = apstra_get(url=url)

    for item in response.json()['items']:
        default_policy_id = item['id']

    return default_policy_id


def get_virtual_network(blueprint_name, vn_name):

    """
    Receive blueprint name and virtual network name
    get and return the virtual network name
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.virtual_network_url}'
    response = apstra_get(url=url)

    for key, value in response.json()['virtual_networks'].items():
        if value['label'] == f'{vn_name}':
            vn_id = key

    return vn_id


def get_ct_policies_id(blueprint_name, ct_name):

    """
       Receive blueprint name and connectivity template name
       get and return the connectivity template id
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.obj_policy_export_url}'
    response = apstra_get(url=url)

    for item in response.json()['policies']:
        if item['label'] == f'{ct_name}':
            ct_policy_id = item['id']

    return ct_policy_id


def get_application_points_id(blueprint_name, vqfx_name, interface: str):

    """
           Receive blueprint name vqfx_name, interface
           return interface id
    """
    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.obj_policy_application_points_url}'
    response = apstra_get(url=url)

    for item in response.json()['application_points']['children']:
        for a in item['children']:
            if a['label'] == f'{vqfx_name}':
                for b in a['children']:
                    for c in b['children']:
                        if interface in c['label']:
                            interface_id = c['id']

    return interface_id


def get_external_router_id(blueprint_name, vqfx_name):

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/nodes'
    response = apstra_get(url=url)

    external_link_id = []
    for key,value in response.json()['nodes'].items():
        if value != None:
            for qfx in vqfx_name:
                if value.get('label') == f'{qfx}':
                    bl_id = (value.get('id'))
                    external_link_id.append(f'"{bl_id}"')

    list_json = ','.join(set(external_link_id))
    return list_json


def get_virtual_network_policy_id(blueprint_name):

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/nodes'
    response = apstra_get(url=url)

    for key, value in response.json()['nodes'].items():
        if value != None:
            if value.get('type') == "virtual_network_policy":
                bl_id = (value.get('id'))

    return bl_id