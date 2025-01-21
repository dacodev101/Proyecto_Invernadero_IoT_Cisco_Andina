import uasyncio as asyncio
import SensorManager as sm
import PublishNetwork as pn
import Activadores as ac
from time import sleep
import utime
import ujson  # Para serializar los datos

# Configurar sensores
sensor_admin = sm.SensorManager()

dht22_sensor = sm.DHT22Sensor(2)
capacitor_sensor = sm.CapacitorSensor(35)
bh1750_sensor = sm.BH1750Sensor(22, 21)
rele_mod1 = ac.ReleSensor(16)

sensor_admin.registrar_sensor(dht22_sensor)
sensor_admin.registrar_sensor(capacitor_sensor)
sensor_admin.registrar_sensor(bh1750_sensor)

# Configurar MQTT
mqtt_client = pn.MqttPublisher("broker.hivemq.com", "agrosmart/servicio/monitoreo", "esp32_client")

# Variable global para almacenar los datos de los sensores
sensor_data = {}
last_read_time = utime.ticks_ms()

async def leer_sensores():
    """Lee sensores y publica datos cada 30 minutos."""
    global sensor_data, last_read_time
    while True:
        try:
            # Leer los datos de todos los sensores
            sensor_data = sensor_admin.obtener_lecturas()
            print(f"Datos obtenidos: {sensor_data}")
            
            # Conectar a Wi-Fi
            conexion_wifi = pn.ConnectWifiCard('MASTV-VOLLBASK', 'Falcons2023')
            conexion_wifi.connect_wifi()
            
            sleep(10)  # Tiempo para establecer conexión Wi-Fi
            
            # Publicar datos en MQTT
            mqtt_client.connect()
            mqtt_client.publish(ujson.dumps(sensor_data))  # Convertir a JSON
            
            # Actualizar el tiempo de la última lectura
            last_read_time = utime.ticks_ms()
        except Exception as e:
            print(f"Error en lectura de sensores: {e}")
        
        # Esperar 30 minutos para la próxima lectura
        await asyncio.sleep(60 * 30)

async def controlar_rele():
    """Activa/desactiva el relé 3 minutos después de la última lectura y verifica continuamente la humedad."""
    while True:
        try:
            # Leer humedad del suelo directamente del sensor
            lectura_capacitor = capacitor_sensor.leer()  # Suponiendo que devuelve un diccionario
            humedad_suelo = lectura_capacitor.get('humedad_suelo', 100)  # Extraer el valor específico
            
            # Asegurarse de que han pasado 3 minutos desde la última lectura general
            if utime.ticks_diff(utime.ticks_ms(), last_read_time) >= 20 * 1000:
                if humedad_suelo < 30:  # Condición para activar el relé
                    print("Humedad baja, activando relé...")
                    rele_mod1.activar_rele()
                else:
                    print("Humedad adecuada, desactivando relé...")
                    rele_mod1.desactivar_rele()
            else:
                print("Aún no han pasado 3 minutos desde la última lectura general.")
        except Exception as e:
            print(f"Error en control del relé: {e}")
        
        # Revisar cada minuto si es necesario actuar
        await asyncio.sleep(60)

async def main():
    """Ejecuta tareas concurrentes."""
    # Asegurar que el relé comienza apagado
    rele_mod1.desactivar_rele()
    await asyncio.gather(leer_sensores(), controlar_rele())

def desactivarRele():
    rele_mod1.desactivar_rele()