
from netmiko import ConnectHandler

device_details = {
    "ip": "192.168.188.131",
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "cisco",
}

connetion = ConnectHandler(**device_details)

print(connetion)
