from paramiko import client
import time

host='192.168.188.131'
username='admin'
password='cisco'

ssh_clint=client.SSHClient()
ssh_clint.set_missing_host_key_policy(client.AutoAddPolicy())

ssh_clint.connect(hostname=host,
                  port=22,
                  username=username,
                  password=password,
                  look_for_keys=False,allow_agent=False)

device_connection=ssh_clint.invoke_shell()
device_connection.send('sh ip int bri\n')
time.sleep(10)
output=device_connection.recv(65535)
print(output.decode())

