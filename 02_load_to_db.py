import pandas as pd
import sqlite3

print("📥 Loading cleaned CSV...")

csv_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\cleaned_delivery_data.csv"
db_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\delivery_data.db"

df = pd.read_csv(csv_path)

print("🗃️ Connecting to SQLite DB...")

conn = sqlite3.connect(db_path)

print("📤 Writing to 'deliveries' table...")

df.to_sql("deliveries", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data loaded into database at:", db_path)
