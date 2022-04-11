from http import client
from pyModbusTCP.client import ModbusClient
import json
with open('configuration.json','r') as f:
    data = json.load(f)

client = ModbusClient(data["serveur"][0]["adresse"],data["serveur"][0]["port"])
client.open()

regs_l=client.read_holding_registers(data["mot"][2]["adresse"])
print('register  : %s' % regs_l)




regs_2=client.read_coils(data["bit"][1]["adresse"])
print('coil : %s'% regs_2)
