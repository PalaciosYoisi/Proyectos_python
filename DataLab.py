import pandas as pd
import matplotlib.pyplot as plt

convertir = pd.read_excel('Choco.xlsx')
convertir_redondeado = convertir.copy()

for columna in convertir_redondeado.columns:
    if convertir_redondeado[columna].dtype == 'float64':
        convertir_redondeado[columna] = convertir_redondeado[columna].round(1)

convertir_redondeado.to_csv('Choco.csv', index=None, header=True)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

espacio_columnas = convertir_redondeado.to_string(index=False, header=True, col_space=10)
espacio_filas = '\n\n'.join(espacio_columnas.split('\n'))

print(espacio_filas)

conceptos_deseados = [
    'Tasa de Ocupación (TO)',
    'Tasa de Desocupación (TD)',
]

datos_filtrados = convertir_redondeado[convertir_redondeado['Concepto'].isin(conceptos_deseados)]

columnas_grafico = ["Concepto", 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]

datos = datos_filtrados[columnas_grafico]

datos.set_index("Concepto", inplace=True)

datos_transpuesta = datos.T

fig, ax = plt.subplots(figsize=(14, 8))
datos_transpuesta.plot(kind="line", marker='o', ax=ax)

plt.title("Cifras de desempleo en el Chocó desde 2015 hasta la actualidad")
plt.xlabel("Años")
plt.ylabel("Tasa de desempleo (%)")
plt.legend(title="Concepto", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid()

plt.tight_layout()

plt.show()

"""Podemos observar que los índices de desempleo desde 2015 hasta 2023 han tenido un aumento gradual siendo
2023 su píco, lo cual es preocupante. lo cual demuestra un indice de bajas oportunidades en el departamento"""