from http import client
from pyModbusTCP.client import ModbusClient
import json
with open('configuration.json','r') as f:
    data = json.load(f)

adresse_ip = data["serveur"][0]["adresse"]
port = data["serveur"][0]["port"]

client = ModbusClient(adresse_ip,port)
client.open()

regs_l=client.read_holding_registers(data["mot"][0]["adresse"])
print('register  : %s' % regs_l)




regs_2=client.read_coils(data["bit"][1]["adresse"])
print('coil : %s'% regs_2)
