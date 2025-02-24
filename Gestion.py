import pandas as pd


data = {
    "Transaction_date": ["1/2/2009 6:17", "1/2/2009 4:53", "1/2/2009 13:08", "1/3/2009 14:44", "1/4/2009 12:23"],
    "Product": ["Product1", "Product2", "Product1", "Product3", "Product2"],
    "Precio": [1200, 800, 900, 1500, 700],
    "Payment_Type": ["Visa", "Mastercard", "Visa", "Amex", "Visa"],
    "Name": ["Maria", "Juan", "Mario", "Felipe", "Sofia"],
    "City": ["London", "New York", "London", "Paris", "New York"],
    "Ciudad": ["Reino Unido", "Estados Unidos", "Reino Unido", "France", "Estados Unidos"]
}


df_example = pd.DataFrame(data)


csv_path = "SalesJan2009.csv"
df_example.to_csv(csv_path, index=False)

print(f"Archivo CSV '{csv_path}' creado con éxito.")

purchase_counts = df_example[df_example["City"].isin(["Paris", "New York"])].groupby("City").size()

payment_methods = df_example[df_example["City"].isin(["Paris", "New York"])].groupby(["City", "Payment_Type"]).size()


print("\nNúmero de compras por ciudad:")
print(purchase_counts)

print("\nMétodos de pago utilizados en cada ciudad:")
print(payment_methods)

