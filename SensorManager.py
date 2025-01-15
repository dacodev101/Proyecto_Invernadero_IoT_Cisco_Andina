from machine import Pin, ADC, I2C, SoftI2C
from dht import DHT22
from bh1750 import BH1750

# Definicíon de Clase por sensor

class DHT22Sensor:
    
    def __init__(self, pin: int):
        self.pin = pin
    
    def __str__(self):
        return "Sensor DHT22 ubicado en el pin {}".format(self.pin)
    
    def __repr__(self):
        return "DHT22Sensor(pin='{}')".format(self.pin)
        
    def leer(self):
        try:
            modulo = DHT22(Pin(self.pin))
            modulo.measure()
            tem = modulo.temperature()
            hum = modulo.humidity()
            return {'temperatura': tem, 'humedad': hum}
        except OSError as e:
            print("El sensor ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))

class CapacitorSensor:
    
    def __init__(self, pin: int, seco: int = 2550, humedo: int = 995):
        self.pin = pin
        self.seco = seco
        self.humedo = humedo
    
    def __str__(self):
        return "Sensor Capacitor humedad suelo, ubicado en el pin {}, con valores (seco={}, humedo={})".format(self.pin, self.seco, self.humedo)
    
    def __repr__(self):
        return "CapacitorSensor(pin='{}', seco={}, humedo{})".format(self.pin, self.seco, self.humedo)
    
    def __porcentaje_humedad(self, lectura: float) -> float:
        resultado = max(0, min(100, (lectura - self.seco) * 100 / (self.seco - self.humedo)))
        return resultado
    
    def leer(self):
        try:
            moisture = ADC(Pin(self.pin, Pin.IN))
            moisture.atten(moisture.ATTN_11DB)
            lectura = moisture.read()
            porcentaje = self.__porcentaje_humedad(lectura)
            return {'humedad_suelo': porcentaje}
        except OSError as e:
            print("El sensor ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))


class BH1750Sensor:
    
    def __init__(self, pin_scl: int, pin_sda: int):
        self.pin_scl = pin_scl
        self.pin_sda = pin_sda
        
    def __str__(self):
        return "Sensor de Luminocidad BH1750, ubicado en los pines scl {} - sda {})".format(self.pin_scl, self.pin_sda)
    
    def __repr__(self):
        return "BH1750Sensor(pin scl='{}', pin sda={})".format(self.pin_scl, self.pin_sda)

    def leer(self):
        try:
            i2c = SoftI2C(scl=Pin(self.pin_scl), sda=Pin(self.pin_sda))
            light_sensor = BH1750(bus=i2c, addr=0x23)
            luminosidad = light_sensor.luminance(BH1750.CONT_HIRES_1)
            return {'luminosidad': luminosidad}
        except OSError as e:
            print("El sensor bh1750 ubicado en los pines scl {} - sda {} tiene el siguiente error {}".format(self.pin_scl, self.pin_sda, e))

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
            self._modulorele.on()
        except OSError as e:
            print("El Relé ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))

    def desactivar_rele(self):
        try:
            self._modulorele.off()
        except OSError as e:
            print("El Relé ubicado en el pin {} tiene el siguiente error {}".format(self.pin, e))