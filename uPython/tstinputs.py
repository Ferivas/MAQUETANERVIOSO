# Programa para ler varios pines de entrada como una tabla
# Para el DevKit2 el pin2 no funciona porque ahi se tiene
# conectado el led de la tarjeta 
from machine import Pin
from time import sleep

print("Test Inputs")

#tblpin=[15,4,16]
tblpin=[17,5,19]
tblkey=[]

for key in tblpin:
    tblkey.append(Pin(key, Pin.IN,Pin.PULL_UP))

print(tblkey)

tblstaant=[]
for i in tblpin:
    tblstaant.append(0)

print(tblstaant)

while True:
    cntr=0
    for kin in tblkey:
        if kin.value()==0:
            if kin.value()!=tblstaant[cntr]:
                print("K",cntr,"=0")
                tblstaant[cntr]=kin.value()
        else:
            if kin.value()!=tblstaant[cntr]:
                print("K",cntr,"=1")
                tblstaant[cntr]=kin.value()
        cntr=cntr+1
        
    sleep(0.1)