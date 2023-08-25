from paramiko import client
from getpass import getpass
import time

host='192.168.188.131'
username=input('Enter username')
if not username:
    username='admin'

password=getpass(f'Enter password {username}') or 'cisco'

print(password)

ssh_client=client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())

ssh_client.connect(hostname=host,
                   port=22,
                   username=username,
                   password=password,
                   look_for_keys=False,allow_agent=False)

print(dir(ssh_client))
print('connected successfully')
device_access=ssh_client.invoke_shell()
device_access.send('terminal length 0\n')
device_access.send('show run\n')
time.sleep(10)
output=device_access.recv(65535)
print(output.decode())
ssh_client.close()
