import pandas as pd
from itertools import combinations

# Cargar dataset
df = pd.read_csv('propiedades_divorcio.csv')
df['valor_neto'] = df['valor_propiedad'] - df['deuda_asociada']

# Filtrar solo propiedades disponibles para asignación
df_disponibles = df[df['disponible_para_asignacion'] == True]
rentables = df_disponibles[df_disponibles['disponible_para_renta'] == True]
no_rentables = df_disponibles[df_disponibles['disponible_para_renta'] == False]

# Función para dividir equitativamente
def dividir_equitativamente(propiedades, objetivo):
    mejor_diferencia = float('inf')
    mejor_combinacion = None
    for r in range(1, len(propiedades)):
        for combo in combinations(propiedades.index, r):
            valor_combo = propiedades.loc[list(combo), 'valor_neto'].sum()
            diferencia = abs(valor_combo - objetivo)
            if diferencia < mejor_diferencia:
                mejor_diferencia = diferencia
                mejor_combinacion = list(combo)
    return propiedades.loc[mejor_combinacion]

# Calcular objetivo (50% del valor total disponible)
valor_total = df_disponibles['valor_neto'].sum()
objetivo = valor_total / 2

# Dividir propiedades
conjunto_rentables_A = dividir_equitativamente(rentables, objetivo / 2)
conjunto_rentables_B = rentables[~rentables.index.isin(conjunto_rentables_A.index)]
conjunto_no_rentables_A = dividir_equitativamente(no_rentables, objetivo / 2)
conjunto_no_rentables_B = no_rentables[~no_rentables.index.isin(conjunto_no_rentables_A.index)]

# Resultados
escenario = {
    "Cónyuge A": {
        "Propiedades rentables": conjunto_rentables_A['id_propiedad'].tolist(),
        "Valor rentables": conjunto_rentables_A['valor_neto'].sum(),
        "Propiedades no rentables": conjunto_no_rentables_A['id_propiedad'].tolist(),
        "Valor no rentables": conjunto_no_rentables_A['valor_neto'].sum(),
        "Total": conjunto_rentables_A['valor_neto'].sum() + conjunto_no_rentables_A['valor_neto'].sum()
    },
    "Cónyuge B": {
        "Propiedades rentables": conjunto_rentables_B['id_propiedad'].tolist(),
        "Valor rentables": conjunto_rentables_B['valor_neto'].sum(),
        "Propiedades no rentables": conjunto_no_rentables_B['id_propiedad'].tolist(),
        "Valor no rentables": conjunto_no_rentables_B['valor_neto'].sum(),
        "Total": conjunto_rentables_B['valor_neto'].sum() + conjunto_no_rentables_B['valor_neto'].sum()
    },
    "Propiedades no asignables": df[df['disponible_para_asignacion'] == False]['id_propiedad'].tolist()
}

# Mostrar resultados
print("⚖️ Escenario Optimizado (50/50) con Disponibilidad:")
for conyuge, datos in escenario.items():
    if conyuge != "Propiedades no asignables":
        print(f"\n👤 {conyuge}:")
        print(f"  - Rentables: {datos['Propiedades rentables']} (${datos['Valor rentables']:.2f})")
        print(f"  - No rentables: {datos['Propiedades no rentables']} (${datos['Valor no rentables']:.2f})")
        print(f"  ✅ Total: ${datos['Total']:.2f}")
    else:
        print(f"\n🚫 Propiedades no asignables: {datos}")

diferencia = abs(escenario["Cónyuge A"]["Total"] - escenario["Cónyuge B"]["Total"])
print(f"\n📌 Diferencia final: ${diferencia:.2f} ({(diferencia / valor_total * 100):.2f}% del valor disponible)")