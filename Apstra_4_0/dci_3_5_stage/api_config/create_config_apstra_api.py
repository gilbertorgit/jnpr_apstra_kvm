"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import requests
import json
import ct_config_base as ct
from time import sleep

requests.packages.urllib3.disable_warnings()


from apstra_gets import *
from apstra_resources import *
from apstra_devices import *
from apstra_design import *
from blueprint_staged import *
from logical_data import create_logical_devices_dic
from int_map_data import create_interface_map_dic
from rack_data import create_rack_type_dic
from templates_data import create_templates_dic

"""
Resources Dictionaries
"""
asn_dic = {'DC1-ASN-POOL': {'asn_name': 'DC1-ASN-POOL', 'asn_start': '100', 'asn_stop': '199'},
           'DC2-ASN-POOL': {'asn_name': 'DC2-ASN-POOL', 'asn_start': '200', 'asn_stop': '299'}, }

vni_dic = {'LAB-VNI-POOL': {'vni_name': 'LAB-VNI-POOL', 'vni_start': '5000', 'vni_stop': '7000'}, }

ip_pool_dic = {'DC1-EXTERNAL-ROUTER': {'ip_name': 'DC1-EXTERNAL-ROUTER', 'network': '10.1.1.0/24'},
               'DC1-LEAF-LOOPBACK': {'ip_name': 'DC1-LEAF-LOOPBACK', 'network': '10.20.30.0/24'},
               'DC1-SPINE-LEAF': {'ip_name': 'DC1-SPINE-LEAF', 'network': '10.10.0.0/22'},
               'DC1-SPINE-LOOPBACK': {'ip_name': 'DC1-SPINE-LOOPBACK', 'network': '10.20.31.0/24'},
               'DC1-VIRTUAL-LEAF-LOOPBACK': {'ip_name': 'DC1-VIRTUAL-LEAF-LOOPBACK', 'network': '10.100.100.0/24'},
               'DC2-EXTERNAL-ROUTER': {'ip_name': 'DC2-EXTERNAL-ROUTER', 'network': '20.2.2.0/24'},
               'DC2-LEAF-LOOPBACK': {'ip_name': 'DC2-LEAF-LOOPBACK', 'network': '20.20.30.0/24'},
               'DC2-SPINE-LEAF': {'ip_name': 'DC2-SPINE-LEAF', 'network': '20.10.0.0/22'},
               'DC2-SPINE-LOOPBACK': {'ip_name': 'DC2-SPINE-LOOPBACK', 'network': '20.20.31.0/24'},
               'DC2-SPINE-SUPERSPINE': {'ip_name': 'DC2-SPINE-SUPERSPINE', 'network': '20.11.0.0/22'},
               'DC2-SUPERSPINE-LOOPBACK': {'ip_name': 'DC2-SUPERSPINE-LOOPBACK', 'network': '20.20.33.0/24'},
               'DC2-VIRTUAL-LEAF-LOOPBACK': {'ip_name': 'DC2-VIRTUAL-LEAF-LOOPBACK', 'network': '20.100.100.0/24'}, }

"""
Create Blueprint Dictionaries
"""

blueprint_dic = {'DC1': {'bl_name': 'DC1', 'template_name': 'JNPR-3-STAGE-TEMPLATE'},
                 'DC2': {'bl_name': 'DC2', 'template_name': 'JNPR-5-STAGE-TEMPLATE'}, }


"""
DC1 Blueprint Routing Zones Dictionaries
"""

dc1_routing_zones_dic = {'customer-1': {'bl_name': 'DC1', 'rz_name': 'customer-1', 'vni_id': 10010},
                         'customer-2': {'bl_name': 'DC1', 'rz_name': 'customer-2', 'vni_id': 10020}, }


dc1_routing_zones_loopback_dic = {'customer-1': {'bl_name': 'DC1', 'rz_name': 'customer-1',
                                                 'lb_ip': 'DC1-VIRTUAL-LEAF-LOOPBACK'},
                                  'customer-2': {'bl_name': 'DC1', 'rz_name': 'customer-2',
                                                 'lb_ip': 'DC1-VIRTUAL-LEAF-LOOPBACK'}, }


