import time
import machine, neopixel
#n=120
NUMPIX=30  #NUMERO DE PIXELS
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

    # bounce
    print("bounce b")
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(120)
        
    print("bounce g")
    for i in range(2 * n):
        for j in range(n):
            np[j] = (0, 128, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(120)        

    print("bounce r")
    for i in range(2 * n):
        for j in range(n):
            np[j] = (128, 0, 0)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(120)
    # fade in/out
    print("fade R")
    for i in range(0, 8 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    print("fade g")
    for i in range(0, 8 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, val, 0)yu+-
            
        np.write()
        
    print("fade b")
    for i in range(0, 8 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (0, 0, val)
        np.write()        
    # clear
    print("clear")
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
demo(np)    
