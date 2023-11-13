import pyreadstat
import pandas as pd

data, meta = pyreadstat.read_sav("EHPM 2022.sav")
data = data.fillna(0)

columnas_ingreso = [col for col in data.columns if 'ingreso' in col.lower()]

# Suma las columnas de ingreso y crea una nueva columna "ingresos_totales"
data['ingresos_totales'] = data[columnas_ingreso].sum(axis=1)

# Define los límites de los grupos de 5 en 5 años
bins = list(range(0, 105, 5))

# Define las etiquetas para los grupos
labels = list(range(1, len(bins)))

data['grupo_edad'] = pd.cut(data['r106'], bins=bins, labels=labels, right=False)
data['edad'] = data['r106']

# Crea un nuevo DataFrame solo con las columnas de interés
nuevo_df = data[['ingresos_totales', 'grupo_edad', 'edad']]

etiquetas_variables = meta.column_names_to_labels

# Encuentra las etiquetas que contienen la palabra 'salud'
etiquetas_salud = {variable: etiqueta for variable, etiqueta in etiquetas_variables.items() if etiqueta and ('') in etiqueta.lower()}

variables_salud = {variable: etiqueta for variable, etiqueta in etiquetas_variables.items() if variable and ('r50') in variable.lower()}
# Muestra las etiquetas relacionadas con salud
#for variable, etiqueta in etiquetas_salud.items():
    #print(f"Variable: {variable}, Etiqueta: {etiqueta}")

for variable, etiqueta in variables_salud.items():
    print(f"Variable: {variable}, Etiqueta: {etiqueta}")

# r3213a Internet residencial 1,2,4 si tiene 5,6 no
# Tenencia de luz 83.5% nivel nacional r311 1 es electrica
# Tenecia de agua 79.4% nivel nacional r312 1,2,3,4,4.1 si tiene acceso

print(data[["r508"]])

# Guarda el nuevo DataFrame en un nuevo archivo .csv o .xlsx, por ejemplo
#nuevo_df.to_csv("MainDatabase.csv", index=False)




