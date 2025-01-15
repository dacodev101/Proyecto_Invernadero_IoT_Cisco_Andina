import SensorManager as sm
import PublishNetwork as pn
from time import sleep

# Creacion del administrador de sensores

sensor_admin = sm.SensorManager()

# Creacion de las instancias de los sensores y registrarlos en el administrador de sensores

sm.registrar_sensor(sm.DHT22Sensor(13))
sm.registrar_sensor(sm.CapacitorSensor(35))
sm.registrar_sensor(sm.BH1750Sensor(22, 21))
sm.registrar_sensor(sm.ReleSensor(16))

# Conectar a wifi

conexion_wifi = pn.ConnectWifiCard('MASTV-VOLLBASK', 'Falcons2023')
conexion_wifi.connect_wifi()

# Crear cliente de MQTT

mqtt_client = pn.MqttPublisher("broker.hivemq.com", "agrosmart/servicio/monitoreo", "esp32_client")


while True:
    # Llamar a la función que realiza la lectura de los sensores
    resultado = sensor_admin.obtener_lecturas()
    
    # Imprimir el resultado
    print(resultado)
    
    #Publicar resultados
    
    pn.publicar_datos(mqtt_client, resultado)
    
    # Pausa entre lecturas
    sleep(3)