dc1_virtual_network_dic = {'VLAN10': {'bl_name': 'DC1', 'vn_name': 'VLAN10', 'rz_name': 'customer-1',
                                      'network': '192.168.10.0/24', 'gw': '192.168.10.1', 'vlan_id': 10, 'vni_id': 5010},
                           'VLAN20': {'bl_name': 'DC1', 'vn_name': 'VLAN20', 'rz_name': 'customer-1',
                                      'network': '192.168.20.0/24', 'gw': '192.168.20.1', 'vlan_id': 20, 'vni_id': 5020},
                           'VLAN100': {'bl_name': 'DC1', 'vn_name': 'VLAN100', 'rz_name': 'customer-2',
                                       'network': '192.168.100.0/24', 'gw': '192.168.100.1', 'vlan_id': 100, 'vni_id': 5100},
                           'VLAN200': {'bl_name': 'DC1', 'vn_name': 'VLAN200', 'rz_name': 'customer-2',
                                       'network': '192.168.200.0/24', 'gw': '192.168.200.1', 'vlan_id': 200, 'vni_id': 5200}, }

dc1_ct_virtual_network_dic = {'CT-VLAN10': {'bl_name': 'DC1', 'policy_id': 'vlan10-ct-policy-id',
                                            'ct_name': 'CT-VLAN10', 'vn_name': 'VLAN10'},
                              'CT-VLAN20': {'bl_name': 'DC1', 'policy_id': 'vlan20-ct-policy-id',
                                            'ct_name': 'CT-VLAN20', 'vn_name': 'VLAN20'},
                              'CT-VLAN100': {'bl_name': 'DC1', 'policy_id': 'vlan100-ct-policy-id',
                                             'ct_name': 'CT-VLAN100', 'vn_name': 'VLAN100'},
                              'CT-VLAN200': {'bl_name': 'DC1', 'policy_id': 'vlan200-ct-policy-id',
                                             'ct_name': 'CT-VLAN200', 'vn_name': 'VLAN200'}, }

dc1_ct_int_assign_dic = {'ae1': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN10',
                                 'leaf_name': 'jnpr_esi_leaf_001', 'int_name': 'ae1'},
                         'xe-0/0/2': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN10',
                                      'leaf_name': 'jnpr_single_leaf_001', 'int_name': 'xe-0/0/2'},
                         'xe-0/0/3_CT-VLAN20': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN20',
                                                'leaf_name': 'jnpr_single_leaf_001', 'int_name': 'xe-0/0/3'},
                         'xe-0/0/3_CT-VLAN100': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN100',
                                                 'leaf_name': 'jnpr_esi_leaf_001', 'int_name': 'xe-0/0/3'},
                         'xe-0/0/4': {'bl_name': 'DC1', 'ct_name': 'CT-VLAN200',
                                    'leaf_name': 'jnpr_single_leaf_001', 'int_name': 'xe-0/0/4'}, }

"""
DC2 Blueprint Routing Zones Dictionaries
"""

dc2_routing_zones_dic = {'customer-1': {'bl_name': 'DC2', 'rz_name': 'customer-1', 'vni_id': 10010},
                         'customer-2': {'bl_name': 'DC2', 'rz_name': 'customer-2', 'vni_id': 10020}, }

dc2_routing_zones_loopback_dic = {'customer-1': {'bl_name': 'DC2', 'rz_name': 'customer-1',
                                                 'lb_ip': 'DC2-VIRTUAL-LEAF-LOOPBACK'},
                                  'customer-2': {'bl_name': 'DC2', 'rz_name': 'customer-2',
                                                 'lb_ip': 'DC2-VIRTUAL-LEAF-LOOPBACK'}, }

