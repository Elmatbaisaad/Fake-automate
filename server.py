from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform
import json

with open('configuration.json','r') as f:
    data = json.load(f)

def initialiser_adresse_register(a,x):
    a= [data["mot"][x]["adresse"]]
    return a
def initialiser_adresse_coil(a,x):
    a= [data["bit"][x]["adresse"]]
    return a

def acceder_adresse_register(x):
    return data["mot"][x]["adresse"]
def acceder_adresse_coil(x):
    return data["bit"][x]["adresse"]

def acceder_valeur_register(x):
    return data["mot"][x]["valeur"]
def acceder_valeur_coil(x):
    return data["bit"][x]["valeur"]



server = ModbusServer(data["serveur"][0]["adresse"],data["serveur"][0]["port"],no_block=True)
adresse_register = None
adresse_coil = None

try:
    print("Start server")
    server.start()
    print("Server is online")
    for i in range  (len(data["mot"])):
        
    #state = [data["mot"][1]["adresse"]]
        initialiser_adresse_register(adresse_register,i)
        DataBank.set_words(acceder_adresse_register(i),[acceder_valeur_register(i)])
        
    for i in range  (len(data["bit"])):
    #coil = [data["bit"][0]["adresse"]]
        initialiser_adresse_coil(adresse_coil,i)
        DataBank.set_bits(acceder_adresse_coil(i),[str(acceder_valeur_coil(i))])
    
    while True:
        continue
        
        
        
        
except:
    print("shutdown server")
    server.stop
    print("server offline")





























# server = ModbusServer("127.0.0.1",12345,no_block=True)

# try:
#     print("Start server")
#     server.start()
#     print("Server is online")
#     state = [0]
#     coil = [1]
#     while True:
#         DataBank.set_words(0,[3])
#         DataBank.set_bits(1,[str(True)])
# except:
#     print("shutdown server")
#     server.stop
#     print("server offline")