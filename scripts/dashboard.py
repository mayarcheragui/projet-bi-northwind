import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# chemins
DATA_PATH = "../data/processed/"
OUT_PATH = "../outputs/figures/"
os.makedirs(OUT_PATH, exist_ok=True)

# ======================
# CHARGEMENT
# ======================
fact = pd.read_csv(DATA_PATH + "fact_orders.csv", parse_dates=["OrderDate"])

# ======================
# LIVRÉES vs NON LIVRÉES (GLOBAL)
# ======================
livrees = fact["nb_commandes_livrees"].sum()
non_livrees = fact["nb_commandes_non_livrees"].sum()

plt.figure(figsize=(6,6))
plt.bar(["Livrées", "Non livrées"], [livrees, non_livrees])
plt.title("Répartition des commandes livrées / non livrées")
plt.ylabel("Nombre de commandes")
plt.tight_layout()
plt.savefig(OUT_PATH + "repartition_livrees_non_livrees.png")
plt.close()

# ======================
#  PAR CLIENT
# ======================
client_stats = (
    fact.groupby("CompanyName")[["nb_commandes_livrees", "nb_commandes_non_livrees"]]
    .sum()
    .sort_values("nb_commandes_livrees", ascending=False)
)

client_stats.plot(kind="bar", stacked=True, figsize=(12,6))
plt.title("Commandes livrées / non livrées par client")
plt.ylabel("Nombre de commandes")
plt.xlabel("Client")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT_PATH + "livrees_non_livrees_par_client.png")
plt.close()

# ======================
#  PAR EMPLOYÉ
# ======================
employee_stats = (
    fact.groupby("EmployeeName")[["nb_commandes_livrees", "nb_commandes_non_livrees"]]
    .sum()
)

employee_stats.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Commandes livrées / non livrées par employé")
plt.ylabel("Nombre de commandes")
plt.xlabel("Employé")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT_PATH + "livrees_non_livrees_par_employe.png")
plt.close()

# ======================
#  ÉVOLUTION MENSUELLE
# ======================
fact["Month"] = fact["OrderDate"].dt.to_period("M")

monthly = fact.groupby("Month").size()

plt.figure(figsize=(10,5))
monthly.plot()
plt.title("Évolution mensuelle des commandes")
plt.ylabel("Nombre de commandes")
plt.xlabel("Mois")
plt.tight_layout()
plt.savefig(OUT_PATH + "evolution_mensuelle_commandes.png")
plt.close()

# ======================
#  GRAPHE 3D
# ======================
summary = (
    fact.groupby(["OrderDate", "EmployeeName", "CompanyName"])
    [["nb_commandes_livrees", "nb_commandes_non_livrees"]]
    .sum()
    .reset_index()
)

fig = px.scatter_3d(
    summary,
    x="OrderDate",
    y="EmployeeName",
    z="CompanyName",
    color="nb_commandes_livrees",
    size="nb_commandes_livrees",
    title="Commandes livrées / non livrées par employé, client et date"
)

fig.write_html(OUT_PATH + "commandes_3D_livrees_non_livrees.html")

print(" Dashboard généré avec succès")