dc2_virtual_network_dic = {'VLAN10': {'bl_name': 'DC2', 'vn_name': 'VLAN10', 'rz_name': 'customer-1',
                                      'network': '192.168.10.0/24', 'gw': '192.168.10.1', 'vlan_id': 10, 'vni_id': 5010},
                           'VLAN20': {'bl_name': 'DC2', 'vn_name': 'VLAN20', 'rz_name': 'customer-1',
                                      'network': '192.168.20.0/24', 'gw': '192.168.20.1', 'vlan_id': 20, 'vni_id': 5020},
                           'VLAN30': {'bl_name': 'DC2', 'vn_name': 'VLAN30', 'rz_name': 'customer-1',
                                      'network': '192.168.30.0/24', 'gw': '192.168.30.1', 'vlan_id': 30, 'vni_id': 5030},
                           'VLAN200': {'bl_name': 'DC2', 'vn_name': 'VLAN200', 'rz_name': 'customer-2',
                                       'network': '192.168.200.0/24', 'gw': '192.168.200.1', 'vlan_id': 200, 'vni_id': 5200}, }

dc2_ct_virtual_network_dic = {'CT-VLAN10': {'bl_name': 'DC2', 'policy_id': 'vlan10-ct-policy-id',
                                            'ct_name': 'CT-VLAN10', 'vn_name': 'VLAN10'},
                              'CT-VLAN20': {'bl_name': 'DC2', 'policy_id': 'vlan20-ct-policy-id',
                                            'ct_name': 'CT-VLAN20', 'vn_name': 'VLAN20'},
                              'CT-VLAN30': {'bl_name': 'DC2', 'policy_id': 'vlan30-ct-policy-id',
                                            'ct_name': 'CT-VLAN30', 'vn_name': 'VLAN30'},
                              'CT-VLAN200': {'bl_name': 'DC2', 'policy_id': 'vlan200-ct-policy-id',
                                             'ct_name': 'CT-VLAN200', 'vn_name': 'VLAN200'}, }

dc2_ct_int_assign_dic = {'xe-0/0/2-1': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN10',
                                        'leaf_name': 'jnpr_single_leaf_001_001', 'int_name': 'xe-0/0/2'},
                         'xe-0/0/3-1': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN20',
                                        'leaf_name': 'jnpr_single_leaf_001_001', 'int_name': 'xe-0/0/3'},
                         'xe-0/0/4-1': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN200',
                                        'leaf_name': 'jnpr_single_leaf_001_001', 'int_name': 'xe-0/0/4'},
                         'xe-0/0/2-2': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN10',
                                        'leaf_name': 'jnpr_single_leaf_002_001', 'int_name': 'xe-0/0/2'},
                         'xe-0/0/3-2': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN20',
                                        'leaf_name': 'jnpr_single_leaf_002_001', 'int_name': 'xe-0/0/3'},
                         'xe-0/0/4-2': {'bl_name': 'DC2', 'ct_name': 'CT-VLAN30',
                                        'leaf_name': 'jnpr_single_leaf_002_001', 'int_name': 'xe-0/0/4'},
                         }


def api_create_asn_pool():

    for i in asn_dic.keys():

        asn_name = asn_dic[i].get('asn_name')
        asn_start = asn_dic[i].get('asn_start')
        asn_stop = asn_dic[i].get('asn_stop')

        create_asn_pool(asn_name, asn_start, asn_stop)


def api_create_vni_pool():

    for i in vni_dic.keys():

        vni_name = vni_dic[i].get('vni_name')
        vni_start = vni_dic[i].get('vni_start')
        vni_stop = vni_dic[i].get('vni_stop')

        create_vni_pool(vni_name, vni_start, vni_stop)


def api_create_ip_pool():

    for i in ip_pool_dic.keys():

        ip_name = ip_pool_dic[i].get('ip_name')
        network = ip_pool_dic[i].get('network')

        create_ip_pool(ip_name, network)


def api_create_logical_devices():

    logical_device_list = create_logical_devices_dic()

    for i in logical_device_list.keys():

        logical_name = logical_device_list[i].get('name')
        logical_data = logical_device_list[i].get('data')

        create_logical_device(logical_name,  logical_data)


def api_create_interface_map():

    interface_map_list = create_interface_map_dic()

    for i in interface_map_list.keys():

        interface_map_name = interface_map_list[i].get('name')
        interface_map_data = interface_map_list[i].get('data')

        create_interface_map(interface_map_name, interface_map_data)


