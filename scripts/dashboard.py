import pandas as pd
import matplotlib.pyplot as plt
import os

# Chemins
DATA_PATH = "../data/processed/"
OUTPUT_PATH = "../outputs/figures/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

# Charger les données
sales = pd.read_csv(DATA_PATH + "sales.csv", parse_dates=["OrderDate"])

# =====================
# KPI 1 : Chiffre d'affaires total
# =====================
total_revenue = sales["Revenue"].sum()
print(f"Chiffre d'affaires total : {total_revenue:.2f}")

# =====================
# KPI 2 : Nombre de commandes
# =====================
nb_orders = sales["OrderID"].nunique()
print(f"Nombre de commandes : {nb_orders}")

# =====================
# CA par catégorie
# =====================
ca_category = sales.groupby("CategoryID")["Revenue"].sum().sort_values(ascending=False)

plt.figure()
ca_category.plot(kind="bar")
plt.title("Chiffre d'affaires par catégorie")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(OUTPUT_PATH + "ca_par_categorie.png")
plt.close()

# =====================
# Évolution du CA dans le temps
# =====================
ca_time = sales.groupby(sales["OrderDate"].dt.to_period("M"))["Revenue"].sum()

plt.figure()
ca_time.plot()
plt.title("Évolution du chiffre d'affaires")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(OUTPUT_PATH + "evolution_ca.png")
plt.close()

print("✅ Dashboard Python généré")
