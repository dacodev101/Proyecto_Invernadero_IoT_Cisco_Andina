from machine import Pin, ADC, I2C, SoftI2C
from dht import DHT22
from bh1750 import BH1750

def porcentaje_humedad_suelo(valor_sensor, valor_humedad, valor_sequedad):
    resultado = max(0, min(100, (valor_sensor - valor_sequedad) * 100 / (valor_humedad - valor_sequedad)))
    return resultado      

def respuesta_dht22(pin_sensor: int):
    resultado = {}
    try:
        sensor = DHT22(Pin(pin_sensor))
        sensor.measure()
        tem = sensor.temperature()
        hum = sensor.humidity()
        resultado['temperatura_ambiente'] = tem
        resultado['humedad_ambiente'] = hum
        return resultado
    except OSError as e:
        print("El sensor {} tiene el siguiente error {e}".format(sensor, e))
        resultado['error_dht22'] = e
        return resultado

def respuesta_capacitor(pin_sensor, valor_seco=2550, valor_humedo=995):
    # Configurar la atenuación del ADC a 11dB para el rango completo

    resultado = {}
    try:
        humedad = valor_humedo
        sequedad = valor_seco
        moisture = ADC(Pin(pin_sensor, Pin.IN))
        moisture.atten(moisture.ATTN_11DB)
        lectura = moisture.read()
        porcentaje = porcentaje_humedad_suelo(lectura, humedad, sequedad)
        resultado['humedad_suelo'] = porcentaje
        return resultado
    except OSError as e:
        print("El sensor Capacitor tiene el siguiente error {e}".format(moisture, e))
        resultado['error_capacitor'] = e
        return resultado

def respuesta_bh1750(pin_scl: int, pin_sda: int):
    # Configurar la atenuación del ADC a 11dB para el rango completo
    resultado = {}
    try:
        i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
        light_sensor = BH1750(bus=i2c, addr=0x23)
        luminosidad = light_sensor.luminance(BH1750.CONT_HIRES_1)
        resultado['luminosidad'] = luminosidad
        return resultado
    except OSError as e:
        print("El sensor bh1750 tiene el siguiente error {}".format(e))
        resultado['Error'] = e
        return resultado
