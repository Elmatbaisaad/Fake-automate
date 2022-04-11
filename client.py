from http import client
from pyModbusTCP.client import ModbusClient
import json
with open('configuration.json','r') as f:
    data = json.load(f)

def adresse_register(x):
    return data["mot"][x]["adresse"]
def adresse_coil(x):
    return data["bit"][x]["adresse"]




adresse_ip = data["serveur"][0]["adresse"]
port = data["serveur"][0]["port"]

client = ModbusClient(adresse_ip,port)
client.open()

regs_l=client.read_holding_registers(adresse_register(0))
print('register  : %s' % regs_l)



regs_2=client.read_coils(adresse_coil(1))
print('coil : %s'% regs_2)
