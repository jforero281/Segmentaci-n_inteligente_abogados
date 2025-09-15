# eda.py

import pandas as pd          # Para manejar la base de datos
import numpy as np           # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para gráficas
import seaborn as sns        # Para gráficas más bonitas
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder


basededatos = pd.read_excel("C:\\Users\\arian\\Segmentaci-n_inteligente_abogados\\Base_Datos.xlsx")
print(basededatos)
print(basededatos.columns)   #muestra el nombre de todas las columnas

basededatos.info()
# 3. Limpiar nombres de columnas: quitar saltos de línea y espacios al inicio/final
basededatos.columns = basededatos.columns.str.replace('\n', ' ').str.strip()

# 4. Lista de columnas a eliminar
columnas_a_eliminar = [
    "INSTANCIA",
    "FOGAFIN",
    "OBSERVACIONES",
    "APODERADO ACTOR",
    "HONORARIOS",
    "TOTAL % PROVISIÓN",
    "% PROVISIÓN 2015",
    "% PROVISIÓN Años anteriores",
    "EMPRESA APODERADO BANCO",
    "FECHA ESTIMADA DE PAGO",
    "MONTO TOTAL DE LA PROVISIÓN",
    "MONTO DE LA PROVISION (EN MILLONES) 2017",
    "MONTO DE LA PROVISION (EN MILLONES) Años anteriores",
    "Fecha Casación",
    "CASACIÓN",
    "Fecha Fallo 2a. instancia",
    "SEGUNDA INSTANCIA",
    "Fecha Fallo 1a. instancia",
    "MOTIVOS",
    "PRIMERA INSTANCIA"
]

# 5. Eliminar solo las columnas que existen en el DataFrame
columnas_a_eliminar_existentes = [col for col in columnas_a_eliminar if col in basededatos.columns]
basededatos.drop(columns=columnas_a_eliminar_existentes, inplace=True)

# 6. Verificar que se eliminaron correctamente
print("Columnas después de eliminar:")
print(basededatos.columns)

basededatos.info()
# Mostrar todas las columnas del DataFrame al imprimir
pd.set_option('display.max_columns', None)
basededatos.describe()
print(basededatos.describe(include='all'))
# Contar cuántas filas están duplicadas
cantidad_duplicados = basededatos.duplicated().sum()
print("Cantidad de filas duplicadas:", cantidad_duplicados)
# Mostrar duplicados sin incluir la primera aparición
filas_duplicadas = basededatos[basededatos.duplicated(keep='first')]
print(filas_duplicadas)
# Eliminar filas duplicadas
basededatos = basededatos.drop_duplicates()

# Verificar que se eliminaron
print("Cantidad de filas después de eliminar duplicados:", len(basededatos))

basededatos.info()
# Revisar valores únicos de cada columna
for col in basededatos.columns:
    print(f"\n🔹 Columna: {col}")
    print("Total de valores únicos:", basededatos[col].nunique())
    print("Ejemplo de valores únicos:", basededatos[col].unique()[:20])  # muestra solo 20 como ejemplo
    print("-"*80)
    #Revisar el nombre exacto de las columnas
print(basededatos.columns.tolist())
# Normalizar todas las columnas de tipo object (texto)
for col in basededatos.select_dtypes(include="object").columns:
    basededatos[col] = basededatos[col].str.lower().str.strip()
# Ver valores únicos de la primera columna
primera_columna = basededatos.columns[0]
print(f"Columna: {primera_columna}")
print("Valores únicos:")
print(basededatos[primera_columna].unique())
print("\nTotal de valores únicos:", basededatos[primera_columna].nunique())
# Normalizar nombres de columnas a minúsculas y sin espacios
basededatos.columns = basededatos.columns.str.lower().str.strip()
#Revisar ocurrencias especificas
print("Cantidad 'johana patricia correa racedo':",
      (basededatos["tipo de proceso"] == "johana patricia correa racedo").sum())

print("Cantidad 'no dda':",
      (basededatos["tipo de proceso"] == "no dda").sum())


basededatos.info()


# Variables
numericas = ["año demanda"]

ordinales = ["clase (posibilidad de pérdida)", "estado actual"]

nominales = [
    "tipo de proceso", "ciudad", "jgo.", "region", "radicado",
    "radicado consulta", "red", "tipo relación", "pretensión",
    "motivos2", "descrpición hechos", "apoderado banco", "causa"
]

# Copia del dataframe original
df_encoded = basededatos.copy()

# Clasificación de las variables
# ==============================
# Numéricas
num_vars = ["año demanda"]

# Ordinales: aquí hay un orden implícito
ord_vars = ["clase (posibilidad de pérdida)", "estado actual"]

# Categóricas nominales: no tienen orden
nom_vars = [
    "tipo de proceso", "ciudad", "jgo.", "region", "radicado",
    "radicado consulta", "red", "tipo relación", "pretensión",
    "motivos2", "descrpición hechos", "apoderado banco", "causa"
]

# ==============================
# Copia de seguridad del dataframe original
# ==============================
df_encoded = basededatos.copy()

# ==============================
# One-Hot Encoding para nominales
# ==============================
df_encoded = pd.get_dummies(df_encoded, columns=nom_vars, drop_first=True)

# ==============================
# Ordinal Encoding para variables con jerarquía
# ==============================
# Defino un posible orden (ajustar según el dataset real)
orden_categorias = [
    ['remota', 'eventual', 'probable', 'alta'],            # clase (posibilidad de pérdida)
    ['inicial', 'en trámite', 'fallado', 'cerrado']        # estado actual
]

encoder = OrdinalEncoder(
    categories=orden_categorias,
    handle_unknown="use_encoded_value",
    unknown_value=-1
)

df_encoded[ord_vars] = encoder.fit_transform(df_encoded[ord_vars])

# ==============================
# Matriz de correlación (Pearson)
# ==============================
corr_matrix = df_encoded.corr(method="pearson")

# Para no saturar en consola, muestro un recorte
print("Vista preliminar de la matriz de correlación:\n")
print(corr_matrix.iloc[:10, :10])

# ==============================
# Heatmap de la correlación
# ==============================
plt.figure(figsize=(15, 10))
sns.heatmap(corr_matrix, cmap="coolwarm", center=0)
plt.title("Matriz de correlación con Pearson")
plt.show()