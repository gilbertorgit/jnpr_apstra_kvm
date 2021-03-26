import subprocess
import time
import console_config
from time import sleep
import re

re_image = '/var/lib/libvirt/images/vqfx-20.2R1.10-re.qcow2'
pfe_image = '/var/lib/libvirt/images/vqfx-20.2R1.10-pfe.qcow2'
generic_centos = '/var/lib/libvirt/images/CentOS-7-x86_64-GenericCloud.qcow2'
image_path = '/var/lib/libvirt/images/'

vqfx_hosts = {'dc1_leaf_1_re': {'hostname' : 'dc1_leaf_1_re','mgmt_ip': '192.168.0.217','mgmt_int': 'br0',
                             'fabric_int': 'vqfx-int-1', 'dummy_int': 'dummy-int-1', 'xe_0': 'L1', 'xe_1': 'L2',
                             'xe_2': 'dummy-int-1', 'xe_3': 'dummy-int-1', 'xe_4': 'L29', 'xe_5': 'dummy-int-1',
                             'xe_6': 'dummy-int-1', 'xe_7': 'dummy-int-1', 'xe_8': 'dummy-int-1',
                             'xe_9': 'dummy-int-1'},
              'dc1_leaf_1_pfe': {'hostname': 'dc1_leaf_1_pfe', 'fabric_int': 'vqfx-int-1', 'dummy_int': 'dummy-int-1'},

              'dc1_leaf_2_re': {'hostname' : 'dc1_leaf_2_re','mgmt_ip': '192.168.0.218','mgmt_int': 'br0',
                             'fabric_int': 'vqfx-int-2', 'dummy_int': 'dummy-int-2', 'xe_0': 'L3', 'xe_1': 'L4',
                             'xe_2': 'dummy-int-2', 'xe_3': 'dummy-int-2', 'xe_4': 'L18', 'xe_5': 'L19',
                             'xe_6': 'dummy-int-2', 'xe_7': 'dummy-int-2', 'xe_8': 'dummy-int-2',
                             'xe_9': 'dummy-int-2'},
              'dc1_leaf_2_pfe': {'hostname': 'dc1_leaf_2_pfe', 'fabric_int': 'vqfx-int-2', 'dummy_int': 'dummy-int-2'},

              'dc1_leaf_3_re': {'hostname': 'dc1_leaf_3_re', 'mgmt_ip': '192.168.0.219', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-3', 'dummy_int': 'dummy-int-3', 'xe_0': 'L5', 'xe_1': 'L6',
                                'xe_2': 'dummy-int-3', 'xe_3': 'dummy-int-3', 'xe_4': 'L20', 'xe_5': 'L21',
                                'xe_6': 'L22', 'xe_7': 'dummy-int-3', 'xe_8': 'dummy-int-3',
                                'xe_9': 'dummy-int-3'},
              'dc1_leaf_3_pfe': {'hostname': 'dc1_leaf_3_pfe', 'fabric_int': 'vqfx-int-3', 'dummy_int': 'dummy-int-3'},

              'dc1_spine_1_re': {'hostname': 'dc1_spine_1_re', 'mgmt_ip': '192.168.0.215', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-4', 'dummy_int': 'dummy-int-4', 'xe_0': 'L7', 'xe_1': 'L1',
                                'xe_2': 'L3', 'xe_3': 'L5', 'xe_4': 'dummy-int-4', 'xe_5': 'dummy-int-4',
                                'xe_6': 'dummy-int-4', 'xe_7': 'dummy-int-4', 'xe_8': 'dummy-int-4',
                                'xe_9': 'dummy-int-4'},
              'dc1_spine_1_pfe': {'hostname': 'dc1_spine_1_pfe', 'fabric_int': 'vqfx-int-4', 'dummy_int': 'dummy-int-4'},

              'dc1_spine_2_re': {'hostname': 'dc1_spine_2_re', 'mgmt_ip': '192.168.0.216', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-5', 'dummy_int': 'dummy-int-5', 'xe_0': 'L8', 'xe_1': 'L2',
                                'xe_2': 'L4', 'xe_3': 'L6', 'xe_4': 'dummy-int-5', 'xe_5': 'dummy-int-5',
                                'xe_6': 'dummy-int-5', 'xe_7': 'dummy-int-5', 'xe_8': 'dummy-int-5',
                                'xe_9': 'dummy-int-5'},
              'dc1_spine_2_pfe': {'hostname': 'dc1_spine_2_pfe', 'fabric_int': 'vqfx-int-5', 'dummy_int': 'dummy-int-5'},

              'dc1_borderleaf_1_re': {'hostname': 'dc1_borderleaf_1_re', 'mgmt_ip': '192.168.0.225', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-6', 'dummy_int': 'dummy-int-6', 'xe_0': 'L7', 'xe_1': 'L8',
                                'xe_2': 'dummy-int-6', 'xe_3': 'dummy-int-6', 'xe_4': 'dummy-int-6', 'xe_5': 'dummy-int-6',
                                'xe_6': 'L9', 'xe_7': 'dummy-int-6', 'xe_8': 'dummy-int-6',
                                'xe_9': 'dummy-int-6'},
              'dc1_borderleaf_1_pfe': {'hostname': 'dc1_borderleaf_1_pfe', 'fabric_int': 'vqfx-int-6', 'dummy_int': 'dummy-int-6'},

              'dc2_leaf_1_re': {'hostname' : 'dc2_leaf_1_re','mgmt_ip': '192.168.0.222','mgmt_int': 'br0',
                             'fabric_int': 'vqfx-int-7', 'dummy_int': 'dummy-int-7', 'xe_0': 'L12', 'xe_1': 'dummy-int-7',
                             'xe_2': 'dummy-int-7', 'xe_3': 'dummy-int-7', 'xe_4': 'L23', 'xe_5': 'L24',
                             'xe_6': 'L25', 'xe_7': 'dummy-int-7', 'xe_8': 'dummy-int-7',
                             'xe_9': 'dummy-int-7'},
              'dc2_leaf_1_pfe': {'hostname': 'dc2_leaf_1_pfe', 'fabric_int': 'vqfx-int-7', 'dummy_int': 'dummy-int-7'},

              'dc2_leaf_2_re': {'hostname' : 'dc2_leaf_2_re','mgmt_ip': '192.168.0.223','mgmt_int': 'br0',
                             'fabric_int': 'vqfx-int-8', 'dummy_int': 'dummy-int-8', 'xe_0': 'L13', 'xe_1': 'dummy-int-8',
                             'xe_2': 'dummy-int-8', 'xe_3': 'dummy-int-8', 'xe_4': 'L26', 'xe_5': 'L27',
                             'xe_6': 'L28', 'xe_7': 'dummy-int-8', 'xe_8': 'dummy-int-8',
                             'xe_9': 'dummy-int-8'},
              'dc2_leaf_2_pfe': {'hostname': 'dc2_leaf_2_pfe', 'fabric_int': 'vqfx-int-8', 'dummy_int': 'dummy-int-8'},

              'dc2_borderleaf_1_re': {'hostname': 'dc2_borderleaf_1_re', 'mgmt_ip': '192.168.0.226', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-9', 'dummy_int': 'dummy-int-9', 'xe_0': 'L11', 'xe_1': 'dummy-int-9',
                                'xe_2': 'dummy-int-9', 'xe_3': 'dummy-int-9', 'xe_4': 'dummy-int-9', 'xe_5': 'dummy-int-9',
                                'xe_6': 'L10', 'xe_7': 'dummy-int-9', 'xe_8': 'dummy-int-9',
                                'xe_9': 'dummy-int-9'},
              'dc2_borderleaf_1_pfe': {'hostname': 'dc2_borderleaf_1_pfe', 'fabric_int': 'vqfx-int-9', 'dummy_int': 'dummy-int-9'},

              'dc2_borderleaf_2_re': {'hostname': 'dc2_borderleaf_2_re', 'mgmt_ip': '192.168.0.227', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-10', 'dummy_int': 'dummy-int-10', 'xe_0': 'L14', 'xe_1': 'dummy-int-10',
                                'xe_2': 'dummy-int-10', 'xe_3': 'dummy-int-10', 'xe_4': 'dummy-int-10', 'xe_5': 'dummy-int-10',
                                'xe_6': 'L15', 'xe_7': 'dummy-int-10', 'xe_8': 'dummy-int-10',
                                'xe_9': 'dummy-int-10'},
              'dc2_borderleaf_2_pfe': {'hostname': 'dc2_borderleaf_2_pfe', 'fabric_int': 'vqfx-int-10', 'dummy_int': 'dummy-int-10'},

              'dc2_spine_1_re': {'hostname': 'dc2_spine_1_re', 'mgmt_ip': '192.168.0.220', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-11', 'dummy_int': 'dummy-int-11', 'xe_0': 'L16', 'xe_1': 'L11',
                                'xe_2': 'L12', 'xe_3': 'dummy-int-11', 'xe_4': 'dummy-int-11', 'xe_5': 'dummy-int-11',
                                'xe_6': 'dummy-int-11', 'xe_7': 'dummy-int-11', 'xe_8': 'dummy-int-11',
                                'xe_9': 'dummy-int-11'},
              'dc2_spine_1_pfe': {'hostname': 'dc2_spine_1_pfe', 'fabric_int': 'vqfx-int-11', 'dummy_int': 'dummy-int-11'},

              'dc2_spine_2_re': {'hostname': 'dc2_spine_2_re', 'mgmt_ip': '192.168.0.221', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-12', 'dummy_int': 'dummy-int-12', 'xe_0': 'L17', 'xe_1': 'L14',
                                'xe_2': 'L13', 'xe_3': 'dummy-int-12', 'xe_4': 'dummy-int-12', 'xe_5': 'dummy-int-12',
                                'xe_6': 'dummy-int-12', 'xe_7': 'dummy-int-12', 'xe_8': 'dummy-int-12',
                                'xe_9': 'dummy-int-12'},
              'dc2_spine_2_pfe': {'hostname': 'dc2_spine_2_pfe', 'fabric_int': 'vqfx-int-12', 'dummy_int': 'dummy-int-12'},

              'dc2_superspine_1_re': {'hostname': 'dc2_superspine_1_re', 'mgmt_ip': '192.168.0.224', 'mgmt_int': 'br0',
                                'fabric_int': 'vqfx-int-13', 'dummy_int': 'dummy-int-13', 'xe_0': 'L16', 'xe_1': 'L17',
                                'xe_2': 'dummy-int-13', 'xe_3': 'dummy-int-13', 'xe_4': 'dummy-int-13', 'xe_5': 'dummy-int-13',
                                'xe_6': 'dummy-int-13', 'xe_7': 'dummy-int-13', 'xe_8': 'dummy-int-13',
                                'xe_9': 'dummy-int-13'},
              'dc2_superspine_1_pfe': {'hostname': 'dc2_superspine_1_pfe', 'fabric_int': 'vqfx-int-13', 'dummy_int': 'dummy-int-13'},
              }

