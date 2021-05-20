import requests
import json
from time import sleep
import base_apstra as ba
import templates_data as td
import rack_data as rd
import logical_data as ld
import int_map_data as imd
from ipaddress import ip_address

requests.packages.urllib3.disable_warnings()


def get_token():

    data = {'username': ba.username, 'password': ba.password}
    auth_resp = requests.post(f'{ba.apstra_url}{ba.login_url}', data=json.dumps(data), verify=False)

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


def create_ip_list(start, end):
    start_int = int(ip_address(start).packed.hex(), 16)
    end_int = int(ip_address(end).packed.hex(), 16)
    return [ip_address(ip).exploded for ip in range(start_int, end_int)]


def get_asn_pool():

    headers = {'Content-Type':'application/json', 'Cache-Control':'no-cache', 'AUTHTOKEN': get_token()}
    asn_pool_resp = requests.get(f'{ba.apstra_url}{ba.asn_pool_url}', headers=headers, verify=False)


def create_asn_pool(asn_name, asn_first, asn_last):

        print(f'--------------------Creating ASN pool: {asn_name} range: {asn_first}-{asn_last}')
        url = f'{ba.apstra_url}{ba.asn_pool_url}'
        data = f''' {{ "display_name": "{asn_name}",
                        "id": "{asn_name}",
                        "ranges": [
                            {{
                            "first": "{asn_first}",
                            "last": "{asn_last}"
                            }}
                        ]
                    }}'''

        response = apstra_post(url=url, data=data)
        return response


def create_vni_pool(vni_name, vni_first, vni_last):

    print(f'--------------------Creating VNI pool: {vni_name} range: {vni_first}-{vni_last}')

    url = f'{ba.apstra_url}{ba.vni_pool_url}'

    data = f''' {{ "display_name": "{vni_name}",
                            "ranges": [
                                {{
                                "first": "{vni_first}",
                                "last": "{vni_last}"
                                }}
                            ],
                            "id": "{vni_name}"
                        }}'''

    response = apstra_post(url=url, data=data)
    return response


def create_ip_pool(ip_name, ip_network):

    print(f'--------------------Creating IP pool: {ip_name} network: {ip_network}')

    url = f'{ba.apstra_url}{ba.ip_pool_url}'

    data = f''' {{             
                          "subnets": [ {{"network": "{ip_network}"}} ],
                          "display_name": "{ip_name}",
                          "id": "{ip_name}"
                      }}'''

    response = apstra_post(url=url, data=data)
    return response


def create_external_router(router_name, loopback_address, asn):

    print(f'--------------------Creating External Router: {router_name} network: {loopback_address} asn: {asn}')

    url = f'{ba.apstra_url}{ba.external_router}'

    data = f''' {{
                      "display_name": "{router_name}",
                      "asn": "{asn}",
                      "address": "{loopback_address}",
                      "id": "{router_name}"
                    }}'''

    response = apstra_post(url=url, data=data)
    return response


def create_offbox_device(start_ip, end_ip, username=f'lab', password=f'lab123', platform=f'junos',
                         agent_type='offbox', operation_mode='full_control'):

    print(f'--------------------Creating Offbox Devices')
    url = f'{ba.apstra_url}{ba.system_gent_url}'

    mgmt_list = create_ip_list(start_ip,end_ip)
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
        response = apstra_post(url=url, data=data)
        response_list.append(response)
        sleep(2)
    return response_list


def manage_device(system_id, model):

    url = f'{ba.apstra_url}{ba.systems_batch_update}'

    data = f'''{{"{system_id}": 
                    {{"user_config": 
                        {{
                            "aos_hcl_model": "{model}", 
                            "admin_state": "normal"
                        }}
                    }}
                }}'''
    response = apstra_post(url=url, data=data)
    return response


