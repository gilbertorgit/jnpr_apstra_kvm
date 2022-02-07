# Using Apstra to build a Juniper DC - (KVM environment)

## Authors

**Gilberto Rampini**

### Other Projects

https://github.com/gilbertorgit?tab=repositories

1. Enterprise Sonic and Apstra
   1. https://github.com/gilbertorgit/ent_sonic_apstra


## Topology

![Topology](https://github.com/gilbertorgit/jnpr_apstra_kvm/blob/main/Apstra_4_0/dci_3_5_stage/topology_prints/Topology.png)

![MGMT IP](https://github.com/gilbertorgit/jnpr_apstra_kvm/blob/main/Apstra_4_0/dci_3_5_stage/topology_prints/MGMT-IP.png)

## Getting Started

This document provides some basic configuration examples for lab purposes only in order to help you get started with the Apstra Intent Based-Networking and Juniper DC using vQFX. 

* **This lab guide does not intend to cover any best practice and/or production configuration. All the configuration provided in this guide, are just "simple examples"**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project will make available:

1. Python script to create, start, stop and delete the entire topology
2. All the necessary steps to create a full lab using Apstra and Juniper vQFX and vMX
3. Python script to create all Apstra configuration is provided in the folder "api_config" 
4. Alternatively, there is a PDF document providing all steps to configure your entire topology
   1. If you are a Partner, contact your account manager to have access
   2. If you are an end customer, contact your partner to have access
5. MPLS Core configuration
6. Lab Topology

Following this guide, you will be able to build

1. DC1 - 3-Stage Clos network 
2. DC2 - 5-Stage Clos network
3. Very simple Core MPLS
4. Enable DCI Connectivity

Important Information
- The python script available in this guide will create and delete all resources (vQFX, vMX, hosts, and AOS Server) It will also start and stop the entire topology.
- It's very important to keep the names and file paths as shown here, otherwise you likely to face issues
- It's very important to keep the verions of the images, otherwise you likely to face issues.   
- Default user and password: -> (You can change it by editing the python script)
  - root/juniper123 
  - lab/lab123 
- Lab Network IP and Interface information:
  - 192.168.122.0/24 -> defaul KVM bridge network (You can change it by editing the python script)
  - virbr0 - default KVM bridge interface
- When creating the topology from scratch, you will need to configure your AOS Server. Please see "Apstra_Installation" Folder
  - https://portal.apstra.com/docs/configure_aos.html
    
## Pre-requisites configs

This test lab has been built and tested using:

```
1. Ubuntu 18.04.5 LTS
2. Server with:
  2.1. 128GB RAM
  2.2. I9 with 14 Cores and Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz
  2.3. 500GB - SSD
3. vQFX 20.2R1.10
4. vMX 20.4R1.12
5. Apstra 4.0.2
6. CentOS-7-x86_64-GenericCloud.qcow2
```

***Although we are downloading and copying packages and configurations within the /home/lab user directory, it's worth mentioning that I'm using root user access for every single step described here.***

## Pre-deployment Server Configs

### Pre-deployment Server Configs and Basic Packages

**Packages Installation and configuration**

```
lab@lab:~$ sudo su -

root@lab:~$ cd /home/lab

root@lab:/home/lab# add-apt-repository ppa:deadsnakes/ppa

root@lab:/home/lab# apt-get -y update

root@lab:/home/lab# apt -y install ansible git

root@lab:/home/lab# git clone https://github.com/gmr2020git/jnpr_apstra_kvm.git

root@lab:/home/lab# ansible-playbook jnpr_apstra_kvm/base-pkg-kvm/playbook.yml
```

## Virtual MX Installation

* We are using vMX to simulate our Core MPLS.

Enable qemu-kvm hugepages

```
root@lab:~# sed -i -e 's/KVM_HUGEPAGES=0/KVM_HUGEPAGES=1/' /etc/default/qemu-kvm
```

Configure hugepages
```
root@lab:~# sed -i -e 's/GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX="default_hugepagesz=1G hugepagesz=1G hugepages=16G"/' /etc/default/grub
```

Change default virbr0 dhcp range from 254 to 100
```
root@lab:~# virsh net-edit default

from:
<range start='192.168.122.2' end='192.168.122.254'/>
to
<range start='192.168.122.2' end='192.168.122.100'/>
```

Update Grub and reboot the server
```
root@lab:~# update-grub

root@lab:~# reboot
```

## Preparing the environment

### Download vMX image to /home/lab

```
lab@lab:~$ sudo su -
root@lab:~$ cd /home/lab
root@lab:/home/lab# tar -xzvf vmx-bundle-20.4R1.12.tgz
```
### Download Apstra, Centos GenericCloud, and vQFX Images and copy to vmx/images

* Apstra - https://support.juniper.net/support/downloads/?p=apstra-fabric-conductor

* CentOS-7-x86_64-GenericCloud.qcow2 - https://cloud.centos.org/centos/7/images/

* vQFX - https://support.juniper.net/support/downloads/?p=vqfx-evaluation - Download as showed below:
![vQFX-Download](https://github.com/gilbertorgit/jnpr_apstra_kvm/blob/main/Apstra_4_0/dci_3_5_stage/topology_prints/vQFX-Download.png)

```
root@lab:~# cp aos_server_4.0.2-142.qcow2 CentOS-7-x86_64-GenericCloud.qcow2 jinstall-vqfx-10-f-20.2R1.10.img vqfx-20.2R1-2019010209-pfe-qemu.qcow   /home/lab/vmx/images/
```

***Make sure you download the right version as described in this guide. 
You will have a directory like that one:***

```
root@lab:/home/lab/vmx# ls -l /home/lab/vmx/images/
total 7997348
-rwx------ 1 root root 1972913664 Jan 14 09:22 aos_server_4.0.2-142.qcow2
-rw-r--r-- 1 root root  858783744 Mar 25 11:08 CentOS-7-x86_64-GenericCloud.qcow2
-rw-r--r-- 1 root root  588251136 Mar 25 11:08 jinstall-vqfx-10-f-20.2R1.10.img
-rw-r--r-- 1  930  930 1391656960 Dec 20 14:46 junos-vmx-x86-64-20.4R1.12.qcow2
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc0.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc10.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc11.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc1.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc2.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc3.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc4.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc5.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc6.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc7.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc8.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-fpc9.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-re0.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-re1.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-re.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-service-pic-10g.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-service-pic-2g.img
-rw-r--r-- 1  930  930   10485760 Dec 10 06:46 metadata-usb-service-pic-4g.img
-rw-r--r-- 1  930  930 2447376384 Dec 10 06:46 vFPC-20201209.img
-rw-r--r-- 1  930  930     197120 Dec 10 06:46 vmxhdd.img
-rw-r--r-- 1 root root  762839040 Mar 25 11:08 vqfx-20.2R1-2019010209-pfe-qemu.qcow
```

## Cloning jnpr_apstra_kvm project

```
root@lab:/home/lab# mv jnpr_apstra_kvm/Apstra_4_0/dci_3_5_stage/* vmx/

root@lab:/home/lab# cd vmx/
```

## Python Script

### Create Infrastructure

1. - Start Topology - It will start the entire topology (you have to create it first - Option 4)
2. - Stop Topology - It will stop the entire topology
3. - Clean Memory Only - It will clean your server memory
4. - Create Topology - It will create the entire topology from scratch
5. - Delete Topology - It will delete and remove the entire topology and images

* In case you are running your environment under a vmware hypervisor, you have to run a guestfish workaround before this script:

```
root@lab:~# export LIBGUESTFS_BACKEND_SETTINGS=force_tcg
```

```
root@lab:/home/lab/vmx# python3.7 start_stop.py 
1 - Start Topology

2 - Stop Topology

3 - Clean Memory Only

4 - Create topology

5 - Delete topology

Select one Option: 
```


## Apstra Server initial configuration

***After creating the topology from scratch you will need to configure your Apstra server. A

Access apstra server using console and check the instructions in the folder Apstra_Installation

* Apstra Server IP: 192.168.122.180 

* Default user and password: admin/admin
```
root@lab:~# virsh console apstra_server
```

* If you want to know more, please check the link below for further information:
  * https://portal.apstra.com/docs/configure_aos.html

***Configure ssh tunnel to access the Apstra UI*** 

* configure your ssh configuration to allow root, TCP and X11 Forwarding
```
root@lab:~# vi /etc/ssh/sshd_config

PermitRootLogin yes
AllowTcpForwarding yes
X11Forwarding yes
```

***SSH Tunnel Example using linux terminal***

```
ssh -L 8101:192.168.122.180:443 root@<YOUR_SERVER_IP> example:
ssh -L 8101:192.168.122.180:443 root@192.168.0.1
```

***SSH Tunnel Example using SecureCRT***

Create a connection to your server and go to "Properties" and configure the relevant parameters, example below:

![SecureCRT](https://github.com/gilbertorgit/jnpr_apstra_kvm/blob/main/Apstra_4_0/dci_3_5_stage/topology_prints/SecureCRT-1.png)

![SecureCRT](https://github.com/gilbertorgit/jnpr_apstra_kvm/blob/main/Apstra_4_0/dci_3_5_stage/topology_prints/SecureCRT-2.png)

## Apstra API Configuration Script

* The script below will configure the entire topology using APIs
```
root@lab:# cd /home/lab/vmx/api_config/

root@lab:/home/lab/vmx/api_config# python3.7 create_config_apstra_api.py
```

**You can check some scripts output in the folder "Output_Script_Example**

## Core vMX R1 and R2 initial configuration

* The pyhon script will configure your core, however in case you have any trouble you can check and apply the configuration
  * Please check "core_config" folder
    
## Customer VMs Access

* Default user and password: lab/lab123

```
root@lab:# virsh console <VM_NAME>

root@lab:# virsh console c1_v10_h1
```

## Workaround vMX

***If you face any error to start any virtual MX, please run the following commands:***

```
root@lab:/home/lab/vmx# ./vmx.sh --start --cfg config_apstra/r1-apstra.conf

root@lab:/home/lab/vmx# ./vmx.sh --start --cfg config_apstra/r2-apstra.conf
```

***In case your bond0 (vm_v10_h1) is not working properly, you will need to update the interface configuration***
```
root@lab:~# virsh console c1_v10_h1

--> login using root credentials: root/juniper123

[root@c1_v10_h1 ~]#vi /etc/sysconfig/network-scripts/ifcfg-bond0

Add the line below to the end of the file: 

BONDING_OPTS="mode=4 miimon=100 lacp_rate=1"

[root@c1_v10_h1 ~]# shutdown -r now
```

