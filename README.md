# ✈️ Flight Insights SQL

Automated **SQL pipeline** with **GitHub Actions** + **SQLite**.  
Every day at 08:00 UTC, the workflow imports raw flight data, runs SQL queries, and saves insights in `/results`.

![SQL Pipeline Status](https://github.com/shanipix/flight_insights_sql/actions/workflows/sql_pipeline.yml/badge.svg)

---

## 📊 Results
Latest auto-generated CSV reports:  
- 📈 [Average price per airline](results/avg_price_per_airline.csv)  
- 💺 [Average price by class](results/avg_price_by_class.csv)  
- 🌍 [Top destinations](results/top_destinations.csv)  

*(Reports update automatically with each workflow run)*

---

## ⚙️ Tech Stack
- SQL (**SQLite**)  
- **GitHub Actions** for automation  
- CSV data processing  

---

## 🚀 Workflow
1. **Raw data** → stored in `/data` (Google Sheets export)  
2. **SQL scripts** → in `/queries` (schema + KPIs)  
3. **Pipeline** → runs automatically via `.github/workflows/sql_pipeline.yml`  
4. **Results** → saved in `/results` as CSV files  

---

## 🌟 Purpose
This project is part of my **Data Analyst Portfolio**.  
It demonstrates how to:  
- Automate SQL workflows using GitHub Actions  
- Transform raw CSV into actionable insights  
- Showcase results directly on GitHub for recruiters & clients  
