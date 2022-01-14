"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import subprocess
import time
import console_config
import send_core_files
from time import sleep
import re
import os

re_image = '/var/lib/libvirt/images/vqfx-20.2R1.10-re.qcow2'
pfe_image = '/var/lib/libvirt/images/vqfx-20.2R1.10-pfe.qcow2'
generic_centos = '/var/lib/libvirt/images/CentOS-7-x86_64-GenericCloud.qcow2'
image_path = '/var/lib/libvirt/images/'
apstra_image = 'aos_server_4.0.2-142.qcow2'

aos_vm = {'apstra_server': {'hostname': 'apstra_server', 'eth0': 'virbr0', 'eth1': 'none'},}


def create_vqfx_dic():
    fhandle = open('vrdc_info.csv')
    hosts=dict()
    for line in fhandle:
        words = line.split(',')
        hosts.update({words[0]: dict()})
        n = len(words)
        for i in range(1, n-1, 2):
            if words[0] in hosts.keys():
                hosts[words[0]].update({words[i]:words[i+1]})

    return(hosts)


def create_vmx_dic():

    fhandle = open('vmx_info.csv')
    hosts=dict()
    for line in fhandle:
        words = line.split(',')
        hosts.update({words[0]: dict()})
        n = len(words)
        for i in range(1, n-1, 2):
            if words[0] in hosts.keys():
                hosts[words[0]].update({words[i]:words[i+1]})

    return(hosts)


def create_vm_dic():

    fhandle = open('vm_info.csv')
    hosts=dict()
    for line in fhandle:
        words = line.split(',')
        hosts.update({words[0]: dict()})
        n = len(words)
        for i in range(1, n-1, 2):
            if words[0] in hosts.keys():
                hosts[words[0]].update({words[i]:words[i+1]})

    return(hosts)


def create_lab_vqfx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating vQFX DC1 Topology")

    print("--------------------------------------------------------- Creating vQFX DC1 Images")

    copy_vqf_pfe = f'cp images/vqfx-20.2R1-2019010209-pfe-qemu.qcow {pfe_image}'
    copy_vqf_re = f'cp images/jinstall-vqfx-10-f-20.2R1.10.img {re_image}'

    subprocess.call(copy_vqf_pfe, shell=True)
    subprocess.call(copy_vqf_re, shell=True)

    vqfx_hosts = create_vqfx_dic()

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
            --os-variant generic \
            --nographics \
            --noautoconsole \
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
            --network bridge={xe_8},model=e1000'

            subprocess.call(install_vqfx_re, bufsize=2000, shell=True)
        else:
            vqfx_vm = f'cp {pfe_image} {image_path}{hostname}.qcow2'
            subprocess.call(vqfx_vm, shell=True)

            install_vqfx_pfe = f'virt-install --name {hostname} \
            --memory 2048 \
            --vcpus=2 \
            --import \
            --os-variant generic \
            --nographics \
            --noautoconsole \
            --disk path={image_path}{hostname}.qcow2,size=18,device=disk,bus=ide,format=qcow2 \
            --network bridge={dummy_int},model=e1000 \
            --network bridge={fabric_int},model=e1000'

            subprocess.call(install_vqfx_pfe, shell=True)


def delete_lab_vqfx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting vQFX Topology")

    delete_vqf_pfe = f'rm -f {pfe_image}'
    delete_vqf_re = f'rm -f {re_image}'

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

    vqfx_hosts = create_vqfx_dic()

    for i in vqfx_hosts.keys():
        delete_image = f"rm -f {image_path}{vqfx_hosts[i].get('hostname')}.qcow2"
        subprocess.call(delete_image, shell=True)


def create_lab_vms():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating Hosts VMs ")

    copy_cloud_image = f'cp images/CentOS-7-x86_64-GenericCloud.qcow2 {generic_centos}'
    subprocess.call(copy_cloud_image, shell=True)

    customer_vm = create_vm_dic()

    for i in customer_vm.keys():

        hostname = customer_vm[i].get('hostname')
        bond = customer_vm[i].get('bond')
        eth0 = customer_vm[i].get('eth0')
        eth1 = customer_vm[i].get('eth1')
        eth2 = customer_vm[i].get('eth2')

        print(f'--------------------------------------------------------- Creating VM {i}')

        create_img = f'qemu-img create -f qcow2 -o preallocation=metadata {image_path}{hostname}.qcow2 15G'
        exapand_img = f'virt-resize --expand /dev/sda1 {generic_centos} {image_path}{hostname}.qcow2'
        add_metadata = f'genisoimage -output {image_path}{hostname}-config.iso -volid cidata ' \
                       f'-joliet -r vm_config/{hostname}/user-data ' \
                       f'vm_config/{hostname}/meta-data vm_config/{hostname}/network-config'

        subprocess.call(create_img, shell=True)
        subprocess.call(exapand_img, shell=True)
        subprocess.call(add_metadata, shell=True)

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

    delete_cloud_image = f'rm -f {generic_centos}'
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

    customer_vm = create_vm_dic()

    for i in customer_vm.keys():
        delete_image = f"rm -f {image_path}{customer_vm[i].get('hostname')}.qcow2"
        delete_iso = f"rm -f {image_path}{customer_vm[i].get('hostname')}-config.iso"
        subprocess.call(delete_image, shell=True)
        subprocess.call(delete_iso, shell=True)