def manage_device_all():

    device_list_url = f'{ba.apstra_url}{ba.systems_url}'
    device_list_response = apstra_get(device_list_url).json()

    device_list_all = []

    for device in device_list_response['items']:

        print(f"--------------------Managing Device: {device['status']['hostname']} IP: {device['facts']['mgmt_ipaddr']}")

        system_id = device['id']
        model = device['facts']['aos_hcl_model']
        response = manage_device(system_id, model)
        device_list_all.append(response)

    return device_list_all


def create_logical_device(data):

    print(f'--------------------Creating Logical Devices')

    url = f'{ba.apstra_url}{ba.logical_device_design_url}'
    data = data
    response = apstra_post(url=url, data=data)
    return response


def create_interface_map(data):

    print(f'--------------------Creating Interface Maps')

    url = f'{ba.apstra_url}{ba.interface_maps_url}'
    data = data
    response = apstra_post(url=url, data=data)
    return response


def create_rack_type(data):

    print(f'--------------------Creating Racks')

    url = f'{ba.apstra_url}{ba.rack_design_url}'
    data = data
    response = apstra_post(url=url, data=data)
    return response


def create_template(data):

    print(f'--------------------Creating Templates')

    url = f'{ba.apstra_url}{ba.template_design_url}'
    data = data
    response = apstra_post(url=url, data=data)
    return response


def create_blueprint(blueprint_name, template_name):

    print(f'--------------------Creating blueprint name {blueprint_name} based on template_name: {template_name}')

    url = f'{ba.apstra_url}{ba.blueprints_url}'

    data = f'''
        {{"design":"two_stage_l3clos", 
        "init_type":"template_reference",
        "label":"{blueprint_name}",
        "template_id":"{template_name}", 
        "id":"{blueprint_name}"}}
    '''
    response = apstra_post(url=url, data=data)
    return response

"""
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
agora vou definir todos os recursos (ASN, IP, VNI) blueprint resources
"""


