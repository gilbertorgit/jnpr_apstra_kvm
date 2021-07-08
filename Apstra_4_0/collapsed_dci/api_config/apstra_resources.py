"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import requests
import base_apstra as ba
import urls_base_apstra as url_ba

requests.packages.urllib3.disable_warnings()


"""
--------------------------------------------------------------------------------------------------------
Basic Apstra configuration, resources, etc.
"""


def create_asn_pool(asn_name, asn_first, asn_last):

        print(f'--------------------Creating ASN pool: {asn_name} range: {asn_first}-{asn_last}')
        url = f'{url_ba.apstra_url}{url_ba.asn_pool_url}'
        data = f''' 
        {{ "display_name": "{asn_name}",
        "id": "{asn_name}",
        "ranges": [
        {{
        "first": "{asn_first}",
        "last": "{asn_last}"
        }}
        ]
        }}'''

        response = ba.apstra_post(url=url, data=data)
        return response


def create_vni_pool(vni_name, vni_first, vni_last):

    print(f'--------------------Creating VNI pool: {vni_name} range: {vni_first}-{vni_last}')

    url = f'{url_ba.apstra_url}{url_ba.vni_pool_url}'

    data = f'''{{ "display_name": "{vni_name}",
    "ranges": [
    {{
    "first": "{vni_first}",
    "last": "{vni_last}"
    }}
    ],
    "id": "{vni_name}"
    }}'''

    response = ba.apstra_post(url=url, data=data)
    return response


def create_ip_pool(ip_name, ip_network):

    print(f'--------------------Creating IP pool: {ip_name} network: {ip_network}')

    url = f'{url_ba.apstra_url}{url_ba.ip_pool_url}'

    data = f'''{{
    "subnets": [ {{"network": "{ip_network}"}} ],
    "display_name": "{ip_name}",
    "id": "{ip_name}"
    }}'''

    response = ba.apstra_post(url=url, data=data)
    return response