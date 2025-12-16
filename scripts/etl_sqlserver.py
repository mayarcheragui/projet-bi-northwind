import pyodbc
import pandas as pd
import os

# Création du dossier data/raw si jamais il n'existe pas
os.makedirs("../data/raw", exist_ok=True)

# Connexion à SQL Server (Docker)
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=Northwind;"
    "UID=sa;"
    "PWD=StrongPassword123!"
)

# Tables à extraire
tables = [
    "Customers",
    "Orders",
    "Order Details",
    "Products",
    "Categories"
]

for table in tables:
    print(f"Extraction de {table}...")
    df = pd.read_sql(f"SELECT * FROM [{table}]", conn)
    df.to_csv(f"../data/raw/{table.replace(' ', '_')}.csv", index=False)

conn.close()
print("✅ Extraction SQL Server terminée avec succès.")
