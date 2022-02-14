#Asignar turno para ver el super bowl

import threading
import time


class SuperBowl():
    def __init__(self, turno = 0):
        self.locked = threading.Lock()
        self.tur_send = turno

    def turno(self):
        self.locked.acquire()
        try:
            self.tur_send += 1
            
            print('Turno: ', self.tur_send)
            print('Esperar 5 minutos')
            time.sleep(5)
        finally:
            self.locked.release()

def solicitar_turno(x):
    for i in range(5):
        x.turno()

if __name__ == '__main__':
    bowl = SuperBowl()
    print('---Super Bowl ----')
    for i in range(2):
        tstart = threading.Thread(target=solicitar_turno, args=(bowl,))
        tstart.start()