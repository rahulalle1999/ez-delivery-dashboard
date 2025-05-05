import sqlite3
import pandas as pd

print("👋 Script started")
print("📡 Connecting to database...")

db_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\delivery_data.db"
conn = sqlite3.connect(db_path)

# Use quotes around Drop (it's a SQL keyword!)
query = """
SELECT 
    OrderID,
    Date,
    Driver,
    Status,
    Time_taken_min,
    Cost,
    Pickup || ' → ' || "Drop" AS Route
FROM deliveries
"""

print("🧾 Running summary query...")
df = pd.read_sql_query(query, conn)

summary_path = r"C:\Users\rahul\OneDrive\Desktop\ez-delivery-insights\data\delivery_summary.csv"
df.to_csv(summary_path, index=False)

print("✅ Summary saved to:", summary_path)


