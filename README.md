# Data folder

# ✈️ Flight Insights SQL

Automated SQL pipeline with **GitHub Actions** + **SQLite**.  
This project runs every day at 08:00 UTC and produces flight insights from raw CSV data.

![SQL Pipeline Status](https://github.com/shanipix/flight_insights_sql/actions/workflows/sql_pipeline.yml/badge.svg)

---

## 📂 Results
- [Average price per airline](results/avg_price_per_airline.csv)  
- [Average price by class](results/avg_price_by_class.csv)  
- [Top destinations](results/top_destinations.csv)  

---

## ⚙️ Tech Stack
- SQL (SQLite)
- GitHub Actions
- CSV Data Processing

---

## 🚀 How it works
1. Raw data in `/data`
2. Queries in `/queries`
3. Results generated in `/results`
4. Workflow in `.github/workflows/sql_pipeline.yml`

---

## 🌟 Purpose
This project is part of my **Data Analyst Portfolio**.  
It shows how to:
- Automate SQL workflows with GitHub Actions  
- Transform raw data into insights  
- Showcase results directly on GitHub
