"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""

from apstra_gets import *
import urls_base_apstra as url_ba
import requests
import json
from time import sleep

requests.packages.urllib3.disable_warnings()


def set_external_router_ct(blueprint_name, id_number, ct_name, peer_ip, peer_asn):

    print(f"--------------------Creating BGP Peering IP EndPoint CT: {ct_name} - blueprint: {blueprint_name}")
    """
    configure external router based on
    Link
    bgp peering (ip endpoint)
    bgp policy
    
    we need to pass the 
    blueprint_name
    id_number -> necessary to tie the ids for subpolicies
    """

    sz_defaul_id = get_security_zone(blueprint_name)
    rt_defaul_id = get_route_policy(blueprint_name)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.obj_policy_import_url}'

    data = f'''
    {{
    "policies": [
        {{
            "attributes": {{
                "subpolicies": [
                    "{id_number}-2"
                ]
            }},
            "description": "",
            "id": "{ct_name}-external-router-ct-{blueprint_name}",
            "label": "{ct_name}",
            "policy_type_name": "batch",
            "tags": [],
            "user_data": "{{\\"isSausage\\":true,\\"positions\\":{{\\"{id_number}-1\\":[290,80,1],\\"{id_number}-4\\":[290,150,2],\\"{id_number}-7\\":[290,220,3]}}}}",
            "visible": true
        }},
        {{
            "attributes": {{
                "ipv4_addressing_type": "numbered",
                "ipv6_addressing_type": "none",
                "security_zone": "{sz_defaul_id}",
                "untagged": true,
                "vlan_id": null
            }},
            "description": "Build an IP link between a fabric node and a generic system. This primitive uses AOS resource pool \\"Link IPs - To Generic\\" by default to dynamically allocate an IP endpoint (/31) on each side of the link. To allocate different IP endpoints, navigate under Routing Zone>Subinterfaces Table.",
            "id": "{id_number}-1",
            "label": "IP Link",
            "policy_type_name": "AttachLogicalLink",
            "visible": false
        }},
        {{
            "attributes": {{
                "first_subpolicy": "{id_number}-1",
                "second_subpolicy": "{id_number}-3"
            }},
            "description": "Build an IP link between a fabric node and a generic system. This primitive uses AOS resource pool \\"Link IPs - To Generic\\" by default to dynamically allocate an IP endpoint (/31) on each side of the link. To allocate different IP endpoints, navigate under Routing Zone>Subinterfaces Table.",
            "id": "{id_number}-2",
            "label": "IP Link (pipeline)",
            "policy_type_name": "pipeline",
            "visible": false
        }},
        {{
            "attributes": {{
                "subpolicies": [
                    "{id_number}-5"
                ]
            }},
            "description": "Build an IP link between a fabric node and a generic system. This primitive uses AOS resource pool \\"Link IPs - To Generic\\" by default to dynamically allocate an IP endpoint (/31) on each side of the link. To allocate different IP endpoints, navigate under Routing Zone>Subinterfaces Table.",
            "id": "{id_number}-3",
            "label": "IP Link (batch)",
            "policy_type_name": "batch",
            "visible": false
        }},
        {{
            "attributes": {{
                "asn": {peer_asn},
                "bfd": false,
                "holdtime_timer": null,
                "ipv4_addr": "{peer_ip}",
                "ipv4_safi": true,
                "ipv6_addr": null,
                "ipv6_safi": false,
                "keepalive_timer": null,
                "neighbor_asn_type": "static",
                "password": null,
                "ttl": 2
            }},
            "description": "Create a BGP peering session with a user-specified BGP neighbor addressed peer.",
            "id": "{id_number}-4",
            "label": "BGP Peering (IP Endpoint)",
            "policy_type_name": "AttachIpEndpointWithBgpNsxt",
            "visible": false
        }},
        {{
            "attributes": {{
                "first_subpolicy": "{id_number}-4",
                "second_subpolicy": "{id_number}-6"
            }},
            "description": "Create a BGP peering session with a user-specified BGP neighbor addressed peer.",
            "id": "{id_number}-5",
            "label": "BGP Peering (IP Endpoint) (pipeline)",
            "policy_type_name": "pipeline",
            "visible": false
        }},
        {{
            "attributes": {{
                "subpolicies": [
                    "{id_number}-8"
                ]
            }},
            "description": "Create a BGP peering session with a user-specified BGP neighbor addressed peer.",
            "id": "{id_number}-6",
            "label": "BGP Peering (IP Endpoint) (batch)",
            "policy_type_name": "batch",
            "visible": false
        }},
        {{
            "attributes": {{
                "rp_to_attach": "{rt_defaul_id}"
            }},
            "description": "Allocate routing policy to specific BGP sessions.",
            "id": "{id_number}-7",
            "label": "Routing Policy",
            "policy_type_name": "AttachExistingRoutingPolicy",
            "visible": false
        }},
        {{
            "attributes": {{
                "first_subpolicy": "{id_number}-7",
                "second_subpolicy": "{id_number}-9"
            }},
            "description": "Allocate routing policy to specific BGP sessions.",
            "id": "{id_number}-8",
            "label": "Routing Policy (pipeline)",
            "policy_type_name": "pipeline",
            "visible": false
        }},
        {{
            "attributes": {{}},
            "description": "",
            "id": "{id_number}-9",
            "label": "noop",
            "policy_type_name": "noop",
            "visible": false
        }}
    ]
    }}
    '''
    response = apstra_put(url=url, data=data)


