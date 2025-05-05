# 🚚 EZ Street Deliveries – End-to-End Analytics Dashboard

This project is a real-world, end-to-end data engineering and analytics solution designed for a delivery company, EZ Street Deliveries. It combines Python, SQLite, and Power BI to track and analyze delivery performance across time, drivers, and locations.

---

## 📊 Features

- **Total Orders, Average Delivery Time, Total Cost** – clean KPI visuals
- **Driver Performance** – deliveries per driver
- **Delivery Status Analysis** – Pie chart for Delivered vs Cancelled
- **Date Trends** – Ability to visualize delivery cost/time over time
- **Interactive Slicers** – filter by Driver or Status easily

---

## 🧰 Tools & Technologies

| Stage         | Tool Used           |
|---------------|---------------------|
| Data Cleaning | Python (pandas)     |
| Storage       | SQLite (via Python) |
| Visualization | Power BI            |

---

## 🗂️ Project Structure

```plaintext
ez-delivery-dashboard/
├── ez_delivery_dashboard.pbix        # Power BI dashboard file
├── sample_delivery_data_with_date.csv # Sample/test CSV with headers
├── EZ_Street_Delivery_Project_Explanation.docx  # Explanation document
├── 01_clean_data.py                  # (Optional) Data cleaning script
├── 02_load_to_db.py                  # (Optional) Load cleaned data to SQLite
├── 03_generate_summary.py            # (Optional) Generate summary from DB
```

---

## 📁 Sample Data Format

| OrderID | Date       | Pickup | Drop   | Distance_km | Time_taken_min | Driver | Cost | Status    |
|---------|------------|--------|--------|--------------|----------------|--------|------|-----------|
| 1001    | 2024-04-10 | Dallas | Austin | 320          | 190            | John   | 50   | Delivered |

---

## ⚙️ How to Use

1. Replace the sample CSV with your own real delivery data (same column names)
2. Open `ez_delivery_dashboard.pbix` in Power BI
3. Use "Transform Data" to update the source to your new CSV file
4. Click "Close & Apply" to refresh the visuals

---

## 🎓 About the Developer

👋 Hi, I'm **Rahul Alle**, a graduate student and aspiring Data Engineer. This project showcases my ability to integrate Python, SQL, and BI tools to solve real business problems.

📫 [Connect with me on LinkedIn](https://www.linkedin.com/in/rahul-alle)

---

## ✅ Status
✅ Completed and tested with real-world-ready dashboards.

---

## 📌 License
This project is open-source. Feel free to fork, customize, and use it to showcase your own data engineering skills!
