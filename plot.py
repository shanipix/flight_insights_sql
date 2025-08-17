# plot.py
# Reads CSV reports in /results and generates .png charts

import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)

def save_bar(df, x, y, title, outpath, rotate=False, horizontal=False):
    plt.figure()
    if horizontal:
        df.plot(x=x, y=y, kind="barh", legend=False)
    else:
        df.plot(x=x, y=y, kind="bar", legend=False)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    if rotate:
        plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(outpath, dpi=120)
    plt.close()

# 1) Average price per airline
f1 = "results/avg_price_per_airline.csv"
if os.path.exists(f1):
    df = pd.read_csv(f1)
    df2 = df.sort_values("avg_price", ascending=False).head(12)
    save_bar(df2, "airline", "avg_price",
             "Average Price per Airline", "results/avg_price_per_airline.png",
             rotate=True)

# 2) Top destinations
f2 = "results/top_destinations.csv"
if os.path.exists(f2):
    df = pd.read_csv(f2)
    save_bar(df.sort_values("avg_price", ascending=True),
             "destination_city", "avg_price",
             "Top Destinations (Avg Price)", "results/top_destinations.png",
             rotate=True)

# 3) Average price by class
f3 = "results/avg_price_by_class.csv"
if os.path.exists(f3):
    df = pd.read_csv(f3)
    save_bar(df, "class", "avg_price",
             "Average Price by Class", "results/avg_price_by_class.png")
