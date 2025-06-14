import pandas as pd
import random

# Cargar el archivo original
archivo_entrada = "nyc_wifi_columnas_ordenadas.xlsx"
archivo_salida = "nyc_wifi_reducido_final.xlsx"

# Cargar todas las hojas
hojas = pd.read_excel(archivo_entrada, sheet_name=None)

# Crear nuevo diccionario de hojas reducidas
hojas_reducidas = {}

for nombre_hoja, df in hojas.items():
    df = df.dropna(subset=['SSID'])  # Asegurar que SSID no sea nulo
    df_temp_closing = df[df['Remarks'] == 'Temporary Closing']
    df_no_temp = df[df['Remarks'] != 'Temporary Closing']

    # Seleccionar 3 filas con "Temporary Closing", si hay suficientes
    n_temp = min(3, len(df_temp_closing))
    muestra_temp = df_temp_closing.sample(n=n_temp, random_state=1)

    # Seleccionar filas restantes al azar (hasta completar 30)
    n_restante = 30 - len(muestra_temp)
    muestra_restante = df_no_temp.sample(n=n_restante, random_state=1)

    # Combinar ambas muestras
    df_final = pd.concat([muestra_temp, muestra_restante]).sample(frac=1, random_state=1)  # Mezclar

    hojas_reducidas[nombre_hoja] = df_final

# Guardar en un nuevo archivo Excel
with pd.ExcelWriter(archivo_salida) as writer:
    for nombre_hoja, df in hojas_reducidas.items():
        df.to_excel(writer, sheet_name=nombre_hoja, index=False)

print(f"Archivo creado: {archivo_salida}")
