import pandas as pd

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# Mostrar tabla
print(df)

# Calcular total de ventas
total_ventas = (df["cantidad"] * df["precio"]).sum()

print("Total de ventas:", total_ventas)