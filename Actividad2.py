class SistemaTransporte:
    def __init__(self):
        self.estaciones = {}  # Diccionario que contiene las estaciones y sus conexiones
    
    def agregar_estacion(self, nombre):
        self.estaciones[nombre] = []
    
    def agregar_conexion(self, origen, destino, tiempo):
        self.estaciones[origen].append((destino, tiempo))
        self.estaciones[destino].append((origen, tiempo))  # Conexión bidireccional
    
    def encontrar_ruta(self, inicio, destino):
        visitados = set()  # Conjunto de estaciones visitadas
        cola = [(inicio, [inicio], 0)]  # (Estación actual, ruta hasta ahora, tiempo acumulado)
        
        while cola:
            (actual, ruta, tiempo_actual) = cola.pop(0)
            
            if actual in visitados:
                continue
            
            if actual == destino:
                return ruta, tiempo_actual  # Se encontró la ruta
            
            visitados.add(actual)
            
            for (vecino, tiempo) in self.estaciones[actual]:
                if vecino not in visitados:
                    cola.append((vecino, ruta + [vecino], tiempo_actual + tiempo))
        
        return None, float('inf')  # No se encontró una ruta

# Base de conocimiento: estaciones y tiempos de trayecto
sistema = SistemaTransporte()
sistema.agregar_estacion("BOGOTA")
sistema.agregar_estacion("GIRARDOT")
sistema.agregar_estacion("MELGAR")
sistema.agregar_estacion("IBAGUE")

# Conexiones entre estaciones (origen, destino, tiempo)
sistema.agregar_conexion("BOGOTA", "GIRARDOT", 10)
sistema.agregar_conexion("BOGOTA", "MELGAR", 15)
sistema.agregar_conexion("GIRARDOT", "IBAGUE", 20)
sistema.agregar_conexion("MELGAR", "IBAGUE", 10)

# Encontrar la mejor ruta desde A hasta D
ruta, tiempo = sistema.encontrar_ruta("BOGOTA", "IBAGUE")

if ruta:
    print(f"Mejor ruta: {' -> '.join(ruta)}, Tiempo total: {tiempo} minutos")
else:
    print("No se encontró una ruta.")