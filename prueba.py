import joblib
import pandas as pd

# 1. Cargamos el modelo guardado
ruta_modelo = r'D:\User0\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\modelo_transporte_masivo.pkl'
modelo_cargado = joblib.load(ruta_modelo)

# 2. Creamos un nuevo conjunto de datos para predecir
# Debemos asegurarnos de que los datos que coincidan para entrenar el modelo

# CIUDAD->              Bogota =0,  Girardot =1, Melgar =2, Ibague =3
# HORA SALIDA ->        valor numérico representando la hora del día en minutos
# CLIMA ->              Soleado = 0, Nublado = 1, Lluvioso = 2, Tormenta = 3
# DEMANDA HORARIA ->    Bajo = 0, Medio = 1, Alto = 2
# DIA DE LA SEMANA ->   Lunes = 0, Martes = 1, Miércoles = 2, Jueves = 3, Viernes = 4, Sábado = 5, Domingo = 6


nuevos_datos = pd.DataFrame({
    'estacion_origen': [0],  # BOGOTA
    'estacion_destino': [3],  # IBAGUE
    'hora_salida': [750],  # Hora en minutos, 12:30 en este caso
    'clima': [0],  # Soleado
    'nivel_congestion': [1],  # Medio
    'demanda_horaria': [2],  # Alto
    'dia_semana': [1]  # Martes
})

# 3. Hacer predicciones
predicciones = modelo_cargado.predict(nuevos_datos)


# 4. Mostrar la predicción en pantalla
print (f'\n La predicción del tiempo de viaje es de:  {predicciones[0]:.2f} minutos')
