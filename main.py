from lectura_sensores import obtener_lecturas
from time import sleep

while True:
    # Llamar a la función que realiza la lectura de los sensores
    resultado = obtener_lecturas()
    
    # Imprimir el resultado
    print(resultado)
    
    # Pausa entre lecturas
    sleep(2)

