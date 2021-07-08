"""
---------------------------------
 Author: Gilberto Rampini
 Date: 06/2021
---------------------------------
"""

import create_lab
import subprocess
import pexpect
import logging
import time

user = "root"
password = "juniper123"


def copy_file_vmx_router():

   vmx_hosts = create_lab.create_vmx_dic()

   for i in vmx_hosts.keys():

      hostname = vmx_hosts[i].get('hostname')
      ip = vmx_hosts[i].get('mgmt_ip')

      print(f"- Sending configuration file to {hostname}")

      try:
         ssh_keyscan = f'ssh-keyscan -H {ip} >> ~/.ssh/known_hosts'
         subprocess.call(ssh_keyscan, shell=True)

         child = pexpect.spawn("scp core_config/{hostname} {user}@{ip}:".format(ip=ip, hostname=hostname, user=user))
         child.expect("Password:")
         child.sendline(password)
         child.read()
      except:
         print("something went wrong during the file copy")

      try:
         print(f"- Additional configuration - {hostname}")
         child = pexpect.spawn(f"./vmx.sh --console vcp {hostname}", timeout=60)
         logging.debug("Got console, Logging in as root")
         child.send("\r")
         child.send("\r")
         child.send("\r")
         child.expect(".*ogin:")
         logging.debug(f"sending user: {user}")
         child.sendline(user)
         child.expect("Password:")
         child.sendline(password)

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
         logging.debug("load file")
         child.sendline("load set {hostname}".format(hostname=hostname))
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
      except:
         print(f"problem to load the configuration {hostname}")


if __name__ == "__main__":
   copy_file_vmx_router()
