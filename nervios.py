# Programa para generar secuencias de encendido/apagado de leds WS2812 de acuerdo
# a la detección de presionado de teclado normalmente abiertos
import time
import machine, neopixel
from machine import Pin
from time import sleep

# Tabla con la definición de pines utilizadas como entradas 
#tblpin=[15,4,16]
tblpin=[17,5,19]

#Configuracion de pines de entrada
tblkey=[]
for key in tblpin:
    tblkey.append(Pin(key, Pin.IN,Pin.PULL_UP))
print(tblkey)

# Tabla para almacenar estados de los pulsantes
tblstaant=[]
for i in tblpin:
    tblstaant.append(0)
print(tblstaant)

# Configuracion tira leds
NUMPIX=20  #NUMERO DE PIXELS
DATA=13  #PIN UTILIZADO EN EL ESP32
np = neopixel.NeoPixel(machine.Pin(DATA), NUMPIX)

def demo(np):
    n = np.n
    # cycle
    print("cycle")
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(120)

print("Test Leds")
demo(np)        

print("Main")
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

