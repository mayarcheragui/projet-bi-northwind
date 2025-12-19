import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

PROCESSED = "../data/processed/"
FIGURES = "../outputs/figures/"
os.makedirs(FIGURES, exist_ok=True)

# Chargement
fact_orders = pd.read_csv(PROCESSED + "fact_orders.csv", parse_dates=["OrderDate", "ShippedDate"])

# KPI global
total_orders = fact_orders.shape[0]
total_delivered = fact_orders["Delivered"].sum()
total_not_delivered = fact_orders["NotDelivered"].sum()
print(f"Total commandes : {total_orders}")
print(f"Commandes livrées : {total_delivered}")
print(f"Commandes non livrées : {total_not_delivered}")

# Commandes par employé
orders_by_employee = fact_orders.groupby("EmployeeName")[["Delivered", "NotDelivered"]].sum().sort_values("Delivered", ascending=False)
orders_by_employee.plot(kind="bar", stacked=True)
plt.title("Commandes livrées / non livrées par employé")
plt.ylabel("Nombre de commandes")
plt.tight_layout()
plt.savefig(FIGURES + "dashboard_livraison.png")
plt.close()

# Commandes par client
orders_by_customer = fact_orders.groupby("CompanyName")[["Delivered", "NotDelivered"]].sum().sort_values("Delivered", ascending=False)
orders_by_customer.plot(kind="bar", stacked=True)
plt.title("Commandes livrées / non livrées par client")
plt.ylabel("Nombre de commandes")
plt.tight_layout()
plt.savefig(FIGURES + "dashboard_client.png")
plt.close()

# Évolution des commandes dans le temps
orders_time = fact_orders.groupby(fact_orders["OrderDate"].dt.to_period("M"))[["Delivered", "NotDelivered"]].sum()
orders_time.plot(kind="line")
plt.title("Évolution des commandes dans le temps")
plt.ylabel("Nombre de commandes")
plt.tight_layout()
plt.savefig(FIGURES + "evolution_commandes.png")
plt.close()

print("✅ Dashboard généré dans outputs/figures")
