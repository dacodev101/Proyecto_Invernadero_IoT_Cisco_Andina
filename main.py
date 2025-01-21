import Sincronizacion  as sc
import uasyncio as asyncio

# Iniciar el bucle de eventos
try:
    asyncio.run(sc.main())
except KeyboardInterrupt:
    print("Interrupción detectada, deteniendo el programa.")
    sc.desactivarRele()