import pandas as pd
import os

# Dossiers
RAW_PATH = "../data/raw/"
PROCESSED_PATH = "../data/processed/"
os.makedirs(PROCESSED_PATH, exist_ok=True)

# Charger les données brutes
customers = pd.read_csv(RAW_PATH + "Customers.csv")
orders = pd.read_csv(RAW_PATH + "Orders.csv")
order_details = pd.read_csv(RAW_PATH + "Order_Details.csv")
products = pd.read_csv(RAW_PATH + "Products.csv")

# Conversion des dates
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# Jointure Orders + Order Details
sales = orders.merge(order_details, on="OrderID", how="inner")

# Jointure avec Products
sales = sales.merge(products, on="ProductID", how="inner")

# 👉 IMPORTANT : on garde le prix de vente (Order_Details)
sales = sales.rename(columns={"UnitPrice_x": "UnitPrice"})

# Calcul du chiffre d'affaires
sales["Revenue"] = sales["UnitPrice"] * sales["Quantity"] * (1 - sales["Discount"])

# Nettoyage
sales = sales.dropna(subset=["Revenue"])

# Colonnes finales (table de faits)
sales_final = sales[[
    "OrderID",
    "OrderDate",
    "CustomerID",
    "ProductID",
    "ProductName",
    "CategoryID",
    "Quantity",
    "UnitPrice",
    "Discount",
    "Revenue"
]]

# Sauvegarde
sales_final.to_csv(PROCESSED_PATH + "sales.csv", index=False)

print("✅ Transformation terminée : sales.csv créé")
