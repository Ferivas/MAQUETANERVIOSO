# Programa para generar secuencias de encendido/apagado de leds WS2812 de acuerdo
# a la detección de presionado de teclado normalmente abiertos
import time
import machine, neopixel
from machine import Pin
from time import sleep

# Tabla con la definición de pines utilizadas como entradas 
#tblpin=[15,4,16]
tblpin=[15,4,16,17,5,18,19 ]
tblname=["cerebro","pulmones","corazon","estomago",
         "ap. urinario","riñones","higado"]
tblcolor=[(255,255,255),(255,255,0),(255,0,0),(255,0,255),
          (0,255,255),(255,255,255),(0,255,0)]
tblsec=[[0],[0,1,2,3,4,5,6,22,24,23,21],[0,1,2,3,4,5,6,7],[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],
        [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[0,1,2,3,4,5,6,7,8,9,10,11,19,18],[0,1,2,3,4,5,6,7,8,9,10,11,20]]

tblneurona=[25,26,27,28,29,30]

tblorgano=[0,21,7,14,17,18,20]

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
NUMPIX=31  #NUMERO DE PIXELS
DATA=13  #PIN UTILIZADO EN EL ESP32
np = neopixel.NeoPixel(machine.Pin(DATA), NUMPIX)

def demo(np):
    n = np.n
    # cycle
    print("cycle")
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 5)
        np.write()
        time.sleep_ms(40)
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
    
def clear(np):
    n=np.n
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()    
    

print("Test Leds")
demo(np)        

print("Main Nervioso")
ptrneurona=0
cntrt=0
while True:
    cntr=0
    for kin in tblkey:
        if kin.value()==0:
            if kin.value()!=tblstaant[cntr]:
                #print("K",cntr,"=0")
                tblstaant[cntr]=kin.value()
                print(tblname[cntr])
                clear(np)
                if cntr==0: #corazon
                    print("fade corazon")
                    for i in range(0, 8 * 256, 8):
                        if (i // 256) % 2 == 0:
                            val = i & 0xff
                        else:
                            val = 255 - (i & 0xff)
                        time.sleep_ms(2)
                        np[0] = (val, val, 0)
                            
                        np.write()
                    clear(np)
                else: # efectos secuencia
                    print(tblsec[cntr])
                    n1=len(tblsec[cntr])
                    print("len=",n1)
                    ptrsec=0
                    for i in range(2 * n1):
                        for j in tblsec[cntr]:
                            np[j] = (0, 0, 0)
                        #np[i % n1] = tblcolor[cntr]
                        datatbl=tblsec[cntr]
                        data=datatbl[ptrsec]
                        #print("I>",data)
                        np[data] = tblcolor[cntr]
                        ptrsec=ptrsec+1
                        ptrsec=ptrsec%n1
                        np.write()
                        time.sleep_ms(120)
                    clear(np)
                    print("Fade organo")
                    for i in range(0, 8 * 256, 8):
                        if (i // 256) % 2 == 0:
                            val = i & 0xff
                        else:
                            val = 255 - (i & 0xff)
                        time.sleep_ms(2)
                        organo=tblorgano[cntr]
                        if cntr==1:
                            np[organo] = (val, val, 0)
                            np[23]=(val, val, 0)
                        else:
                            np[organo] = (val, val, 0)
                        np.write()
                    clear(np)                        
                    
                    
                    
        else:
            if kin.value()!=tblstaant[cntr]:
                #print("K",cntr,"=1")
                tblstaant[cntr]=kin.value()
        cntr=cntr+1
        
    sleep(0.1)
    cntrt=cntrt+1
    t1=cntrt%2
    if t1==0:
        for j in tblneurona:
            np[j] = (0, 0, 0)
        if ptrneurona<6:
            np[tblneurona[ptrneurona]]=(55,155,255)
        np.write()
        ptrneurona=ptrneurona+1
        ptrneurona=ptrneurona%7
        if ptrneurona==0:
            clear(np)
    
