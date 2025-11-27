import pandas as pd

df = pd.read_parquet(r"C:/Users\bbce_\Desktop/python/flights_RUH.parquet")

csv_file = r"C:\Users\bbce_\Desktop\python\flights_RUH.csv"
df.to_csv(csv_file, index=False)