def set_virtual_network_ct(blueprint_name, id_number, ct_name, vn_name):

    print(f"--------------------Creating Virtual Network CT: {ct_name} - blueprint: {blueprint_name}")
    """
    configure external router based on
    Link
    bgp peering (ip endpoint)
    bgp policy

    we need to pass the
    blueprint_name
    id_number -> necessary to tie the ids for subpolicies
    """

    vn_id = get_virtual_network(blueprint_name, vn_name)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}{url_ba.obj_policy_import_url}'

    data = f'''
        {{
        "policies": [
            {{
                "attributes": {{
                    "subpolicies": [
                        "{id_number}-1"
                    ]
                }},
                "description": "",
                "id": "{ct_name}-virtual-network-ct-{blueprint_name}",
                "label": "{ct_name}",
                "policy_type_name": "batch",
                "tags": [],
                "user_data": "{{\\"isSausage\\":true,\\"positions\\":{{\\"vn-id-2\\":[290,80,1]}}}}",
                "visible": true
            }},
            {{
                "attributes": {{
                    "tag_type": "untagged",
                    "vn_node_id": "{vn_id}"
                }},
                "description": "Add a single VLAN to interfaces, as tagged or untagged.",
                "id": "{id_number}-2",
                "label": "Virtual Network (Single)",
                "policy_type_name": "AttachSingleVLAN",
                "visible": false
            }},
            {{
                "attributes": {{
                    "first_subpolicy": "{id_number}-2",
                    "second_subpolicy": "{id_number}-3"
                }},
                "description": "Add a single VLAN to interfaces, as tagged or untagged.",
                "id": "{id_number}-1",
                "label": "Virtual Network (Single) (pipeline)",
                "policy_type_name": "pipeline",
                "visible": false
            }},
            {{
                "attributes": {{}},
                "description": "",
                "id": "{id_number}-3",
                "label": "noop",
                "policy_type_name": "noop",
                "visible": false
            }}
        ]
        }}
        '''
    response = apstra_put(url=url, data=data)


def set_blueprint_server_link(blueprint_name, ct_name, vqfx_name, interface):

    print(f"--------------------Assigning: {ct_name} to: {vqfx_name}, interface: {interface} - blueprint: {blueprint_name}")
    """
        configure external router based on
        Link
        bgp peering (ip endpoint)
        bgp policy

        we need to pass the
        blueprint_name
        id_number -> necessary to tie the ids for subpolicies
    """

    policy_id = get_ct_policies_id(blueprint_name, ct_name)
    interface_id = get_application_points_id(blueprint_name, vqfx_name, interface)

    url = f'{url_ba.apstra_url}{url_ba.blueprints_url}/{blueprint_name}/obj-policy-batch-apply'

    data = f'''
    {{
      "application_points": [
        {{
          "id": "{interface_id}",
          "policies": [
            {{
              "policy": "{policy_id}",
              "used": true
            }}
          ]
        }}
      ]
    }}
    '''
    response = apstra_patch(data=data, url=url)


