import subprocess
from time import sleep
import create_lab
import time


def clean_memory():

    """Clean linux memory"""
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Clean Memory")
    check_memory = 'free -g'
    free_memory = 'sync; echo 3 > /proc/sys/vm/drop_caches'
    subprocess.call(check_memory, shell=True)
    sleep(2)
    subprocess.call(free_memory, shell=True)
    subprocess.call(check_memory, shell=True)
    sleep(5)


def defining_interfaces():

    """
    define Lx virtual interfaces to connect vQFX (spine, leafs, etc)
    define vqfx-int virtual interfaces to connect vQFX-RE and vQFX-PFE
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Generate Bridges")
    interface_list = []
    for fabric_interface in range(1, 40):
        interface_temp = "L" + str(fabric_interface)
        interface_list.append(interface_temp)

    for vqfx_internal_interface in range(1, 20):
        interface_temp = "vqfx-int-" + str(vqfx_internal_interface)
        interface_list.append(interface_temp)

    return interface_list


def defining_dummy_interfaces():

    """
    Define dummy interfaces to populate unused ports
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Generate dummy interfaces")
    dummy_interface_list = []

    for vqfx_internal_interface in range(1, 20):
        interface_temp = "dummy-int-" + str(vqfx_internal_interface)
        dummy_interface_list.append(interface_temp)

    return dummy_interface_list


