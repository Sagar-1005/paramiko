import webbrowser
import difflib
import time
from paramiko import client, RSAKey
from config import *

# import paramiko
# paramiko.util.log_to_file('paramiko.log',level='DEBUG')


def running_invoke_shell_config(device):
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(
        hostname=device,
        port=PORT,
        username=USERNANE,
        password=PASSWORD,
        look_for_keys=False,
        allow_agent=False,
    )
    device_connection = ssh_client.invoke_shell()
    device_connection.send("terminal len 0\n")
    device_connection.send("sh run \n")
    time.sleep(30)
    output = device_connection.recv(65535)
    with open("previous_backup.txt", "a") as file:
        file.write(output.decode())
    print(output.decode())


def running_exec_command(device):
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect(
        hostname=device,
        port=PORT,
        username=USERNANE,
        password=PASSWORD,
        look_for_keys=False,
        allow_agent=False,
    )
    stdin, stdout, stderr = ssh_client.exec_command("show run")
    print(stdout.read().decode())
    print(stderr.read().decode())


def ssh_exec_command(device):
    key_file = RSAKey.from_private_key_file(filename=FILE_NAME)
    try:
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
        ssh_client.connect(
            hostname=device,
            port=PORT,
            username=USERNANE,
            pkey=key_file,
            look_for_keys=True,
            allow_agent=True,
            disabled_algorithms=dict(pubkeys=["rsa-sha2-512", "rsa-sha2-256"]),
        )
        stdin, stdout, stderr = ssh_client.exec_command("sh run")
        print(stdout.read().decode())
    except:
        print("Not connected")


def config_compare(comp_with, comp_to, html_normal):
    if html_normal == "normal":
        with open(comp_with) as file:
            previous_config = file.read()
        with open(comp_to) as file:
            new_config = file.read()
        delta = difflib.Differ().compare(
            previous_config.splitlines(), new_config.splitlines()
        )
        print(delta)
        for data in delta:
            print(data)
    elif html_normal == "html":
        with open(comp_with) as file:
            previous_config = file.readlines()
        with open(comp_to) as file:
            new_config = file.readlines()
        config_compare = difflib.HtmlDiff().make_file(
            fromlines=previous_config,
            tolines=new_config,
            fromdesc="previous_config",
            todesc="newconfig",
        )
        with open("diff.html", "w") as file:
            file.write(config_compare)
        webbrowser.open_new_tab("diff.html")
