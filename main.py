from lectura_sensores import obtener_lecturas
import publicacion
from time import sleep

publicacion.conectar_wifi('name_red', 'pass_red')


while True:
    # Llamar a la función que realiza la lectura de los sensores
    resultado = obtener_lecturas()
    
    # Imprimir el resultado
    publicacion.publicar_datos(resultado)
    
    # Pausa entre lecturas
    sleep(2)

