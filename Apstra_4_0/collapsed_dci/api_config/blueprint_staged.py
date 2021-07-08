"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
from apstra_gets import *
from base_apstra import *
import urls_base_apstra as url_ba
import json
import requests
from time import sleep

requests.packages.urllib3.disable_warnings()

"""
--------------------------------------------------------------------------------------------------------
Create Blueprint
"""


def create_blueprint(blueprint_name, template_name):

    print(f'--------------------Creating blueprint name {blueprint_name} based on template_name: {template_name}')

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}'

    data = f'''
        {{"design":"two_stage_l3clos", 
        "init_type":"template_reference",
        "label":"{blueprint_name}",
        "template_id":"{template_name}", 
        "id":"{blueprint_name}"}}
    '''
    response = apstra_post(url=url, data=data)
    return response


def blueprint_resource_asn_superspine(blueprint_name, asn_pool):

    print(f"--------------------Assigning SuperSpine ASN: {asn_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resource_group_asn_superspine_url}'
    data = f'''
    {{"pool_ids":["{asn_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_asn_spine(blueprint_name, asn_pool):

    print(f"--------------------Assigning Spine ASN: {asn_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_asn_spine_url}'
    data = f'''
    {{"pool_ids":["{asn_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_asn_leaf(blueprint_name, asn_pool):

    print(f"--------------------Assigning Leaf ASN: {asn_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_asn_leaf_url}'
    data = f'''
    {{"pool_ids":["{asn_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_superspine(blueprint_name, loopback_pool):

    print(f"--------------------Assigning SuperSpine loopback: {loopback_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_loopback_superspine_url}'
    data = f'''
    {{"pool_ids":["{loopback_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_spine(blueprint_name, loopback_pool):

    print(f"--------------------Assigning spine loopback: {loopback_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_loopback_spine_url}'
    data = f'''
    {{"pool_ids":["{loopback_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_leaf(blueprint_name, loopback_pool):

    print(f"--------------------Assigning leaf loopback: {loopback_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_loopback_leaf_url}'
    data = f'''
    {{"pool_ids":["{loopback_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_fabric_spine_superspine(blueprint_name, fabric_pool):

    print(f"--------------------Assigning Spine-SuperSpine fabric IP: {fabric_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_spine_superspine_link_url}'
    data = f'''
    {{"pool_ids":["{fabric_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_fabric_spine_leaf(blueprint_name, fabric_pool):

    print(f"--------------------Assigning Spine-Leaf fabric IP: {fabric_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_spine_leaf_link_url}'
    data = f'''
    {{"pool_ids":["{fabric_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    print(response.json())
    return response


def blueprint_resource_generic_link_ip(blueprint_name, ip_pool):

    print(f"--------------------Assigning external router IP: {ip_pool} to blueprint: {blueprint_name}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resource_groups_ip_to_generic_link_ips_url}'
    data = f'''
    {{"pool_ids":["{ip_pool}"]}}
    '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_device_profile_3_stage(blueprint_name, spine_device, leaf_device, borderleaf_device):

    print(f"--------------------Assigning 3-stage Device profile: {spine_device}, {leaf_device}, "
          f"{borderleaf_device} to blueprint: {blueprint_name}")

    """
    Define 3 Stage clos device profile.
    Get the list of device using: ba.get_blueprint_device_id
    and based on that, define the right device profiles
    """

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_interface_map_assignments_url}'

    device_id_list = get_blueprint_device_id(blueprint_name)

    interface_maps = {}

    for id in device_id_list:
        if id != None:
            if id['role'] == 'spine':
                interface_maps[id['id']] = spine_device
            elif id['label'] == 'jnpr_border_leaf_001_leaf1':
                interface_maps[id['id']] = borderleaf_device
            elif id['role'] == 'leaf':
                interface_maps[id['id']] = leaf_device

    data = f'''
    {{"assignments":
    {json.dumps(interface_maps)}
    }}
    '''

    response = apstra_put(url=url, data=data)
    return response


def blueprint_device_profile_5_stage(blueprint_name, superspine_device, spine_device, leaf_device, borderleaf_device):

    print(f"--------------------Assigning 5-stage Device profile: {superspine_device}, {spine_device}, {leaf_device}, "
          f"{borderleaf_device} to blueprint: {blueprint_name}")

    """
    Define 5 Stage clos device profile.
    Get the list of device using: ba.get_blueprint_device_id
    and based on that, define the right device profiles
    """

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_interface_map_assignments_url}'

    device_id_list = get_blueprint_device_id(blueprint_name)

    interface_maps = {}

    for id in device_id_list:
        if id != None:
            if id['role'] == 'spine':
                interface_maps[id['id']] = spine_device
            elif id['role'] == 'superspine':
                interface_maps[id['id']] = superspine_device
            elif id['label'] == 'leaf001_001_1':
                interface_maps[id['id']] = borderleaf_device
            elif id['label'] == 'leaf002_001_1':
                interface_maps[id['id']] = borderleaf_device
            elif id['role'] == 'leaf':
                interface_maps[id['id']] = leaf_device

    data = f'''
    {{"assignments":
    {json.dumps(interface_maps)}
    }}
    '''

    response = apstra_put(url=url, data=data)
    return response


"""
Now we are build the logic to associate the right physical devices
3 steps:
1- get all blueprint information using: ba.get_blueprint_all_info
2- get all system devices to config
3- and send the right parameters
"""


def blueprint_physical_device(blueprint_name, serial_number, blueprint_device_id):

    print(f"--------------------Assigning physical device : {serial_number} to blueprint: {blueprint_name}")
    """
    send parameters to define the physical device
    """

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/nodes/{blueprint_device_id}'
    data = f'''
    {{"system_id":"{serial_number}", "deploy_mode":"deploy"}}
    '''

    response = apstra_patch(url=url, data=data)
    return response


def send_physical_device_parameters_dc1(blueprint_name):

    blueprint_response = get_blueprint_all_info(blueprint_name=blueprint_name)
    devices_response = get_system_info()

    for key, value in blueprint_response.json()['nodes'].items():
        device = value.get('role')
        if device != None:
            if 'spine1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.215':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'spine2' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.216':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'jnpr_border_leaf_001_leaf1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.225':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'jnpr_esi_leaf_001_leaf1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.217':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'jnpr_esi_leaf_001_leaf2' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.218':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'jnpr_single_leaf_001_leaf1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.219':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])


def send_physical_device_parameters_dc2(blueprint_name):

    blueprint_response = get_blueprint_all_info(blueprint_name=blueprint_name)
    devices_response = get_system_info()

    for key, value in blueprint_response.json()['nodes'].items():
        device = value.get('role')
        if device != None:
            if 'sspine001_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.224':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'spine001_001_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.220':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'spine002_001_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.221':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'leaf001_001_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.226':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'leaf001_002_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.222':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'leaf002_001_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.227':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])

            elif 'leaf002_002_1' in value['label'] and value.get('system_type') == 'switch':
                for sysDevice in devices_response.json()['items']:
                    if sysDevice['facts']['mgmt_ipaddr'] == '192.168.122.223':
                        response = blueprint_physical_device(blueprint_name, sysDevice['device_key'], value['id'])


"""
Security Zone and Virtual Network
"""


def set_blueprint_sz(blueprint_name, zn_name, vni_number: int):

    print(f"--------------------Creating Security Zone : {zn_name} VNI: {vni_number}")

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_security_zone_url}'

    data = f'''
    {{
    "vni_id": {vni_number},
    "sz_type": "evpn",
    "label": "{zn_name}",
    "vrf_name": "{zn_name}"
    }}
    '''
    response = apstra_post(url=url, data=data)
    return response


def get_blueprint_sz(blueprint_name):

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_security_zone_url}'
    response = apstra_get(url=url)
    return response


def set_blueprint_sz_loopback(blueprint_name, zn_name, ip_pool):

    print(f"--------------------Setting Security Zone : {zn_name} loopback pool: {ip_pool}")

    zn_response = get_blueprint_sz(blueprint_name)
    zn_response_json = zn_response.json()

    for key, value in zn_response_json['items'].items():
        if value['vrf_name'] == zn_name:
            sz_id = value['id']

    data = f'''
        {{"pool_ids":["{ip_pool}"]}}
    '''

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprints_resouce_group_url}/ip/sz%3A{sz_id}%2Cleaf_loopback_ips'

    response = apstra_put(url=url, data=data)
    return response


def set_blueprint_vn(blueprint_name, vn_name, sz_name, ipv4_network, ipv4_gw, vlan_id, vni_id):

    print(f"--------------------Setting virtual network : {vn_name} to security zone: {sz_name} "
          f"with vlan id: {vlan_id} vxlan id: {vni_id} network: {ipv4_network} gateway: {ipv4_gw}")

    response = get_blueprint_device_id(blueprint_name)
    devices_list = []
    for device in response:
        if device['role'] == 'leaf':
            devices_list.append(f'{{"system_id": "{device["id"]}", "vlan_id": {vlan_id} }}')

    list_json = ','.join(set(devices_list))

    responses = get_blueprint_sz(blueprint_name)
    sz_response_json = responses.json()
    for key, value in sz_response_json['items'].items():
        if value['vrf_name'] == sz_name:
            sz_id = value['id']

    ipv4_enable = 'true'
    ipv4_gw = '"' + ipv4_gw + '"'
    ipv4_network = '"' + ipv4_network + '"'
    virtual_gateway_ipv4_enabled = 'true'

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_virtual_networks_url}'
    data = f'''
    {{
    "virtual_networks": [
    {{
    "vn_type": "vxlan",
    "virtual_gateway_ipv4": {ipv4_gw},
    "bound_to": [
    {list_json}
    ],
    "ipv4_subnet": {ipv4_network},
    "label": "{vn_name}",
    "ipv4_enabled": {ipv4_enable},
    "virtual_gateway_ipv4_enabled": {virtual_gateway_ipv4_enabled},
    "security_zone_id": "{sz_id}",
    "vn_id": "{vni_id}"
    }}
    ]
    }}
    '''
    response = apstra_post(url=url, data=data)
    return response


"""
set the leaf server interface
"""


def set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_1, sl_2):

    """
    set interface port to virtual network
    """

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/virtual-networks/{vn_id}/endpoints'

    if sl_2 != None:
        data = f'''
        {{
        "endpoints": [
        {{
        "interface_id": "{sl_1}",
        "tag_type": "untagged"
        }},
        {{
        "interface_id": "{sl_2}",
        "tag_type": "untagged"
        }}
        ]
        }}
        '''
    else:
        data = f'''
        {{
        "endpoints": [
        {{
        "interface_id": "{sl_1}",
        "tag_type": "untagged"
        }}
        ]
        }}
        '''
    response = apstra_put(data=data, url=url)


def set_deploy_blueprint(blueprint_name, description):

    print(f"--------------------Deploying blueprint: {blueprint_name}")

    get_version = get_deploy_version(blueprint_name)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.deploy_blueprint_url}?async=full'
    data = f'''
    {{
    "version": {get_version},
    "description": "{description}"
    }}
    '''
    response = apstra_put(url=url, data=data)


"""
configure remote gateway DC1 and DC2
"""


def set_remote_gateway(blueprint_name, gw_asn, gw_name, gw_ip, vqfx_name):

    print(f"--------------------Configuring remote gateway: {gw_name} - blueprint: {blueprint_name}")

    gw_list = get_external_router_id(blueprint_name, vqfx_name)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.blueprint_remote_gateway_url}'

    data = f'''{{
    "gw_asn": {gw_asn},
    "gw_ip": "{gw_ip}",
    "gw_name": "{gw_name}",
    "local_gw_nodes": [
    {gw_list}
    ],
    "ttl": 50
    }}
    '''

    response = apstra_post(url=url, data=data)


def set_external_router_interface_mtu(blueprint_name, mtu_number, type5_routes):

    print(f"--------------------Configuring external interface MTU: {mtu_number} - blueprint: {blueprint_name}")

    get_vn_policy_id = get_virtual_network_policy_id(blueprint_name)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/nodes/{get_vn_policy_id}'

    data = f'''
    {{
    "evpn_generate_type5_host_routes": "{type5_routes}",
    "external_router_mtu": {mtu_number},
    "max_evpn_routes": 0,
    "max_external_routes": 0,
    "max_fabric_routes": 0,
    "max_mlag_routes": 0,
    "overlay_control_protocol": "evpn"
    }}
    '''

    response = apstra_patch(url=url, data=data)