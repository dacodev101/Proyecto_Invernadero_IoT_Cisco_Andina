from machine import Pin

class ReleSensor:
    
    def __init__(self, pin:int):
        self.pin = pin
        self._modulo_rele = Pin(pin, Pin.OUT)
        
    def __str__(self):
        return "Rele ubicado en el pin {}".format(self.pin)
    
    def __repr__(self):
        return "ReleSensor(pin='{}')".format(self.pin)
   
    def activar_rele(self):
        try:
            self._modulorele.value(1)
        except OSError as e:
            print("El Relé ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))

    def desactivar_rele(self):
        try:
            self._modulorele.value(0)
        except OSError as e:
            print("El Relé ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))
