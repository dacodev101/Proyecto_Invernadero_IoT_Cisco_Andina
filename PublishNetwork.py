import network
from umqtt.simple import MQTTClient
from random import randint
from json import dumps


class MqttPublisher:
    
    def __init__(self, broker: str, topic: str, client_id: str):
        self.broker = broker
        self.topic = topic
        self.client_id = client_id + str(randint(1, 1000))
        self.client = MQTTClient(client_id, broker)
        
    def __str__(self):
        return "Conexión con Broker {} redireccionando en {} con el cliente {}".format(self.broker, self.topic, self.client_id)
        
    def __repr__(self):
        return "MqttPublisher(broker = {}, topic = {}, client_id = {}=".format(self.broker, self.topic, self.client_id)
    
    def connect(self):
        try:
            self.client.connect()
            print("Conexión MQTT establecida.")
        except Exception as e:
            print("Error al conectar MQTT: {}".format(e))
    
    def publish(self, message: str):
        try:
            self.client.publish(self.topic, message)
        except Exception as e:
            print("Error al publicar {}".format(e))
        
class ConnectWifiCard:
    
    def __init__(self, ssid: str, passw: str):
        self.ssid = ssid
        self.__pass = passw
        
    def __str__(self):
        return "Conexión a la red {}".format(self.ssid)
    
    def __repr__(self):
        return "ConnectWifiCard(ssid ={})".format(self.ssid)
    
    def connect_wifi(self):
        try:
            wlan = network.WLAN(network.STA_IF)
            wlan.active(True)
            wlan.connect(self.ssid, self.__pass)  # Reemplaza con tu SSID y contraseña
            while not wlan.isconnected():
                pass
            print("Conexión Wi-Fi establecida:", wlan.ifconfig())
        except:
            print("Error al publicar: {}".format(e))
            client.disconnect()  # Desconectar después de la publicación
        


# Función para conectar y publicar datos
def publicar_datos(mqtt_publisher: MqttPublisher , data_json: dict):
    try:
        mqtt_publisher.connect()  # Conectar al broker MQTT
        data_json = dumps(str(data_json))
        mqtt_publisher.publish(data_json)  # Conectar al broker MQTT
    except Exception as e:
        print("Error al publicar {}".format(e))

if __name__ == "__main__":
    
    # Conexion a Wifi
    #wifi = ConnectWifiCard('MASTV-VOLLBASK', 'Falcons2023')
    #wifi.connect_wifi()
    
    # Configuración del broker MQTT
    # Cliente MQTT  
    
    mqtt = MqttPublisher("broker.hivemq.com", "agrosmart/servicio/monitoreo", "esp32_client0001")
    publicar_datos(mqtt, {"temperatura": 23, "humedad": 60})

    print(mqtt)

