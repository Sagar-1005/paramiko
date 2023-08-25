from paramiko import client
from config import *
import time
import paramiko
paramiko.util.log_to_file('paramiko.log',level='DEBUG')

def running_invoke_shell_config(device):
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=device,
                       port=PORT,
                       username=USERNANE,
                       password=PASSWORD,
                       look_for_keys=False, allow_agent=False)
    device_connection=ssh_client.invoke_shell()
    device_connection.send('sh run \n')
    time.sleep(15)
    output=device_connection.recv(65535)   
    print(output.decode())
    

def running_exec_command(device):
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(hostname=device,
                       port=PORT,
                       username=USERNANE,
                       password=PASSWORD,
                       look_for_keys=False,allow_agent=False)
    stdin,stdout,stderr=ssh_client.exec_command('show run')
    print(stdout.read().decode())
    print(stderr.read().decode())

def ssh_exec_command(device):
    # try:
        ssh_client=client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(hostname=device,
                           port=PORT,
                           username=USERNANE,
                           look_for_keys=True,allow_agent=True,disabled_algorithms=dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256']))
        stdin,stdout,stderr=ssh_client.exec_command('sh run')
        print(stdout.read().decode())
    # except:
        # print('Not connected')