# Importamos las librerías
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib

# Cargamos el dataset anteriormente generado
ruta_dataset = r'D:\User0\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\transporte_masivo_dataset.csv'

dataset = pd.read_csv(ruta_dataset)

# Convertirmos hora de salida a minutos para que sea numérico
dataset['hora_salida'] = dataset['hora_salida'].apply(lambda x: int(x.split(':')[0]) * 60 + int(x.split(':')[1]))

# Preprocesamos las variables categóricas
le = LabelEncoder()
for col in ['estacion_origen', 'estacion_destino', 'clima', 'nivel_congestion', 'demanda_horaria', 'dia_semana']:
    dataset[col] = le.fit_transform(dataset[col])

# Escalar los datos para mejorar el rendimiento de KMeans
scaler = StandardScaler()
dataset_scaled = scaler.fit_transform(dataset)

# Aplicar KMeans con un número de clusters (por ejemplo, 4 grupos)
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(dataset_scaled)

# Obtener los clusters asignados para cada registro
dataset['cluster'] = kmeans.labels_

# Guardar el modelo entrenado
ruta_modelo = r'D:\User0\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\modelo_kmeans_transporte.pkl'
joblib.dump(kmeans, ruta_modelo)

print(f'Modelo K-Means guardado en: {ruta_modelo}')

# Visualizar los primeros registros con su cluster asignado
print(dataset.head())

# Guardar el dataset con los clusters asignados
ruta_resultado = r'D:\User0\Desktop\ING SOFTWARE\7 Semestre\Inteligencia Artificial\Act 3\transporte_masivo_clusters.csv'
dataset.to_csv(ruta_resultado, index=False)

print(f'Dataset con clusters guardado en: {ruta_resultado}')