def create_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Creating AOS Server ")

    aos_vm.get('key1', {}).get('key2')

    hostname = aos_vm['apstra_server'].get('hostname')
    eth0 = aos_vm['apstra_server'].get('eth0')
    eth1 = aos_vm['apstra_server'].get('eth1')

    copy_aos_image = f'cp images/{apstra_image} {image_path}{hostname}.qcow2'
    subprocess.call(copy_aos_image, shell=True)

    install_aos = f'virt-install --name={hostname} \
    --vcpu=8 \
    --ram=32768 \
    --import \
    --disk={image_path}{hostname}.qcow2 \
    --os-type=linux --os-variant ubuntu16.04 \
    --network bridge={eth0},model=virtio \
    --noautoconsole'

    subprocess.call(install_aos, shell=True)


def delete_lab_aos():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting AOS Server")

    get_c_vm_name = subprocess.Popen("virsh list --all | egrep 'apstra_server' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    li_vm = list(get_c_vm_name.split("\n"))
    result = [x for x in li_vm if x]

    for image in result:

        print(f"--------------------------------------------------------- Deleting {image}")

        destroy_image = f'virsh destroy {image}'
        undefine_image = f'virsh undefine {image}'
        subprocess.call(destroy_image, shell=True)
        subprocess.call(undefine_image, shell=True)

        delete_image = f"rm -f {image_path}apstra_server.qcow2"
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

    vmx_hosts = create_vmx_dic()

    for i in vmx_hosts.keys():
        hostname = vmx_hosts[i].get('hostname')

        print(f'--------------------------------------------------------- Creating vMX {i}')

        create_vmx_router = f'./vmx.sh --start --cfg config_apstra/{hostname}-apstra.conf'
        subprocess.call(create_vmx_router, shell=True)
        sleep(5)

    for i in vmx_hosts.keys():
        hostname = vmx_hosts[i].get('hostname')
        vmx_info = subprocess.Popen("virsh list --all | egrep 'vcp-' | awk '{print $2}'", shell=True,
                                     stdout=subprocess.PIPE).stdout.read().decode('utf-8')
        # creates list of the vqfx_info and clean the empty spaces
        li_vmx = list(vmx_info.split("\n"))
        result = [x for x in li_vmx if x]
        print("########################### test vMX ##################################################################")
        print(result)
        print(f'vcp-{hostname}')
        print("########################### test vMX ##################################################################")
        if f'vcp-{hostname}' not in result:
            print(f'----- Trying to create {hostname} again')

            subprocess.call(create_vmx_router, shell=True)

    bind_interfaces = f'./vmx.sh --bind-dev --cfg config_apstra/apstra-topology.conf'
    subprocess.call(bind_interfaces, shell=True)


def delete_lab_vmx():

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Deleting Core MPLS")

    vmx_hosts = create_vmx_dic()

    for i in vmx_hosts.keys():
        hostname = vmx_hosts[i].get('hostname')

        delete_vmx_router = f'./vmx.sh --cleanup --cfg config_apstra/{hostname}-apstra.conf'
        subprocess.call(delete_vmx_router, shell=True)

    unbind_interfaces = f'./vmx.sh --unbind-dev --cfg config_apstra/apstra-topology.conf'
    delete_vmx_re = f'rm -f {image_path}junos-vmx-x86-64-20.4R1.12.qcow2'
    delete_vmx_hdd = f'rm -f {image_path}vmxhdd.img'
    delete_vmx_fpc = f'rm -f  {image_path}vFPC-20201209.img'
    clean_known_hosts = f'echo "" > ~/.ssh/known_hosts'

    subprocess.call(unbind_interfaces, shell=True)
    subprocess.call(delete_vmx_re, shell=True)
    subprocess.call(delete_vmx_hdd, shell=True)
    subprocess.call(delete_vmx_fpc, shell=True)
    subprocess.call(clean_known_hosts, shell=True)


def configure_vqfx():

    print("We will wait around 2 minutes to start the initial vQFX configuration")
    start_time = time.time()
    sleep(120)
    run_time = time.time() - start_time
    print("** Time waiting: %s sec" % round(run_time, 2))
    sleep(5)
    print("Send hostname e ip")

    vqfx_hosts = create_vqfx_dic()

    for i in vqfx_hosts.keys():
        hostname = vqfx_hosts[i].get('hostname')
        mgmt_ip = vqfx_hosts[i].get('mgmt_ip')
        if re.match('.*._re.*', hostname):
            print(f"- Sending {hostname} and {mgmt_ip} to configure basic access")
            console_config.config_vqfx(hostname, mgmt_ip)


def configure_vmx():

    print("We will wait around 1 minute to start the initial vMX CORE configuration")
    sleep(60)

    vmx_hosts = create_vmx_dic()

    for i in vmx_hosts.keys():
        hostname = vmx_hosts[i].get('hostname')
        mgmt_ip = vmx_hosts[i].get('mgmt_ip')

        print(f"Sending {hostname} and {mgmt_ip} to configure basic access")
        console_config.config_vmx(hostname, mgmt_ip)

    sleep(10)
    send_core_files.copy_file_vmx_router()