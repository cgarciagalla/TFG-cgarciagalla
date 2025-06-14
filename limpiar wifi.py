import pandas as pd

# Ruta del archivo de entrada
archivo_entrada = r"C:\Users\carli\OneDrive\Escritorio\nyc-wi-fi-hotspot-locations.csv"

# Cargar CSV
df = pd.read_csv(archivo_entrada, encoding='utf-8', sep=',')

# Columnas a conservar y su orden específico
columnas_ordenadas = [
    "Type", "OBJECTID", "SSID", "Remarks", "Location_T", "Name", "Location",
    "Latitude", "Longitude", "Provider", "City", "BoroName", "BoroCode",
    "NTAName", "NTACode", "Borough", "DOITT_ID", "CounDist", "Postcode"
]

# Filtrar columnas y eliminar filas con valores nulos
df_filtrado = df[columnas_ordenadas].dropna()

# Dividir en dos hojas por tipo
df_free = df_filtrado[df_filtrado["Type"] == "Free"]
df_limited = df_filtrado[df_filtrado["Type"] == "Limited Free"]

# Guardar en un archivo Excel con dos hojas
archivo_salida = r"C:\Users\carli\OneDrive\Escritorio\nyc_wifi_columnas_ordenadas.xlsx"
with pd.ExcelWriter(archivo_salida, engine="openpyxl") as writer:
    df_free.to_excel(writer, sheet_name="FreeHotspot", index=False)
    df_limited.to_excel(writer, sheet_name="LimitedFreeHotspot", index=False)

print("✅ Archivo guardado correctamente:", archivo_salida)
