# 1-RECOLECCIÓN DE DATOS

import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
file_path = '/content/Base de datos Sales.csv'

# Cargar datos desde el archivo CSV
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame
print(df.head())

# 2-LIMPIEZA Y TRANSFORMACIÓN DE DATOS

# Ruta del archivo CSV
file_path = '/content/Base de datos Sales.csv'

# Cargar datos desde el archivo CSV
df = pd.read_csv(file_path)

# Mostrar las primeras filas del DataFrame para verificar la carga correcta
print(df.head())

# Eliminar duplicados
df.drop_duplicates(inplace=True)

# Manejar valores nulos (rellenar con 0)
df.fillna(0, inplace=True)

# Normalizar datos (convertir fechas al mismo formato)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Mostrar las primeras filas del DataFrame después de la limpieza
print(df.head())

# 3 - ANALISIS DE DATOS
# 3.1 Estadísticas descriptivas del Conjunto de datos

data = pd.read_csv(file_path)

# Estadísticas descriptivas del conjunto de datos
# count:Número total de registros en el conjunto de datos
# mean: Promedio de los IDs de pedido
# std: Desviación estándar de los IDs de pedido, indicando la variabilidad
# min: ID de pedido más bajo
# 25%: Primer cuartil, el 25% de los IDs de pedido son menores que este valor
# 50%: Mediana, el 50% de los IDs de pedido son menores que este valor
# 75%: Tercer cuartil, el 75% de los IDs de pedido son menores que este valor
# max: ID de pedido más alto

print("\nEstadísticas descriptivas del conjunto de datos:")
print(data.describe())

# 3.2 Conteo de ventas por región
sales_by_region = data['Region'].value_counts()
print("\nConteo de ventas por región:")
print(sales_by_region)

# Graficar el conteo de ventas por región
sales_by_region.plot(kind='bar', figsize=(6, 1))
plt.title('Conteo de Ventas por Región')
plt.xlabel('Región')
plt.ylabel('Cantidad de Ventas')
plt.show()

# 3.3 Ingresos totales por región
revenue_by_region = data.groupby('Region')['Total Revenue'].sum()
print("\nIngresos totales por región:")
print(revenue_by_region)

# Graficar los ingresos totales por región
revenue_by_region.plot(kind='pie', figsize=(5, 5), autopct='%1.1f%%', startangle=140)
plt.title('Ingresos Totales por Región')
plt.ylabel('')
# Ocultar la etiqueta del eje Y
plt.show()

# 3.4 Beneficio total por región
profit_by_region = data.groupby('Region')['Total Profit'].sum()
print("\nBeneficio total por región:")
print(profit_by_region)
descriptive_stats = df.describe()

# Graficar el beneficio total por región
profit_by_region.plot(kind='bar', figsize=(6, 2))
plt.title('Beneficio Total por Región')
plt.xlabel('Región')
plt.ylabel('Beneficio Total')
plt.xticks(rotation=45)
plt.show()

# 3.5 Conteo de ventas por tipo de producto
revenue_by_item_type = data.groupby('Item Type')['Total Revenue'].sum()
sales_by_item_type = data['Item Type'].value_counts()
print("\nConteo de ventas por tipo de producto:")
print(sales_by_item_type)

# Graficar el conteo de ventas por tipo de producto
sales_by_item_type.plot(kind='bar', figsize=(6, 2))
plt.title('Conteo de Ventas por Tipo de Producto')
plt.xlabel('Tipo de Producto')
plt.ylabel('Cantidad de Ventas')
plt.xticks(rotation=45)
plt.show()

# 3.6 Ingresos totales por tipo de producto
revenue_by_item_type = data.groupby('Item Type')['Total Revenue'].sum()
print("\nIngresos totales por tipo de producto:")
print(revenue_by_item_type)

# Graficar el conteo de ventas por tipo de producto
sales_by_item_type.plot(kind='bar', figsize=(6, 2))
plt.title('Conteo de Ventas por Tipo de Producto')
plt.xlabel('Tipo de Producto')
plt.ylabel('Cantidad de Ventas')
plt.xticks(rotation=45)
plt.show()

# 3.7 Beneficio total por tipo de producto
profit_by_item_type = data.groupby('Item Type')['Total Profit'].sum()
print("\nBeneficio total por tipo de producto:")
print(profit_by_item_type)

# Graficar el beneficio total por tipo de producto
profit_by_item_type.plot(kind='bar', figsize=(6, 2))
plt.title('Beneficio Total por Tipo de Producto')
plt.xlabel('Tipo de Producto')
plt.ylabel('Beneficio Total')
plt.xticks(rotation=45)
plt.show()

# 3.8 Conteo de ventas por canal de ventas
sales_by_channel = data['Sales Channel'].value_counts()
print("\nConteo de ventas por canal de ventas:")
print(sales_by_channel)

# Graficar el conteo de ventas por canal de ventas
sales_by_channel.plot(kind='pie', figsize=(5, 5), autopct='%1.1f%%', startangle=140)
plt.title('Conteo de Ventas por Canal de Ventas')
plt.ylabel('')
# Ocultar la etiqueta del eje Y
plt.show()

# 3.9 Ingresos totales por canal de ventas
revenue_by_channel = data.groupby('Sales Channel')['Total Revenue'].sum()
print("\nIngresos totales por canal de ventas:")
print(revenue_by_channel)

# Graficar los ingresos totales por canal de ventas
revenue_by_channel.plot(kind='pie', figsize=(5, 5), autopct='%1.1f%%', startangle=140)
plt.title('Ingresos Totales por Canal de Ventas')
plt.ylabel('')
# Ocultar la etiqueta del eje Y
plt.show()

# 3.10 # Beneficio total por canal de ventas
profit_by_channel = data.groupby('Sales Channel')['Total Profit'].sum()
print("\nBeneficio total por canal de ventas:")
print(profit_by_channel)

# Graficar el beneficio total por canal de ventas
profit_by_channel.plot(kind='bar', figsize=(6, 2))
plt.title('Beneficio Total por Canal de Ventas')
plt.xlabel('Canal de Ventas')
plt.ylabel('Beneficio Total')
plt.xticks(rotation=45)
plt.show()