def blueprint_resource_asn_superspine(blueprint_name, asn_pool):

    print(f"--------------------Assigning SuperSpine ASN: {asn_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resource_group_asn_superspine_url}'
    data = f'''
            {{"pool_ids":["{asn_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_asn_spine(blueprint_name, asn_pool):

    print(f"--------------------Assigning Spine ASN: {asn_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_asn_spine_url}'
    data = f'''
            {{"pool_ids":["{asn_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_asn_leaf(blueprint_name, asn_pool):

    print(f"--------------------Assigning Leaf ASN: {asn_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_asn_leaf_url}'
    data = f'''
            {{"pool_ids":["{asn_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_superspine(blueprint_name, loopback_pool):

    print(f"--------------------Assigning SuperSpine loopback: {loopback_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_loopback_superspine_url}'
    data = f'''
            {{"pool_ids":["{loopback_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_spine(blueprint_name, loopback_pool):

    print(f"--------------------Assigning spine loopback: {loopback_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_loopback_spine_url}'
    data = f'''
            {{"pool_ids":["{loopback_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_loopback_leaf(blueprint_name, loopback_pool):

    print(f"--------------------Assigning leaf loopback: {loopback_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_loopback_leaf_url}'
    data = f'''
            {{"pool_ids":["{loopback_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_fabric_spine_superspine(blueprint_name, fabric_pool):

    print(f"--------------------Assigning Spine-SuperSpine fabric IP: {fabric_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_spine_superspine_link_url}'
    data = f'''
            {{"pool_ids":["{fabric_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_fabric_spine_leaf(blueprint_name, fabric_pool):

    print(f"--------------------Assigning Spine-Leaf fabric IP: {fabric_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_spine_leaf_link_url}'
    data = f'''
            {{"pool_ids":["{fabric_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def blueprint_resource_external_router_ip(blueprint_name, ip_pool):

    print(f"--------------------Assigning external router IP: {ip_pool} to blueprint: {blueprint_name}")
    """
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_external_ip_url}'
    data = f'''
            {{"pool_ids":["{ip_pool}"]}}
        '''
    response = apstra_put(url=url, data=data)
    return response


def get_blueprint_device_id(blueprint_name):

    """
    pega os default device ID dentro do blueprint (necessario para configurar os profiles corretos do
    device profile
    """
    url = f"{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}/experience/web/cabling-map"
    id_list=[]
    response = apstra_get(url=url)

    for id in response.json()['links']:
        id=id['endpoints']
        for value in id:
            id_list.append(value['system'])
    return id_list


def blueprint_device_profile_3_stage(blueprint_name, spine_device, leaf_device, borderleaf_device):

    print(f"--------------------Assigning 3-stage Device profile: {spine_device}, {leaf_device}, {borderleaf_device} to blueprint: {blueprint_name}")

    """
    define device profile no 3 stage clos
    pega a lista de devices usando a função get_blueprint_device_id
    e baseado nas roles define o profile correto
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_interface_map_assignments_url}'

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

    """
        define device profile no 3 stage clos
        pega a lista de devices usando a função get_blueprint_device_id
        e baseado nas roles define o profile correto
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_interface_map_assignments_url}'

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
Agora vou montar a lógica para associar os physical devices
serão 3
uma para pegar toda a informação do blue print get_blueprint_all_info
outro para pegar todos os system devices
outra para configurar 
e outra que vai enviar os parametros corretos
"""


def get_blueprint_all_info(blueprint_name):

    """
    pega todas as infos do blueprint
    """
    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}'
    response = apstra_get(url=url)
    return response


def get_system_info():
    """
    pega todos os system id
    """
    url = f'{ba.apstra_url}{ba.systems_url}'
    response = apstra_get(url=url)
    return response


def blueprint_physical_device(blueprint_name, serial_number, blueprint_device_id):

    print(f"--------------------Assigning physical device : {serial_number} to blueprint: {blueprint_name}")
    """
    envia os parametros para definir o physical device no blueprint
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}/nodes/{blueprint_device_id}'
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


def blueprint_external_router_import(blueprint_name, external_router_id):

    print(f"--------------------Importing external router : {external_router_id} to blueprint: {blueprint_name}")

    """
        import o external router do external resources para o blueprint
    """
    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_external_router_import_url}'
    data = f'''
    {{
    "router_id": "{external_router_id}"
    }}
    '''
    response = apstra_post(url=url, data=data)
    return response


def create_external_router_link(blueprint_name, router_name):

    print(f"--------------------creating external router link : {router_name} to blueprint: {blueprint_name}")

    """
    get external router id
    """
    external_router_id_url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_external_router_import_url}'

    external_router_response = apstra_get(url=external_router_id_url)
    for external_router in external_router_response.json()['items']:
        if external_router['display_name'] == router_name:
            router_id = external_router['id']

    """
    get external router link id name: return example: jnpr_border_leaf_001_leaf1<->router0001
    """

    router_id_url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_external_router_links_url}'
    response = apstra_get(url=router_id_url)

    router_link_id = []
    for router_link in response.json()['links']:
        router_link_id.append(f'"{router_link}"')

    list_json = ','.join(set(router_link_id))

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_external_router_links_url}/{router_id}'

    """
        now with the router id + router link id we can send the right put. 
    """

    data = f'''
    {{
    "connectivity_type": "l3",
    "links": [
    {list_json}
    ]
    }}
    '''
    response = apstra_put(url=url, data=data)
    #print(data)
    #print(response.json())
    return response


def set_blueprint_sz(blueprint_name, zn_name, vni_number: int):

    print(f"--------------------Creating Security Zone : {zn_name} VNI: {vni_number}")

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_security_zone_url}'

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

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_security_zone_url}'
    response = apstra_get(url=url)
    return response


def set_blueprint_sz_loopback(zn_name, blueprint_name, ip_pool):

    print(f"--------------------Setting Security Zone : {zn_name} loopback pool: {ip_pool}")

    zn_response = get_blueprint_sz(blueprint_name)
    zn_response_json = zn_response.json()
    for key, value in zn_response_json['items'].items():
        if value['vrf_name'] == zn_name:
            sz_id = value['id']

    data = f'''
        {{"pool_ids":["{ip_pool}"]}}
    '''

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprints_resouce_group_url}/ip/sz%3A{sz_id}%2Cleaf_loopback_ips'

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

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_virtual_networks_url}'
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
                        "security_zone_id": "{sz_id}",
                        "vn_id": "{vni_id}"
                    }}
                ]
            }}
        '''
    response = apstra_post(url=url, data=data)
    return response


def get_blueprint_virtual_network(blueprint_name, vlan_name):

    """
    este método pega o virtual network id
    """

    """GET VIRTUAL NETWORK ID 
    """
    virtual_network_url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.get_blueprint_virtual_networks}'
    virtual_network_response = apstra_get(url=virtual_network_url)
    virtual_network_response_json = virtual_network_response.json()
    for key, value in virtual_network_response_json['virtual_networks'].items():
        if value['label'] == vlan_name:
            vn_id = key

    return vn_id


def set_blueprint_server_link(blueprint_name, vlan_name):

    print(f"--------------------Attaching interface to virtual network: {vlan_name}")
    """
    este method chama o get_blueprint_virtual_network para pegar o virtual network id
    este método pega o server link id e chama o method set_blueprint_interface_virtual_network para
    enviar os dados
    """

    vn_id = get_blueprint_virtual_network(blueprint_name, vlan_name)

    server_links_url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}/experience/web/leaf-server-links/{vn_id}'
    server_links_response = apstra_get(server_links_url)
    server_links_response_json = server_links_response.json()

    for link in server_links_response_json['links']:
        if link['label'] == "jnpr_esi_leaf_001_leaf_pair1<->jnpr_esi_leaf_001_server001(server-1-dual-link)":
            for endpoint in link['endpoints']:
                if endpoint['system']['label'] == "jnpr_esi_leaf_001_server001":
                    sl_id_1 = endpoint['interface']['id']

        elif link['label'] == "jnpr_single_leaf_001_leaf1<->jnpr_single_leaf_001_server001(server-1-link-1)[1]":
            for endpoint in link['endpoints']:
                if endpoint['system']['label'] == "jnpr_single_leaf_001_server001":
                    sl_id_2 = endpoint['interface']['id']

        elif link['label'] == "jnpr_single_leaf_001_leaf1<->jnpr_single_leaf_001_server002(server-2-link-1)[1]":
            for endpoint in link['endpoints']:
                if endpoint['system']['label'] == "jnpr_single_leaf_001_server002":
                    sl_id_3 = endpoint['interface']['id']

        elif link['label'] == "jnpr_esi_leaf_001_leaf2<->jnpr_esi_leaf_001_server003(server-3-link-1)[1]":
            for endpoint in link['endpoints']:
                if endpoint['system']['label'] == "jnpr_esi_leaf_001_server003":
                    sl_id_4 = endpoint['interface']['id']

        elif link['label'] == "jnpr_single_leaf_001_leaf1<->jnpr_single_leaf_001_server003(server-3-link-1)[1]":
            for endpoint in link['endpoints']:
                if endpoint['system']['label'] == "jnpr_single_leaf_001_server003":
                    sl_id_5 = endpoint['interface']['id']

    #vlan 10
    if blueprint_name == "DC1":
        if vlan_name == "VLAN10":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_1, sl_id_2)
        #vlan 20
        if vlan_name == "VLAN20":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_3, None)
        #vlan 100
        if vlan_name == "VLAN100":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_4, None)
        #vlan 200
        if vlan_name == "VLAN200":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_5, None)

    if blueprint_name == "DC2":

        for link in server_links_response_json['links']:
            if link['label'] == "leaf001_002_1<->server001_002_001(server-1-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server001_002_001":
                        sl_id_1 = endpoint['interface']['id']

            elif link['label'] == "leaf002_002_1<->server002_002_001(server-1-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server002_002_001":
                        sl_id_2 = endpoint['interface']['id']

            elif link['label'] == "leaf001_002_1<->server001_002_002(server-2-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server001_002_002":
                        sl_id_3 = endpoint['interface']['id']

            elif link['label'] == "leaf002_002_1<->server002_002_002(server-2-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server002_002_002":
                        sl_id_4 = endpoint['interface']['id']

            elif link['label'] == "leaf002_002_1<->server002_002_003(server-3-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server002_002_003":
                        sl_id_5 = endpoint['interface']['id']

            elif link['label'] == "leaf001_002_1<->server001_002_003(server-3-link-1)[1]":
                for endpoint in link['endpoints']:
                    if endpoint['system']['label'] == "server001_002_003":
                        sl_id_6 = endpoint['interface']['id']

        if vlan_name == "VLAN10":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_1, sl_id_2)
        #vlan 20
        if vlan_name == "VLAN20":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_3, sl_id_4)
        #vlan 100
        if vlan_name == "VLAN30":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_5, None)
        #vlan 200
        if vlan_name == "VLAN200":
            set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_id_6, None)


def set_blueprint_interface_virtual_network(blueprint_name, vn_id, sl_1, sl_2):

    """set interface port to virtual network
    """

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}/virtual-networks/{vn_id}/endpoints'

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


def get_deploy_version(blueprint_name):

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_version_url}'
    response = apstra_get(url=url)
    return response.json()['staging_version']


def set_deploy_blueprint(blueprint_name, description):

    print(f"--------------------Deploying blueprint: {blueprint_name}")

    get_version = get_deploy_version(blueprint_name)

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.deploy_blueprint_url}?async=full'
    data = f'''
    {{
    "version": {get_version},
    "description": "{description}"
    }}
    '''
    response = apstra_put(url=url, data=data)


def set_remote_gateway(blueprint_name, gw_asn, gw_name, gw_ip):

    print(f"--------------------Configuring remote gateway: {gw_name} - blueprint: {blueprint_name}")

    external_links_url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_external_router_links_url}'
    external_links_response = apstra_get(external_links_url)

    external_link_id = []
    for key, value in external_links_response.json()['links'].items():
        system_id = value["system_id"]
        external_link_id.append(f'"{system_id}"')

    list_json = ','.join(set(external_link_id))

    url = f'{ba.apstra_url}{ba.blueprints_url}/{blueprint_name}{ba.blueprint_remote_gateway_url}'

    data = f'''{{
    "gw_asn": {gw_asn},
    "gw_ip": "{gw_ip}",
    "gw_name": "{gw_name}",
    "local_gw_nodes": [
    {list_json}
    ],
    "ttl": 50
    }}
    '''
    response = apstra_post(url=url, data=data)


if __name__ == '__main__':

    print("################################################### Creating Common resources")
    create_asn_pool("DC1-ASN-POOL", 100, 199)
    create_asn_pool("DC2-ASN-POOL", 200, 299)
    create_vni_pool("LAB-VNI-POOL", 5000, 7000)
    create_ip_pool("DC1-EXTERNAL-ROUTER", "10.1.1.0/24")
    create_ip_pool("DC1-LEAF-LOOPBACK", "10.20.30.0/24")
    create_ip_pool("DC1-SPINE-LEAF", "10.10.0.0/22")
    create_ip_pool("DC1-SPINE-LOOPBACK", "10.20.31.0/24")
    create_ip_pool("DC1-VIRTUAL-LEAF-LOOPBACK", "10.100.100.0/24")
    create_ip_pool("DC2-EXTERNAL-ROUTER", "20.2.2.0/24")
    create_ip_pool("DC2-LEAF-LOOPBACK", "20.20.30.0/24")
    create_ip_pool("DC2-SPINE-LEAF", "20.10.0.0/22")
    create_ip_pool("DC2-SPINE-LOOPBACK", "20.20.31.0/24")
    create_ip_pool("DC2-SPINE-SUPERSPINE", "20.11.0.0/22")
    create_ip_pool("DC2-SUPERSPINE-LOOPBACK", "20.20.33.0/24")
    create_ip_pool("DC2-VIRTUAL-LEAF-LOOPBACK", "20.100.100.0/24")
    sleep(2)
    create_external_router("DC1-R1", "100.100.11.1", 65002)
    create_external_router("DC2-R2", "100.100.12.1", 65002)
    sleep(2)
    create_offbox_device('192.168.122.215', '192.168.122.228')
    sleep(60)
    manage_device_all()
    sleep(5)
    create_logical_device(ld.data_JNPR_7_10_Spine)
    create_logical_device(ld.data_JNPR_7_10_SuperSpine)
    create_logical_device(ld.data_JNPR_8_10_BorderLeaf)
    create_logical_device(ld.data_JNPR_10_10_Leaf)
    sleep(5)
    create_interface_map(imd.data_JNPR_vQFX_7_10_Spine)
    create_interface_map(imd.data_JNPR_vQFX_7_10_SuperSpine)
    create_interface_map(imd.data_JNPR_vQFX_8_10_BorderLeaf)
    create_interface_map(imd.data_JNPR_vQFX_10_10_Leaf)
    sleep(2)
    create_rack_type(rd.data_rack_JNPR_SINGLE_LEAF)
    create_rack_type(rd.data_rack_JNPR_ESI_LEAF)
    create_rack_type(rd.data_rack_JNPR_BORDER_LEAF)
    sleep(2)
    create_template(td.data_JNPR_3_STAGE_TEMPLATE)
    create_template(td.data_JNPR_5_STAGE_BASE)
    create_template(td.data_JNPR_5_STAGE_TEMPLATE)
    sleep(2)

    create_blueprint("DC1", "JNPR-3-STAGE-TEMPLATE")
    create_blueprint("DC2", "JNPR-5-STAGE-TEMPLATE")
    sleep(10)

    
    #--------------------- DC1
    print("################################################### DC1 Configuration")
    blueprint_resource_asn_spine("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_asn_leaf("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_loopback_spine("DC1","DC1-SPINE-LOOPBACK")
    sleep(1)
    blueprint_resource_loopback_leaf("DC1","DC1-LEAF-LOOPBACK")
    sleep(1)
    blueprint_resource_fabric_spine_leaf("DC1", "DC1-SPINE-LEAF")
    sleep(1)
    blueprint_resource_external_router_ip("DC1", "DC1-EXTERNAL-ROUTER")
    sleep(1)
    
    blueprint_device_profile_3_stage("DC1", "JNPR_vQFX-7x10-Spine", "JNPR_vQFX_10x10-Leaf", "JNPR_vQFX_8x10-BorderLeaf")
    sleep(2)
    
    send_physical_device_parameters_dc1("DC1")
    sleep(2)

    blueprint_external_router_import("DC1", "DC1-R1")
    sleep(5)
    create_external_router_link("DC1", "DC1-R1")
    
    set_blueprint_sz("DC1", "customer-1", 10010)
    set_blueprint_sz("DC1", "customer-2", 10020)
    
    set_blueprint_sz_loopback("customer-1", "DC1", "DC1-VIRTUAL-LEAF-LOOPBACK")
    set_blueprint_sz_loopback("customer-2", "DC1", "DC1-VIRTUAL-LEAF-LOOPBACK")

    set_blueprint_vn("DC1", "VLAN10", "customer-1", "192.168.10.0/24", "192.168.10.1", 10, 5010)
    set_blueprint_vn("DC1", "VLAN20", "customer-1", "192.168.20.0/24", "192.168.20.1", 20, 5020)
    set_blueprint_vn("DC1", "VLAN100", "customer-2", "192.168.100.0/24", "192.168.100.1", 100, 5100)
    set_blueprint_vn("DC1", "VLAN200", "customer-2", "192.168.200.0/24", "192.168.200.1", 200, 5200)
    sleep(5)

    set_blueprint_server_link("DC1", "VLAN10")
    sleep(1)
    set_blueprint_server_link("DC1", "VLAN20")
    sleep(1)
    set_blueprint_server_link("DC1", "VLAN100")
    sleep(1)
    set_blueprint_server_link("DC1", "VLAN200")
    sleep(10)
    
    set_deploy_blueprint("DC1", "DC1 full config")

    #--------------------- DC2

    print("################################################### DC2 Configuration")
    blueprint_resource_asn_superspine("DC2", "DC2-ASN-POOL")
    sleep(1)
    blueprint_resource_asn_spine("DC2", "DC2-ASN-POOL")
    sleep(1)
    blueprint_resource_asn_leaf("DC2", "DC2-ASN-POOL")
    sleep(1)
    blueprint_resource_loopback_superspine("DC2", "DC2-SUPERSPINE-LOOPBACK")
    sleep(1)
    blueprint_resource_loopback_spine("DC2", "DC2-SPINE-LOOPBACK")
    sleep(1)
    blueprint_resource_loopback_leaf("DC2", "DC2-LEAF-LOOPBACK")
    sleep(1)
    blueprint_resource_fabric_spine_superspine("DC2", "DC2-SPINE-SUPERSPINE")
    sleep(1)
    blueprint_resource_fabric_spine_leaf("DC2", "DC2-SPINE-LEAF")
    sleep(1)
    blueprint_resource_external_router_ip("DC2", "DC2-EXTERNAL-ROUTER")
    sleep(1)
    blueprint_device_profile_5_stage("DC2", "JNPR_vQFX-7x10-SuperSpine", "JNPR_vQFX-7x10-Spine", "JNPR_vQFX_10x10-Leaf", "JNPR_vQFX_8x10-BorderLeaf")
    sleep(2)
    send_physical_device_parameters_dc2("DC2")
    sleep(2)

    blueprint_external_router_import("DC2", "DC2-R2")
    sleep(5)
    create_external_router_link("DC2", "DC2-R2")

    set_blueprint_sz("DC2", "customer-1", 10010)
    set_blueprint_sz("DC2", "customer-2", 10020)
    sleep(5)
    set_blueprint_sz_loopback("customer-1", "DC2", "DC2-VIRTUAL-LEAF-LOOPBACK")
    set_blueprint_sz_loopback("customer-2", "DC2", "DC2-VIRTUAL-LEAF-LOOPBACK")

    set_blueprint_vn("DC2", "VLAN10", "customer-1", "192.168.10.0/24", "192.168.10.1", 10, 5010)
    set_blueprint_vn("DC2", "VLAN20", "customer-1", "192.168.20.0/24", "192.168.20.1", 20, 5020)
    set_blueprint_vn("DC2", "VLAN30", "customer-1", "192.168.30.0/24", "192.168.30.1", 100, 5030)
    set_blueprint_vn("DC2", "VLAN200", "customer-2", "192.168.200.0/24", "192.168.200.1", 200, 5200)
    sleep(5)

    set_blueprint_server_link("DC2", "VLAN10")
    sleep(1)
    set_blueprint_server_link("DC2", "VLAN20")
    sleep(1)
    set_blueprint_server_link("DC2", "VLAN30")
    sleep(1)
    set_blueprint_server_link("DC2", "VLAN200")
    sleep(10)
    set_deploy_blueprint("DC2", "DC2 full config")
    sleep(5)

    print("################################################### Remote Gateways Configuration")
    set_remote_gateway("DC1", 203, "DC2-BL1", "20.20.30.0")
    set_remote_gateway("DC1", 205, "DC2-BL2", "20.20.30.2")
    sleep(5)
    set_deploy_blueprint("DC1", "DC1 to DC2 External GW")
    sleep(5)
    set_remote_gateway("DC2", 102, "DC1-BL1", "10.20.30.0")
    sleep(5)
    set_deploy_blueprint("DC2", "DC2 to DC1 External GW")