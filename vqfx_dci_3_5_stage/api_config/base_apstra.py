"""
---------------------------------
 Author: Gilberto Rampini
 Date: 05/2021
---------------------------------
"""
import requests
import json

requests.packages.urllib3.disable_warnings()

# Basic information
apstra_url = 'https://192.168.122.180:443'
apstra_port = '8001'
username = 'admin'
password = 'admin'

# APIs URLs
login_url = '/api/user/login'

# Resources
asn_pool_url = '/api/resources/asn-pools'
ip_pool_url = '/api/resources/ip-pools'
vni_pool_url = '/api/resources/vni-pools'
external_router = '/api/resources/external-routers'

# Onboading
system_gent_url = '/api/system-agents'
systems_url = '/api/systems/'
systems_batch_update = '/api/systems-batch-update/'

# Design
rack_design_url = '/api/design/rack-types'
template_design_url = '/api/design/templates'
logical_device_design_url = '/api/design/logical-devices'
interface_maps_url = '/api/design/interface-maps'

# Blueprint
blueprints_url = '/api/blueprints'

blueprints_resource_group_asn_superspine_url = '/resource_groups/asn/superspine_asns'
blueprints_resouce_group_asn_spine_url = '/resource_groups/asn/spine_asns'
blueprints_resouce_group_asn_leaf_url = '/resource_groups/asn/leaf_asns'
blueprints_resouce_group_url = '/resource_groups'
blueprints_resouce_group_loopback_superspine_url = '/resource_groups/ip/superspine_loopback_ips'
blueprints_resouce_group_loopback_spine_url = '/resource_groups/ip/spine_loopback_ips'
blueprints_resouce_group_loopback_leaf_url = '/resource_groups/ip/leaf_loopback_ips'
blueprints_resouce_group_spine_superspine_link_url = '/resource_groups/ip/spine_superspine_link_ips'
blueprints_resouce_group_spine_leaf_link_url = '/resource_groups/ip/spine_leaf_link_ips'
blueprints_resouce_group_external_ip_url = '/resource_groups/ip/to_external_router_link_ips'
blueprints_resouce_group_vni_url = '/resource_groups/vni/evpn_l3_vnis'

blueprint_device_id_url = '/cabling-map'

blueprint_interface_map_assignments_url = '/interface-map-assignments'

blueprint_external_router_import_url = '/external-routers'
blueprint_external_router_links_url = '/external-router-links'

blueprint_security_zone_url = '/security-zones'
blueprint_virtual_networks_url = '/virtual-networks-batch'

# get virtual networks
get_blueprint_virtual_networks = '/experience/web/virtual-networks'

get_blueprint_server_links = '/experience/web/meta/leaf-server-links'

# remote gateway
blueprint_remote_gateway_url = '/remote_gateways'

# commit blueprint
blueprint_version_url = '/diff-status'
deploy_blueprint_url = '/deploy'
