import pandas as pd
from pathlib import Path

# chemins
RAW = Path("../data/raw")
OUT = Path("../data/processed")
OUT.mkdir(parents=True, exist_ok=True)

# chargement
employees = pd.read_csv(RAW / "Employees.csv")
customers = pd.read_csv(RAW / "Customers.csv")
orders = pd.read_csv(RAW / "Orders.csv")

orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["ShippedDate"] = pd.to_datetime(orders["ShippedDate"])

# ------------------
# DIM EMPLOYEE
# ------------------
dim_employee = employees[
    ["EmployeeID", "FirstName", "LastName", "Title", "City", "Country"]
].copy()
dim_employee["EmployeeName"] = dim_employee["FirstName"] + " " + dim_employee["LastName"]
dim_employee.to_csv(OUT / "dim_employee.csv", index=False)

# ------------------
# DIM CUSTOMER
# ------------------
dim_customer = customers[
    ["CustomerID", "CompanyName", "City", "Country"]
].copy()
dim_customer.to_csv(OUT / "dim_customer.csv", index=False)

# ------------------
# FACT ORDERS
# ------------------
fact_orders = orders.merge(
    dim_employee[["EmployeeID", "EmployeeName"]], on="EmployeeID"
).merge(
    dim_customer[["CustomerID", "CompanyName"]], on="CustomerID"
)

fact_orders["nb_commandes_livrees"] = fact_orders["ShippedDate"].notna().astype(int)
fact_orders["nb_commandes_non_livrees"] = fact_orders["ShippedDate"].isna().astype(int)

fact_orders = fact_orders[
    [
        "OrderID",
        "OrderDate",
        "EmployeeName",
        "CompanyName",
        "nb_commandes_livrees",
        "nb_commandes_non_livrees",
    ]
]

fact_orders.to_csv(OUT / "fact_orders.csv", index=False)

print(" ETL terminé")