def getting_destroyed_vqfx():

    """
    create a list with all destroyed vQFX
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get destroyed vqfx")

    vqfx_info = subprocess.Popen("virsh list --all | egrep 'dc[1-2]_' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vqfx_info and clean the empty spaces
    li_vqfx = list(vqfx_info.split("\n"))
    result = [ x for x in li_vqfx if x ]
    return result


def getting_destroyed_servers():

    """
    create a list with all destroyed customer vm and Apstra Server
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get destroyed Servers")

    vqfx_info = subprocess.Popen("virsh list --all | egrep 'c[1-2]_v|aos_server' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vqfx_info and clean the empty spaces
    li_vqfx = list(vqfx_info.split("\n"))
    result = [ x for x in li_vqfx if x ]
    return result


def getting_running_vqfx():

    """
    create a list with all running vQFX
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get Running vqfx")

    vqfx_info = subprocess.Popen("virsh list | egrep 'dc[1-2]_' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vqfx_info and clean the empty spaces
    li_vqfx = list(vqfx_info.split("\n"))
    result = [ x for x in li_vqfx if x ]
    return result


def getting_running_servers():

    """
    create a list with all running vQFX customer vm and Apstra Server
    """
    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Get Running Servers")

    vqfx_info = subprocess.Popen("virsh list | egrep 'c[1-2]_|aos_server' | awk '{print $2}'", shell=True,
                                 stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    # creates list of the vqfx_info and clean the empty spaces
    li_vqfx = list(vqfx_info.split("\n"))
    result = [ x for x in li_vqfx if x ]
    return result


def create_fabric_interface():

    """
    Create logical interfaces
    """
    interface_list = defining_interfaces()
    dummy_interface_list = defining_dummy_interfaces()

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Create fabric bridges")

    for br_interface in interface_list:

        cmd_brctl = f'/sbin/brctl addbr {br_interface}'
        cmd_ifconfig = f'/sbin/ifconfig {br_interface} up'
        subprocess.call(cmd_brctl, shell=True)
        subprocess.call(cmd_ifconfig, shell=True)

        lacp_ldp = f'echo 16384 > /sys/class/net/{br_interface}/bridge/group_fwd_mask'
        subprocess.call(lacp_ldp, shell=True)

        print(f'- Creating Interface {br_interface}')

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Create dummy bridges")

    for dummy in dummy_interface_list:

        cmd_brctl = f'/sbin/brctl addbr {dummy}'
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Creating Interface {dummy}')


def delete_fabric_interface():

    interface_list = defining_interfaces()
    dummy_interface_list = defining_dummy_interfaces()

    print("---------------------------------------------------------")
    print("---------------------------------------------------------")
    print("--------------------------------------------------------- Delete Bridges")

    print("--------------------------------------------------------- Delete fabric ridges")
    for br_interface in interface_list:


        cmd_brctl = f'/sbin/brctl delbr {br_interface}'
        cmd_ifconfig = f'/sbin/ifconfig {br_interface} down'
        subprocess.call(cmd_ifconfig, shell=True)
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Deleting Interface {br_interface}')

    print("--------------------------------------------------------- Delete dummy ridges")

    for dummy in dummy_interface_list:



        cmd_brctl = f'/sbin/brctl delbr {dummy}'
        cmd_ifconfig = f'/sbin/ifconfig {dummy} down'
        subprocess.call(cmd_ifconfig, shell=True)
        subprocess.call(cmd_brctl, shell=True)

        print(f'- Deleting Interface {dummy}')


def start_vmx():

    
    print("############################################################ Start vMX R1 and R2")
    start_r1 = f'./vmx.sh --start --cfg config_apstra/r1-apstra.conf'
    start_r2 = f'./vmx.sh --start --cfg config_apstra/r2-apstra.conf'
    bind_interfaces = f'./vmx.sh --bind-dev --cfg config_apstra/apstra-topology.conf'

    subprocess.call(start_r1, shell=True)
    sleep(2)
    subprocess.call(start_r2, shell=True)
    sleep(2)
    subprocess.call(bind_interfaces, shell=True)


def stop_vmx():

    print("############################################################ Stop vMX R1 and R2")
    stop_r1 = f'./vmx.sh --stop --cfg config_apstra/r1-apstra.conf'
    stop_r2 = f'./vmx.sh --stop --cfg config_apstra/r2-apstra.conf'
    unbind_interfaces = f'./vmx.sh --unbind-dev --cfg config_apstra/apstra-topology.conf'

    subprocess.call(stop_r1, shell=True)
    subprocess.call(stop_r2, shell=True)
    subprocess.call(unbind_interfaces, shell=True)


def start_servers():

    print("############################################################ Start Servers and Apstra Server")
    vqfx_list = getting_destroyed_servers()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh start {vqfx}'
        print(f'- Starting {vqfx}')
        subprocess.call(command, shell=True)
        sleep(2)


def stop_servers():

    print("############################################################ Destroy Servers")
    vqfx_list = getting_running_servers()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh destroy {vqfx}'
        print(f'- {vqfx}')
        subprocess.call(command, shell=True)
        sleep(1)


def start_vqfx():

    print("############################################################ Start vQFX")
    vqfx_list = getting_destroyed_vqfx()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh start {vqfx}'
        print(f'- Starting {vqfx}')
        subprocess.call(command, shell=True)
        sleep(2)


def stop_vqfx():

    print("############################################################ Destroy vQFX")
    vqfx_list = getting_running_vqfx()

    for vqfx in vqfx_list:
        command = f'/usr/bin/virsh destroy {vqfx}'
        print(f'- {vqfx}')
        subprocess.call(command, shell=True)
        sleep(1)


def start_topology():

    print("############################################################ Start Topology")
    clean_memory()
    create_fabric_interface()
    start_vqfx()
    start_servers()
    start_vmx()


def stop_topology():

    print("############################################################ Stop Topology")
    stop_vqfx()
    stop_servers()
    stop_vmx()
    delete_fabric_interface()
    clean_memory()


def create_topology():

    print("############################################################ Create Topology")
    clean_memory()
    create_fabric_interface()
    create_lab.create_lab_aos()
    sleep(10)
    create_lab.create_lab_vqfx()
    sleep(10)
    create_lab.create_lab_vms()
    sleep(10)
    create_lab.create_lab_vmx()
    sleep(5)
    create_lab.configure_vqfx()
    sleep(5)
    create_lab.configure_vmx()


def delete_topology():

    print("############################################################ Delete Topology")
    create_lab.delete_lab_vqfx()
    create_lab.delete_lab_vmx()
    create_lab.delete_lab_vms()
    create_lab.delete_lab_aos()
    delete_fabric_interface()
    clean_memory()


if __name__ == "__main__":

    print("1 - Start Topology")
    print("2 - Stop Topology")
    print("3 - Clean Memory Only")
    print("4 - Create topology from Scratch (Make sure you have no topology already running!!"
          "You can run option 5 to delete everything - Be careful!!")
    print("5 - Delete topology! This option will delete everything, be sure you want to proceed! ")

    select_function = input("Select one Option: ") or None

    if select_function == '1':
        start_time = time.time()
        start_topology()
        run_time = time.time() - start_time
        print("** Time to run: %s sec" % round(run_time, 2))
    elif select_function == '2':
        start_time = time.time()
        stop_topology()
        run_time = time.time() - start_time
        print("** Time to run: %s sec" % round(run_time, 2))
    elif select_function == '3':
        start_time = time.time()
        clean_memory()
        run_time = time.time() - start_time
        print("** Time to run: %s sec" % round(run_time, 2))
    elif select_function == '4':
        print("Are you sure you want to create a topology from scratch?")
        select_function = input("Type 'yes' or 'no': ").upper() or None
        if select_function == 'YES' or 'Y' or None:
            start_time = time.time()
            create_topology()
            run_time = time.time() - start_time
            print("** Time to run: %s sec" % round(run_time, 2))
            print("- Default vQFX, vMX and Host VMs user and password")
            print("- lab/lab123 and root/juniper123")
        else:
            print("Stopping the script!!!")
            exit()
    elif select_function == '5':
        print("Are you sure you want to delete everything?")
        select_function = input("Type 'yes' or 'no': ").upper() or None
        if select_function == 'YES' or 'Y' or None:
            start_time = time.time()
            delete_topology()
            run_time = time.time() - start_time
            print("** Time to run: %s sec" % round(run_time, 2))
        else:
            print("Stopping the script!!!")
            exit()
    else:
        print("Wrong option!! Nothing do to")