def api_create_rack_type():

    rack_list = create_rack_type_dic()

    for i in rack_list.keys():

        rack_type_name = rack_list[i].get('name')
        rack_type_data = rack_list[i].get('data')

        create_rack_type(rack_type_name, rack_type_data)


def api_create_templates():

    template_list = create_templates_dic()

    for i in template_list.keys():

        template_name = template_list[i].get('name')
        template_data = template_list[i].get('data')

        create_template(template_name, template_data)


def api_create_blueprint():

    for i in blueprint_dic.keys():

        bl_name = blueprint_dic[i].get('bl_name')
        template_name = blueprint_dic[i].get('template_name')

        create_blueprint(bl_name, template_name)


def api_create_routing_zones(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        rz_name = dic_data[i].get('rz_name')
        vni_id = dic_data[i].get('vni_id')

        set_blueprint_sz(bl_name, rz_name, vni_id)


def api_set_rz_loopback(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        rz_name = dic_data[i].get('rz_name')
        lb_ip = dic_data[i].get('lb_ip')

        set_blueprint_sz_loopback(bl_name, rz_name, lb_ip)


def api_create_virtual_network(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        vn_name = dic_data[i].get('vn_name')
        rz_name = dic_data[i].get('rz_name')
        network = dic_data[i].get('network')
        gw = dic_data[i].get('gw')
        vlan_id = dic_data[i].get('vlan_id')
        vni_id = dic_data[i].get('vni_id')

        set_blueprint_vn(bl_name, vn_name, rz_name, network, gw, vlan_id, vni_id)


def api_create_vn_ct(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        policy_id = dic_data[i].get('policy_id')
        ct_name = dic_data[i].get('ct_name')
        vn_name = dic_data[i].get('vn_name')

        ct.set_virtual_network_ct(bl_name, policy_id, ct_name, vn_name)


def api_ct_int_assign(dic_data):

    dic_data = dic_data

    for i in dic_data.keys():

        bl_name = dic_data[i].get('bl_name')
        ct_name = dic_data[i].get('ct_name')
        leaf_name = dic_data[i].get('leaf_name')
        int_name = dic_data[i].get('int_name')

        ct.set_blueprint_server_link(bl_name, ct_name, leaf_name, int_name)


if __name__ == '__main__':

    print("################################################### Creating Common resources")

    api_create_asn_pool()
    api_create_vni_pool()
    api_create_ip_pool()
    
    sleep(2)
    
    print("################################################### Onbox/Offbox and Manage Devices")
    create_offbox_device('192.168.122.215', '192.168.122.228')
    check_agent_state()
    check_connection_state()
    manage_device_all()
    sleep(5)

    print("################################################### Design")
    api_create_logical_devices()
    api_create_interface_map()
    api_create_rack_type()
    api_create_templates()
    print("################################################### Create Blueprint")
    api_create_blueprint()

    sleep(10)
    
    # --------------------- DC1
    print("################################################### DC1 Configuration")
    
    # Allocate IP pools to blueprint
    blueprint_resource_asn_spine("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_asn_leaf("DC1", "DC1-ASN-POOL")
    sleep(1)
    blueprint_resource_loopback_spine("DC1", "DC1-SPINE-LOOPBACK")
    sleep(1)
    blueprint_resource_loopback_leaf("DC1", "DC1-LEAF-LOOPBACK")
    sleep(1)
    blueprint_resource_fabric_spine_leaf("DC1", "DC1-SPINE-LEAF")
    sleep(1)
    
    # assign device profiles to blueprint
    blueprint_device_profile_3_stage("DC1", "JNPR_vQFX-7x10-Spine", "JNPR_vQFX-10x10-Leaf", "JNPR_vQFX-8x10-BorderLeaf")
    sleep(2)
    
    # assign physical device to blueprint
    send_physical_device_parameters_dc1("DC1")
    sleep(2)
    api_create_routing_zones(dc1_routing_zones_dic)
    sleep(5)
    api_set_rz_loopback(dc1_routing_zones_loopback_dic)
    sleep(5)
    api_create_virtual_network(dc1_virtual_network_dic)
    sleep(5)
    
    sleep(5)
    set_deploy_blueprint("DC1", "DC1 Basic Configuration")
    sleep(5)

    # create external router connectivity template, assign interface and allocate IP Pool
    ct.set_external_router_ct("DC1", "dc1-r1-ct-policy-id", "CT-DC1-R1", "10.1.1.1", 65002)
    sleep(5)
    ct.set_blueprint_server_link("DC1", "CT-DC1-R1", "jnpr_border_leaf_001", "xe-0/0/4")
    sleep(5)
    blueprint_resource_generic_link_ip("DC1", "DC1-EXTERNAL-ROUTER")
    sleep(5)
    
    api_create_vn_ct(dc1_ct_virtual_network_dic)
    sleep(2)
    api_ct_int_assign(dc1_ct_int_assign_dic)
    
    sleep(5)
    
    set_deploy_blueprint("DC1", "DC1 Connectivity Templates")
    sleep(5)

    # --------------------- DC2
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
    
    blueprint_device_profile_5_stage("DC2", "JNPR_vQFX_7x10-SuperSpine", "JNPR_vQFX-7x10-Spine", "JNPR_vQFX-10x10-Leaf",
                                     "JNPR_vQFX-8x10-BorderLeaf")
    sleep(2)
    
    send_physical_device_parameters_dc2("DC2")
    sleep(2)
    
    
    api_create_routing_zones(dc2_routing_zones_dic)
    sleep(5)
    api_set_rz_loopback(dc2_routing_zones_loopback_dic)
    sleep(5)

    sleep(5)
    api_create_virtual_network(dc2_virtual_network_dic)
    sleep(5)

    set_deploy_blueprint("DC2", "DC2 Basic Configuration")
    
    sleep(5)
    # create external router connectivity template, assign interface and allocate IP Pool
    ct.set_external_router_ct("DC2", "dc2-r2-bl1-ct-policy-id", "CT-DC2-R2-BL1", "20.2.2.1", 65002)
    ct.set_external_router_ct("DC2", "dc2-r2-bl2-ct-policy-id", "CT-DC2-R2-BL2", "20.2.2.3", 65002)
    sleep(5)
    ct.set_blueprint_server_link("DC2", "CT-DC2-R2-BL1", "jnpr_border_leaf_001_001", "xe-0/0/4")
    ct.set_blueprint_server_link("DC2", "CT-DC2-R2-BL2", "jnpr_border_leaf_002_001", "xe-0/0/4")
    sleep(5)
    blueprint_resource_generic_link_ip("DC2", "DC2-EXTERNAL-ROUTER")
    sleep(5)
    
    # create virtual networks connectivity template and assign interfaces
    api_create_vn_ct(dc2_ct_virtual_network_dic)
    sleep(5)
    api_ct_int_assign(dc2_ct_int_assign_dic)

    set_deploy_blueprint("DC2", "DC2 Connectivity Templates")
    sleep(5)

    print("################################################### Remote Gateways Configuration")
    set_remote_gateway("DC1", 203, "DC2-BL1", "20.20.30.0", ["jnpr_border_leaf_001_leaf1"])
    set_remote_gateway("DC1", 205, "DC2-BL2", "20.20.30.2", ["jnpr_border_leaf_001_leaf1"])
    sleep(5)
    set_deploy_blueprint("DC1", "DC1 to DC2 External GW")
    sleep(5)
    set_remote_gateway("DC2", 102, "DC1-BL1", "10.20.30.0", ["leaf001_001_1", "leaf002_001_1"])
    sleep(5)
    set_deploy_blueprint("DC2", "DC2 to DC1 External GW")

    print("################################################### External Router Link MTU Configuration and enabling Generate EVPN host routes")
    set_external_router_interface_mtu("DC1", 9000, "enabled")
    sleep(5)
    set_deploy_blueprint("DC1", "External Router Link MTU 9000 and Generate EVPN host routes")
    set_external_router_interface_mtu("DC2", 9000, "enabled")
    sleep(5)
    set_deploy_blueprint("DC2", "External Router Link MTU 9000 and Generate EVPN host routes")
