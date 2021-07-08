"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""
import time
import logging
import pexpect

user = "root"
pwd = "juniper123"
pwd_lab = "lab123"
mgmt_interface_vqfx = "em0"
mgmt_interface_vmx = "fxp0"


def config_vqfx(hostname, mgmt_ip):

    print(f"- Configuring {hostname}")
    child = pexpect.spawn(f"virsh console {hostname} --force", timeout=60)
    logging.debug("Got console, Logging in as root")
    child.send("\r")
    child.send("\r")
    child.send("\r")
    child.expect(".*ogin:")
    logging.debug(f"sending user: {user}")
    child.sendline(user)

    child.expect("root@.*")
    child.send("\r")
    child.send("\r")
    child.send("\r")

    logging.debug("Sending cli")
    child.sendline("cli")

    child.expect("root.*>")
    logging.debug("Sending configure")
    child.sendline("edit")
    child.expect("root.*#")

    logging.debug("Setting root authentication")
    child.sendline("set system root-authentication plain-text-password")
    child.expect("New password:")
    logging.debug("sending first password")
    child.sendline(pwd)
    child.expect("Retype new password:")
    child.sendline(pwd)

    logging.debug("Setting lab authentication")
    child.sendline("set system login user lab class super-user authentication plain-text-password")
    child.expect("New password:")
    logging.debug("sending first password")
    child.sendline(pwd_lab)
    child.expect("Retype new password:")
    child.sendline(pwd_lab)

    logging.debug(f"Setting host-name to {hostname}")
    child.sendline(f"set system host-name {hostname}")
    logging.debug("Turning on netconf and ssh")
    child.sendline("set system services netconf ssh")
    child.sendline("set system services ssh")
    child.sendline("delete interfaces")
    time.sleep(.5)
    logging.debug(f"Configuring hostname default to /24 for now!!!")
    child.sendline(f"set interface {mgmt_interface_vqfx} unit 0 family inet address {mgmt_ip}/24")
    logging.debug("Reconfiguring RE PFE Interface em1")
    child.sendline("set interfaces em1 unit 0 family inet address 169.254.0.2/24")
    time.sleep(.5)
    logging.debug("Committing changes")
    child.sendline("commit and-quit")
    child.expect("root.*>", timeout=300)
    time.sleep(1)
    child.sendline("quit")
    time.sleep(1)
    child.sendline("exit")
    child.expect("login:")
    child.sendcontrol("]")
    print(f"- {hostname} configuration completed")


def config_vmx(hostname, mgmt_ip):

    print(f"- Configuring {hostname}")
    child = pexpect.spawn(f"./vmx.sh --console vcp {hostname}", timeout=60)
    logging.debug("Got console, Logging in as root")
    child.send("\r")
    child.send("\r")
    child.send("\r")
    child.expect(".*ogin:")
    logging.debug(f"sending user: {user}")
    child.sendline(user)

    child.expect("root@.*")
    child.send("\r")
    child.send("\r")
    child.send("\r")

    logging.debug("Sending cli")
    child.sendline("cli")

    child.expect("root.*>")
    logging.debug("Sending configure")
    child.sendline("edit")
    child.expect("root.*#")

    logging.debug("Deleting chassis, system and protocols")
    child.sendline("delete chassis auto-image-upgrade")
    child.sendline("delete system processes dhcp-service")
    child.sendline("delete protocols router-advertisement")

    logging.debug("Configuring lite-mode")
    child.sendline("set chassis fpc 0 lite-mode")

    logging.debug("Setting root authentication")
    child.sendline("set system root-authentication plain-text-password")
    child.expect("New password:")
    logging.debug("sending first password")
    child.sendline(pwd)
    child.expect("Retype new password:")
    child.sendline(pwd)

    logging.debug("Setting lab authentication")
    child.sendline("set system login user lab class super-user authentication plain-text-password")
    child.expect("New password:")
    logging.debug("sending first password")
    child.sendline(pwd_lab)
    child.expect("Retype new password:")
    child.sendline(pwd_lab)

    logging.debug(f"Setting host-name to {hostname}")
    child.sendline(f"set system host-name {hostname}")
    logging.debug("Turning on netconf and ssh")
    child.sendline("set system services netconf ssh")
    child.sendline("set system services ssh")
    child.sendline("set system services ssh root-login allow")
    child.sendline("delete interfaces")
    time.sleep(.5)
    logging.debug(f"Configuring hostname default to /24 for now!!!")
    child.sendline(f"set interface {mgmt_interface_vmx} unit 0 family inet address {mgmt_ip}/24")
    logging.debug("Committing changes")
    child.sendline("commit and-quit")
    child.expect("root.*>", timeout=300)
    time.sleep(1)
    child.sendline("quit")
    time.sleep(1)
    child.sendline("exit")
    child.expect("login:")
    child.sendcontrol("]")
    child.expect("telnet>")
    child.sendline("quit")
    print(f"- {hostname} configuration completed")
