# Proyecto_Invernadero_IoT_Cisco_Andina

## Clases

- Cada sensor cuenta con clase y metodos
- La conexion de wifi de la tarjeta esp32 y la publicacion de los datos se manejan por clases
  
## Funcionalidades

- Utilizamos la libreria de uasyncio para controlar la lectura de los sensores y el control del riego automatico
- La publicacion de los datos se realiza mediante mqtt que luego controlamos desde firebase, influxdb, nodered, grafana

# Visualizacion.

- La transformacion de los datos se hace mediante grafana, influxdb, IoT MQTT Panel en su version Android