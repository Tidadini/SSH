from netmiko import Netmiko
from getpass import getpass

password = getpass()

cisco1 = {
    "host": "192.168.42.219",
    "username": "fouzi",
    "password": password,
    "device_type": "cisco_ios",
}
cisco2 = {
    "host": "192.168.42.94",
    "username": "fouzi",
    "password": password,
    "device_type": "cisco_ios",
}
for device in (cisco1, cisco2):
    net_connect = Netmiko(**device)
    print(net_connect.find_prompt())
    output = net_connect.send_command('show ip int brief')
    print(output)
    
