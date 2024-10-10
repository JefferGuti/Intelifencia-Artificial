import pandas as pd #Instalamos paquetes
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import joblib  # Para guardar el modelo entrenado

# Definimos posibles valores para cada columna
estaciones = ['BOGOTA', 'GIRARDOT', 'MELGAR', 'IBAGUE']
climas = ['soleado', 'lluvioso', 'nublado']
congestion = ['bajo', 'medio', 'alto']
demanda = ['bajo', 'medio', 'alto']
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']

# es la función para generar una muestra de datos simulados
def generar_dataset(n=1000):
    data = {
        'estacion_origen': [random.choice(estaciones) for _ in range(n)],
        'estacion_destino': [random.choice(estaciones) for _ in range(n)],
        'hora_salida': [f'{random.randint(5, 23)}:{random.randint(0, 59):02d}' for _ in range(n)],
        'tiempo_viaje': [random.randint(10, 60) for _ in range(n)],
        'clima': [random.choice(climas) for _ in range(n)],
        'nivel_congestion': [random.choice(congestion) for _ in range(n)],
        'demanda_horaria': [random.choice(demanda) for _ in range(n)],
        'dia_semana': [random.choice(dias_semana) for _ in range(n)]
    }
    return pd.DataFrame(data)

# 1. Generamos el dataset simulado
dataset = generar_dataset(n=1000)

# 2. Convertir 'hora_salida' a minutos
dataset['hora_salida'] = dataset['hora_salida'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

# 3. Preprocesar las variables categóricas
le = LabelEncoder()
for col in ['estacion_origen', 'estacion_destino', 'clima', 'nivel_congestion', 'demanda_horaria', 'dia_semana']:
    dataset[col] = le.fit_transform(dataset[col])

# 4. Separar variables predictoras (X) y variable objetivo (y)
X = dataset.drop(columns=['tiempo_viaje'])
y = dataset['tiempo_viaje']

# 5. Dividir los datos en conjunto de entrenamiento (80%) y de prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 7. Hacer predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# 8. Evaluar el modelo con el error cuadrático medio (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Error cuadrático medio (MSE): {mse}')

# 9. Guardar algunos resultados de predicción
for i in range(5):
    print(f'Predicción: {y_pred[i]:.2f}, Real: {y_test.iloc[i]}')

# 10. Guardar el modelo entrenado en la carpeta especificada
ruta_modelo = r'D:\User0\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\modelo_transporte_masivo.pkl'
joblib.dump(modelo, ruta_modelo)

print(f'Modelo guardado en: {ruta_modelo}')
