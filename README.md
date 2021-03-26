# Using Apstra to build a Juniper DC - (KVM environment)

## Authors

* **Gilberto Rampini**

## Getting Started

This document provides some basic configuration examples for lab purposes only in order to help you get started with the Apstra Intent Based-Networking and Juniper DC using vQFX. 

* **This lab guide does not intend to cover any best practice and/or production configuration. All the configuration provided in this guide, are just "simple examples"**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

This project will make available:

1. Python script to create, start, stop and delete the entire topology
2. All the necessary steps to create a full lab using Apstra and Juniper vQFX and vMX
3. Word document providing all steps to configure your entire topology
   If you are a Partner, contact your Juniper Account Manager
   If you are an End Customer, contact your Partner
4. MPLS Core configuration
5. Lab Topology

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
- Lab Network: 192.168.0.0/24 -> (You can change it by editing the python script)
- When creating the topology from scratch, you will need to configure your AOS Server: 
  - https://portal.apstra.com/docs/configure_aos.html


## Pre-requisites configs

This test lab has been built and tested using:

```
1. Ubuntu 16.04
2. Phisical Server with:
  2.1. 128GB RAM
  2.2. I9 with 14 Cores
  2.3. 500GB SSD
3. vQFX 20.2R1.10
4. vMX 20.4R1.12
5. Apstra 3.3.0
6. CentOS-7-x86_64-GenericCloud.qcow2
```

***Although we are downloading and copying packages and configurations within the /home/lab user directory, it's worth mentioning that I'm using root user access for every single step described here.***

## Pre-deployment Server Configs

### Pre-deployment Basic Packages

**Packages Installation and configuration**

```
lab@lab:~$ su -
root@lab:~# add-apt-repository ppa:deadsnakes/ppa
root@lab:~# apt-get -y update
root@lab:~# apt-get -y install qemu qemu-kvm libvirt-daemon  bridge-utils virt-manager ntp net-tools git python3.7 python3-dev python3-pip python3.7-dev libguestfs-tools


root@lab:~# python3.7 -m pip install pexpect
```

```
root@lab:~# usermod -aG libvirtd $USER
root@lab:~# usermod -aG kvm $USER

root@lab:~# usermod -aG libvirtd lab
root@lab:~# usermod -aG kvm lab
```

## Virtual MX Installation

* We are using vMX to simulate our Core MPLS.

Enable qemu-kvm hugepages

```
root@lab:~# sed -i -e 's/KVM_HUGEPAGES=0/KVM_HUGEPAGES=1/' /etc/default/qemu-kvm
```

Install additional vMX packages

```
root@lab:~# apt-get -y install python-pip python-netifaces

root@lab:~# pip install pyyaml 
root@lab:~# pip install netifaces
```

Change interface name and configure hugepages
```
root@lab:~# sed -i -e 's/GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0 default_hugepagesz=1G hugepagesz=1G hugepages=16G"/' /etc/default/grub
```

Configure Bridge br0

```
root@lab:~# vi /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface

auto br0
iface br0 inet static
      address 192.168.0.199
      netmask 255.255.255.0
      network 192.168.0.0
      gateway 192.168.0.1
      dns-nameservers 8.8.8.8 8.8.4.4
      bridge_ports eth0
      bridge_stp off
      bridge_maxwait 0
```

```
root@lab:~# update-grub

root@lab:~# reboot
```

## Preparing the environment

### Download vMX image to /home/lab

```
root@lab:/home/lab# tar -xzvf vmx-bundle-20.4R1.12.tgz

root@lab:/home/lab# cd vmx/

root@lab:/home/lab/vmx# 

root@lab:/home/lab/vmx# cp images/junos-vmx-x86-64-20.4R1.12.qcow2 /var/lib/libvirt/images/junos-vmx-x86-64-20.4R1.12.qcow2

root@lab:/home/lab/vmx# cp images/vmxhdd.img /var/lib/libvirt/images/vmxhdd.img

root@lab:/home/lab/vmx# cp images/vFPC-20201209.img /var/lib/libvirt/images/vFPC-20201209.img
```
### Download Apstra, Centos GenericCloud, and vQFX Images and copy to vmx/images

***You will have a directory like that one:***

```
root@lab:/home/lab/vmx# ls -l images/
total 7997348
-rw-r--r-- 1 root root 1951413760 Mar 25 11:07 aos_server_3.3.0.2-46.qcow2
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

```
root@lab:/home/lab/vmx# cd ..

root@lab:/home/lab# git clone https://github.com/gmr2020git/jnpr_apstra_kvm.git

root@lab:/home/lab# cp -rp jnpr_apstra_kvm/* vmx/

root@lab:/home/lab# cd vmx/
```

## Python Script 

1 - Start Topology - It will start the entire topology (you have to create it first - Option 4)
2 - Stop Topology - It will stop the entire topology
3 - Clean Memory Only - It will clean your server memory
4 - Create Topology - It will create the entire topology from scratch
5 - Delete Topology - It will delete and remove the entire topology and images

```
root@lab:/home/lab/vmx#  python3.7 start_stop.py 
1 - Start Topology

2 - Stop Topology

3 - Clean Memory Only

4 - Create topology

5 - Delete topology

Select one Option: 
```

## Core vMX R1 and R2 initial configuration

***After creating the topology from scratch you will need to configure your vMX R1 and R2***

1. r1 - check and apply the core1.conf - core_config folder
2. r2 - check and apply the core2.conf - core_config folder

## Apstra Server initial configuration

***After creating the topology from scratch you will need to configure your Apstra server. Please check the link below and follow the instructions:***
https://portal.apstra.com/docs/configure_aos.html

# Workaround vMX

***If you got an error to start vMX r1 and/or r2 please run the following commands:***

```
./vmx.sh --start --cfg config_apstra/r1-apstra.conf

./vmx.sh --start --cfg config_apstra/r2-apstra.conf
```

