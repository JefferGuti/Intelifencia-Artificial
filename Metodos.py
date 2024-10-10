# Importamos las librerias para la ejecución del algoritmo
import pandas as pd
import random

# Definimos posibles valores para las estaciones
estaciones = ['BOGOTA', 'GIRARDOT', 'MELGAR', 'IBAGUE']
climas = ['soleado', 'lluvioso', 'nublado']
congestion = ['bajo', 'medio', 'alto']
demanda = ['bajo', 'medio', 'alto']
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

# Función para generar una muestra de datos simulados
def generar_dataset(n=1000):
    data = {
        'estacion_origen': [random.choice(estaciones) for _ in range(n)],
        'estacion_destino': [random.choice(estaciones) for _ in range(n)],
        'hora_salida': [f'{random.randint(5, 23)}:{random.randint(0, 59):02d}' for _ in range(n)],
        'tiempo_viaje': [random.randint(10, 120) for _ in range(n)],  # tiempo de viaje entre 10 y 120 minutos
        'clima': [random.choice(climas) for _ in range(n)],
        'nivel_congestion': [random.choice(congestion) for _ in range(n)],
        'demanda_horaria': [random.choice(demanda) for _ in range(n)],
        'dia_semana': [random.choice(dias_semana) for _ in range(n)]
    }
    return pd.DataFrame(data)

# Generar dataset de ejemplo
dataset = generar_dataset(n=1000)

# Guardar el dataset en la ruta especificada
ruta_guardado = r'D:\UserPro\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\transporte_masivo_dataset.csv'
dataset.to_csv(ruta_guardado, index=False)

# Mostrar confirmación de guardado
print(f"Dataset guardado en: {ruta_guardado}")