customer_vm = {'c1_v10_h1': {'hostname': 'c1_v10_h1', 'bond': 'True', 'eth0': 'br0', 'eth1': 'L29', 'eth2': 'L18'},
              'c1_v10_h2': {'hostname': 'c1_v10_h2', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L20', 'eth2': 'none'},
              'c1_v10_h4': {'hostname': 'c1_v10_h4', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L23', 'eth2': 'none'},
              'c1_v10_h6': {'hostname': 'c1_v10_h6', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L26', 'eth2': 'none'},
              'c1_v20_h3': {'hostname': 'c1_v20_h3', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L21', 'eth2': 'none'},
              'c1_v20_h5': {'hostname': 'c1_v20_h5', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L24', 'eth2': 'none'},
              'c1_v20_h7': {'hostname': 'c1_v20_h7', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L27', 'eth2': 'none'},
              'c1_v30_h8': {'hostname': 'c1_v30_h8', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L28', 'eth2': 'none'},
              'c2_v100_h1': {'hostname': 'c2_v100_h1', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L19', 'eth2': 'none'},
              'c2_v200_h2': {'hostname': 'c2_v200_h2', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L22', 'eth2': 'none'},
              'c2_v200_h3': {'hostname': 'c2_v200_h3', 'bond': 'False', 'eth0': 'br0', 'eth1': 'L25', 'eth2': 'none'},
              }


def create_lab_vqfx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating vQFX DC1 Topology")

    print("--------------------------------------------------------- Creating vQFX DC1 Images")

    copy_vqf_pfe = f'cp images/vqfx-20.2R1-2019010209-pfe-qemu.qcow {image_path}vqfx-20.2R1.10-pfe.qcow2'
    copy_vqf_re = f'cp images/jinstall-vqfx-10-f-20.2R1.10.img {image_path}vqfx-20.2R1.10-re.qcow2'

    subprocess.call(copy_vqf_pfe, shell=True)
    subprocess.call(copy_vqf_re, shell=True)

    for i in vqfx_hosts.keys():

        hostname = vqfx_hosts[i].get('hostname')
        mgmt_int = vqfx_hosts[i].get('mgmt_int')
        mgmt_ip = vqfx_hosts[i].get('mgmt_ip')
        fabric_int = vqfx_hosts[i].get('fabric_int')
        dummy_int = vqfx_hosts[i].get('dummy_int')
        xe_0 = vqfx_hosts[i].get('xe_0')
        xe_1 = vqfx_hosts[i].get('xe_1')
        xe_2 = vqfx_hosts[i].get('xe_2')
        xe_3 = vqfx_hosts[i].get('xe_3')
        xe_4 = vqfx_hosts[i].get('xe_4')
        xe_5 = vqfx_hosts[i].get('xe_5')
        xe_6 = vqfx_hosts[i].get('xe_6')
        xe_7 = vqfx_hosts[i].get('xe_7')
        xe_8 = vqfx_hosts[i].get('xe_8')
        xe_9 = vqfx_hosts[i].get('xe_9')

        print(f'--------------------------------------------------------- Creating vQFX {i}')

        if re.match('.*._re.*', hostname):
            vqfx_vm = f'cp {re_image} {image_path}{hostname}.qcow2'
            subprocess.call(vqfx_vm, shell=True)

            install_vqfx_re = f'virt-install --name {hostname} \
            --memory 2048 \
            --vcpus=2 \
            --import \
            --disk path={image_path}{hostname}.qcow2,size=18,device=disk,bus=ide,format=qcow2 \
            --network bridge={mgmt_int},model=e1000 \
            --network bridge={fabric_int},model=e1000 \
            --network bridge={dummy_int},model=e1000 \
            --network bridge={xe_0},model=e1000 \
            --network bridge={xe_1},model=e1000 \
            --network bridge={xe_2},model=e1000 \
            --network bridge={xe_3},model=e1000 \
            --network bridge={xe_4},model=e1000 \
            --network bridge={xe_5},model=e1000 \
            --network bridge={xe_6},model=e1000 \
            --network bridge={xe_7},model=e1000 \
            --network bridge={xe_8},model=e1000 \
            --network bridge={xe_9},model=e1000 \
            --noautoconsole'
            subprocess.call(install_vqfx_re, shell=True)
        else:
            vqfx_vm = f'cp {pfe_image} {image_path}{hostname}.qcow2'
            subprocess.call(vqfx_vm, shell=True)

            install_vqfx_pfe = f'virt-install --name {hostname} \
            --memory 2048 \
            --vcpus=2 \
            --import \
            --disk path={image_path}{hostname}.qcow2,size=18,device=disk,bus=ide,format=qcow2 \
            --network bridge={dummy_int},model=e1000 \
            --network bridge={fabric_int},model=e1000 \
            --graphics vnc,listen=0.0.0.0 \
            --noautoconsole'
            subprocess.call(install_vqfx_pfe, shell=True)


def delete_lab_vqfx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting vQFX Topology")

    delete_vqf_pfe = f'rm -f {image_path}vqfx-20.2R1.10-pfe.qcow2'
    delete_vqf_re = f'rm -f {image_path}vqfx-20.2R1.10-re.qcow2'

    subprocess.call(delete_vqf_pfe, shell=True)
    subprocess.call(delete_vqf_re, shell=True)

    get_vqfx_name = subprocess.Popen("virsh list --all | egrep 'dc[1-2]_' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vqfx = list(get_vqfx_name.split("\n"))
    result = [x for x in li_vqfx if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

    for i in vqfx_hosts.keys():
        delete_image = f"rm -f {image_path}{vqfx_hosts[i].get('hostname')}.qcow2"
        subprocess.call(delete_image, shell=True)


def create_lab_vms():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating Hosts VMs ")

    copy_cloud_image = f'cp images/CentOS-7-x86_64-GenericCloud.qcow2 /var/lib/libvirt/images/'
    subprocess.call(copy_cloud_image, shell=True)

    for i in customer_vm.keys():

        hostname = customer_vm[i].get('hostname')
        bond = customer_vm[i].get('bond')
        eth0 = customer_vm[i].get('eth0')
        eth1 = customer_vm[i].get('eth1')
        eth2 = customer_vm[i].get('eth2')

        print(f'--------------------------------------------------------- Creating VM {i}')

        create_img = f'qemu-img create -f qcow2 -o preallocation=metadata {image_path}{hostname}.qcow2 20G'
        exapand_img = f'virt-resize --expand /dev/sda1 {generic_centos} {image_path}{hostname}.qcow2'
        add_metadata = f'genisoimage -output {image_path}{hostname}-config.iso -volid cidata ' \
                       f'-joliet -r vm_config/{hostname}/user-data ' \
                       f'vm_config/{hostname}/meta-data vm_config/{hostname}/network-config'

        subprocess.call(create_img, shell=True)
        subprocess.call(exapand_img, shell=True)
        subprocess.call(add_metadata, shell=True)

        print(f'######################### bond')
        if bond == "True":
            install_c_vm = f'virt-install --import --name {hostname} \
            --ram 1024 --vcpus 1 \
            --disk {image_path}{hostname}.qcow2,format=qcow2,bus=virtio \
            --disk {image_path}{hostname}-config.iso,device=cdrom \
            --network bridge={eth0},model=e1000 \
            --network bridge={eth1},model=e1000 \
            --network bridge={eth2},model=e1000 \
            --os-type=linux --os-variant=rhel7 \
            --noautoconsole \
            --accelerate'
            subprocess.call(install_c_vm, shell=True)
        else:
            install_c_vm = f'virt-install --import --name {hostname} \
            --ram 1024 --vcpus 1 \
            --disk {image_path}{hostname}.qcow2,format=qcow2,bus=virtio \
            --disk {image_path}{hostname}-config.iso,device=cdrom \
            --network bridge={eth0},model=e1000 \
            --network bridge={eth1},model=e1000 \
            --os-type=linux --os-variant=rhel7 \
            --noautoconsole \
            --accelerate'
            subprocess.call(install_c_vm, shell=True)


def delete_lab_vms():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting Host VMs")

    delete_cloud_image = f'rm -f /var/lib/libvirt/images/CentOS-7-x86_64-GenericCloud.qcow2'
    subprocess.call(delete_cloud_image, shell=True)

    get_c_vm_name = subprocess.Popen("virsh list --all | egrep 'c[1-2]_v' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vm = list(get_c_vm_name.split("\n"))
    result = [x for x in li_vm if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

    for i in customer_vm.keys():
        delete_image = f"rm -f {image_path}{customer_vm[i].get('hostname')}.qcow2"
        delete_iso = f"rm -f {image_path}{customer_vm[i].get('hostname')}-config.iso"
        subprocess.call(delete_image, shell=True)
        subprocess.call(delete_iso, shell=True)


def create_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating AOS Server ")

    copy_aos_image = f'cp images/aos_server_3.3.0.2-46.qcow2 {image_path}aos_server_3_3.qcow2'
    subprocess.call(copy_aos_image, shell=True)

    install_aos = f'virt-install --name=aos_server_3_3 \
    --vcpu=8 \
    --ram=16384 \
    --import \
    --disk={image_path}aos_server_3_3.qcow2 \
    --os-type=linux --os-variant ubuntu16.04 \
    --network bridge=br0,model=virtio \
    --noautoconsole '

    subprocess.call(install_aos, shell=True)


def delete_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting AOS Server")

    get_c_vm_name = subprocess.Popen("virsh list --all | egrep 'aos_server' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vm = list(get_c_vm_name.split("\n"))
    result = [x for x in li_vm if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

        delete_image = f"rm -f {image_path}aos_server_3_3.qcow2"
        subprocess.call(delete_image, shell=True)


def create_lab_vmx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating Core MPLS ")

    copy_vmx_re = f'cp images/junos-vmx-x86-64-20.4R1.12.qcow2 {image_path}junos-vmx-x86-64-20.4R1.12.qcow2'
    copy_vmx_hdd = f'cp images/vmxhdd.img {image_path}vmxhdd.img'
    copy_vmx_fpc = f'cp images/vFPC-20201209.img  {image_path}vFPC-20201209.img'

    subprocess.call(copy_vmx_re, shell=True)
    subprocess.call(copy_vmx_hdd, shell=True)
    subprocess.call(copy_vmx_fpc, shell=True)

    create_r1 = f'./vmx.sh --start --cfg config_apstra/r1-apstra.conf'
    create_r2 = f'./vmx.sh --start --cfg config_apstra/r2-apstra.conf'
    bind_interfaces = f'./vmx.sh --bind-dev --cfg config_apstra/apstra-topology.conf'

    subprocess.call(create_r1, shell=True)
    subprocess.call(create_r2, shell=True)
    sleep(10)

    vmx_info = subprocess.Popen("virsh list --all | egrep 'vcp-' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vqfx_info and clean the empty spaces
    li_vmx = list(vmx_info.split("\n"))
    result = [x for x in li_vmx if x]
    print("########################### test vMX ##################################################################")
    print(result)
    print("########################### test vMX ##################################################################")
    if 'vcp-r1' not in result:
        print('----- Trying to create R1 again')

        subprocess.call(create_r1, shell=True)

    if 'vcp-r2' not in result:
        print('----- Trying to create R2 again')

        subprocess.call(create_r2, shell=True)

    subprocess.call(bind_interfaces, shell=True)


def delete_lab_vmx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting Core MPLS")

    delete_r1 = f'./vmx.sh --cleanup --cfg config_apstra/r1-apstra.conf'
    delete_r2 = f'./vmx.sh --cleanup --cfg config_apstra/r2-apstra.conf'
    unbind_interfaces = f'./vmx.sh --unbind-dev --cfg config_apstra/apstra-topology.conf'

    subprocess.call(delete_r1, shell=True)
    subprocess.call(delete_r2, shell=True)
    subprocess.call(unbind_interfaces, shell=True)

    delete_vmx_re = f'rm -f {image_path}junos-vmx-x86-64-20.4R1.12.qcow2'
    delete_vmx_hdd = f'rm -f {image_path}vmxhdd.img'
    delete_vmx_fpc = f'rm -f  {image_path}vFPC-20201209.img'

    subprocess.call(delete_vmx_re, shell=True)
    subprocess.call(delete_vmx_hdd, shell=True)
    subprocess.call(delete_vmx_fpc, shell=True)


def configure_vqfx():

    print("We will wait around 2 minutes to start the initial vQFX configuration")
    start_time = time.time()
    sleep(120)
    run_time = time.time() - start_time
    print("** Time waiting: %s sec" % round(run_time, 2))
    sleep(5)
    print("Send hostname e ip")
    for i in vqfx_hosts.keys():
        hostname = vqfx_hosts[i].get('hostname')
        mgmt_ip = vqfx_hosts[i].get('mgmt_ip')
        if re.match('.*._re.*', hostname):
            print(f"- Sending {hostname} and {mgmt_ip} to configure basic access")
            console_config.config_vqfx(hostname, mgmt_ip)


def configure_vmx():

    print("We will wait around 1 minute to start the initial vMX(R1 and R2) basic configuration")
    sleep(60)

    print("Sending r1 and 192.168.0.176 to configure basic access")
    console_config.config_vmx('r1', '192.168.0.176')
    print("Sending  r2 and 192.168.0.177 to configure basic access")
    console_config.config_vmx('r2', '192.168.0.177')