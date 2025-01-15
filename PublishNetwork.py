import network
from umqtt.simple import MQTTClient

class MqttPublisher:
    
    def __init__(self, broker: str, topic: str, client_id: str):
        self.broker = broker
        self.topic = topic
        self.client_id = client_id
        self.client = MQTTClient(client_id, broker)
        
    def __str__(self):
        return "Conexión con Broker {} redireccionando en {}".format(self.broker, self.topic)
        
    def __repr__(self):
        return "MqttPublisher(broker = {}, topic = {}, client_id = {}=".format(self.broker, self.topic, self.client_id)
    

# Configura la conexión Wi-Fi
def conectar_wifi(name_red: str, pass_red: str):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(name_red, pass_red)  # Reemplaza con tu SSID y contraseña
    while not wlan.isconnected():
        pass
    print("Conexión Wi-Fi establecida:", wlan.ifconfig())

# Configuración del broker MQTT
MQTT_BROKER = "broker.hivemq.com"
MQTT_TOPIC = "agrosmart/servicio/monitoreo"
CLIENT_ID = "esp32_client0001"  # ID del cliente MQTT

# Crear el cliente MQTT
client = MQTTClient(CLIENT_ID, MQTT_BROKER)

# Función para conectar y publicar datos
def publicar_datos(datos_json: dict):
    try:
        client.connect()  # Conectar al broker MQTT
        client.publish(MQTT_TOPIC, str(datos_json))  # Publicar el mensaje
        print(f"Publicado: {datos_json}")
        
    except Exception as e:
        print("Error al publicar:", e)
        client.disconnect()  # Desconectar después de la publicación

