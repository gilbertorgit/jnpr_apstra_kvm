"""
---------------------------------
 Author: Gilberto Rampini
 Date: 05/2021
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


"""
--------------------------------------------------------------------------------------------------------
GETs
"""


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

