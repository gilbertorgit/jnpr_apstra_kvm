# Using Apstra to build a Juniper DC - (KVM environment)

## Authors

* **Gilberto Rampini**

## Getting Started

This document provides some basic configuration examples for lab purposes only in order to help you get started with the Apstra Intent Based-Networking and Juniper DC using vQFX. 

* **This lab guide does not intend to cover any best practice and/or production configuration. All the configuration provided in this guide, are just "simple examples"**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
this project will make available:

1. Python script to create, start, stop and delete the topology
2. All the necessary steps to create a full lab using Apstra and Juniper vQFX and vMX
3. Document with all prints to configure your Data Center
4. MPLS Core configuration
5. Lab Topology

Following this guide, you will be able to build

1. DC1 - 3-Stage Clos network 
2. DC2 - 5-Stage Clos network
3. Very simple Core MPLS
4. Enable DCI Connectivity

Important Information
- The python script will not create and configure Hosts VMs and Apstra server. You will need to create and configure both before using this script
- The python script available in this guide will create and delete all resources (vQFX, hosts and AOS Server) It will also start and stop the entire topology.
- It's very important to keep the names and file paths as shown here, otherwise you likely to face issues
- Default vQFX and vMX user and password: -> (You can change it editing the python script)
  - root/juniper123 
  - lab/lab123 
- Lab Network: 192.168.0.0/24 -> (You can change it editing the python script)
- When creating the topology from scratch, you will need to configure your AOS Server: https://portal.apstra.com/docs/configure_aos.html



## Pre-requisites configs

This test lab has been built and tested usign:

```
1. Ubuntu 16.04
2. Phisical Server with:
  2.1. 128GB RAM
  2.2. I9 with 14 Cores
  2.3. 500GB SSD
```

***Although, we are downloading and copying packages and configurations within the /home/lab user directory, it's worth mentioning that I'm using root user access for every single step described here.***

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

Install additinal vMX packages

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
### Download Apstra, Centos GenericCloud and vQFX Images and copy to vmx/images

You will have a directory like that one:

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
65535
change the echo command to: 16384

1 - Start Topology - It will start the entire topoloy (you have to create it first - Option 4)
2 - Stop Topology - It will stop the entire topology
3 - Clean Memory Only - It will clean your server memory
4 - Create Topology - It will create the entire topology from scratch
5 - Delete Topology - It will delete and remove the entire topology and images
```
root@lab:/home/lab/vmx# python3.7 start_stop.py 
1 - Start Topology
2 - Stop Topology
3 - Clean Memory Only
4 - Create topology from Scratch (Make sure you have no topology already running!!You can run option 5 to delete everything - Be careful!!
5 - Delete topology! This option will delete everything, be sure you want to proceed! 
```

## Core vMX R1 and R2 Configuration

r1 - check and apply the core1.conf - core_config folder
r2 - check and apply the core2.conf - core_config folder



# Workaround 

```
If you got an error to start vMX r1 and/or r2 please run the following commands:
./vmx.sh --start --cfg config_apstra/r1-apstra.conf

./vmx.sh --start --cfg config_apstra/r2-apstra.conf
```

## Optional Config - UKSM 

* Although it's totally optional but as you can se below, it likely to improve your server performance as well as enable some additional kernel features. 

```
#memory use before
root@ubuntu:/home/lab/apstra_script# free -g
              total        used        free      shared  buff/cache   available
Mem:            125          77          31           0          17          47
Swap:             0           0           0


#memory use after USKM 
root@ubuntu:/home/lab/apstra_script# free -g
              total        used        free      shared  buff/cache   available
Mem:            125          36          70           0          18          86
Swap:             0           0           0
```

```
apt-get -y install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc gnupg2
apt-get -y --no-install-recommends install kernel-package
```


```
mkdir kernel-4-9-40-source
cd kernel-4-9-40-source
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.9.40.tar.sign
wget https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.9.40.tar.xz

unxz linux-4.9.40.tar.xz
```

```
gpg2 --verify linux-4.9.40.tar.sign 
gpg: assuming signed data in 'linux-4.9.40.tar'
gpg: Signature made Thu 27 Jul 2017 23:08:44 BST using RSA key ID XXXXXXXX <---- You will get another key
gpg: Can't check signature: No public key
```

```
gpg --keyserver hkp://keys.gnupg.net --recv-keys XXXXXXXX
and verify again

gpg --verify linux-4.9.40.tar.sign 
```

```
tar xvf linux-4.9.40.tar
cd linux-4.9.40/
cp /boot/config-4.4.0-186-generic .config
```

```
- edit br_private.h and change from
cat net/bridge/br_private.h | grep BR_GROUPFWD_RESTRICTED
#define BR_GROUPFWD_RESTRICTED     0x0007

- to
cat net/bridge/br_private.h | grep BR_GROUPFWD_RESTRICTED
#define BR_GROUPFWD_RESTRICTED  0x0000u
```
```
copy the uksm patch 4.9 from https://github.com/dolohow/uksm/tree/master/v4.x

apply the patch
patch -p1 < uksm-4-9.patch 
```

This command will generate the kernel .config script 
```
make oldconfig
```
_You will see a few prompots before the UKSM option. In my case was the option 1. 
Make sure you select the right option to enable UKSM and select the default option for everything else_

Compile your new kernel - 14 is the number of my processor core (It will take a while) 
```
Enable KSM for page merging (KSM) [Y/n/?] y
  Choose UKSM/KSM strategy
  > 1. Ultra-KSM for page merging (UKSM) (NEW)
    2. Legacy KSM implementation (KSM_LEGACY) (NEW)
```

```
make -j14 deb-pkg LOCALVERSION=-uksm

# You should see something like that 

root@ubuntu:~/kernel-4-9-40-source/linux-4.9.40# ls -la ../*.deb
-rw-r--r-- 1 root root    957376 Mar 20 11:07 ../linux-firmware-image-4.9.40-uksm_4.9.40-uksm-1_amd64.deb
-rw-r--r-- 1 root root  10546258 Mar 20 11:08 ../linux-headers-4.9.40-uksm_4.9.40-uksm-1_amd64.deb
-rw-r--r-- 1 root root  46015482 Mar 20 11:09 ../linux-image-4.9.40-uksm_4.9.40-uksm-1_amd64.deb
-rw-r--r-- 1 root root 479960848 Mar 20 11:29 ../linux-image-4.9.40-uksm-dbg_4.9.40-uksm-1_amd64.deb
-rw-r--r-- 1 root root    870920 Mar 20 11:08 ../linux-libc-dev_4.9.40-uksm-1_amd64.deb
```

Install the new kernel, update your grub and reboot your system
```
dpkg -i ../linux-headers-4.9.40-uksm_4.9.40-uksm-1_amd64.deb
dpkg -i ../linux-image-4.9.40-uksm_4.9.40-uksm-1_amd64.deb
dpkg -i ../linux-libc-dev_4.9.40-uksm-1_amd64.deb

sudo update-grub

reboot
```

```
uname -r
Linux ubuntu 4.9.40-uksm
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 



See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
