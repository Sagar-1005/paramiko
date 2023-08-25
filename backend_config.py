from paramiko import client
from config import *
import time

def running_config(device):
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
    

