import pandas as pd
import os

RAW = "../data/raw/"
PROCESSED = "../data/processed/"
os.makedirs(PROCESSED, exist_ok=True)

# DimCustomer
customers = pd.read_csv(RAW + "Customers.csv")
dim_customer = customers[["CustomerID", "CompanyName", "City", "Country", "Region"]]
dim_customer.to_csv(PROCESSED + "dim_customer.csv", index=False)

# DimProduct
products = pd.read_csv(RAW + "Products.csv")
dim_product = products[["ProductID", "ProductName", "CategoryID", "SupplierID"]]
dim_product.to_csv(PROCESSED + "dim_product.csv", index=False)

# DimCategory
categories = pd.read_csv(RAW + "Categories.csv")
dim_category = categories[["CategoryID", "CategoryName"]]
dim_category.to_csv(PROCESSED + "dim_category.csv", index=False)

print("✅ Dimensions créées")
