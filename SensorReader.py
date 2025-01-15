import sensores
from time import sleep

def obtener_lecturas():
    """
    Lee los datos de los sensores y devuelve un diccionario con los resultados redondeados.
    """
    resultado_general = {}

    try:
        # Leer datos del sensor DHT22
        dht22_data = sensores.respuesta_dht22(13)
        if 'temperatura_ambiente' in dht22_data:
            dht22_data['temperatura_ambiente'] = round(dht22_data['temperatura_ambiente'], 2)
        if 'humedad_ambiente' in dht22_data:
            dht22_data['humedad_ambiente'] = round(dht22_data['humedad_ambiente'], 2)

        # Leer datos del sensor de humedad del suelo
        capacitor_data = sensores.respuesta_capacitor(35)
        if 'humedad_suelo' in capacitor_data:
            capacitor_data['humedad_suelo'] = round(capacitor_data['humedad_suelo'], 2)

        # Leer datos del sensor BH1750
        bh1750_data = sensores.respuesta_bh1750(22, 21)
        if 'luminosidad' in bh1750_data:
            bh1750_data['luminosidad'] = round(bh1750_data['luminosidad'], 2)

        # Combinar los resultados en un solo diccionario
        resultado_general.update(dht22_data)
        resultado_general.update(capacitor_data)
        resultado_general.update(bh1750_data)

    except Exception as e:
        # Capturar errores y añadirlos al resultado
        resultado_general['error'] = f"Error durante la lectura de sensores: {e}"

    return resultado_general

