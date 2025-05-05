import pandas as pd

print("📦 Reading raw file...")

file_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\raw_delivery_data.csv"
df = pd.read_csv(file_path)

print("🧹 Cleaning data...")

df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Date'] = pd.to_datetime(df['Date'])

cleaned_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\cleaned_delivery_data.csv"
df.to_csv(cleaned_path, index=False)

print("✅ Cleaned file saved at:", cleaned_path)
