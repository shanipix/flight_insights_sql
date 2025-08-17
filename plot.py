import pandas as pd
import matplotlib.pyplot as plt

# Load results
avg_price_airline = pd.read_csv("results/avg_price_per_airline.csv")
avg_price_class = pd.read_csv("results/avg_price_by_class.csv")
top_destinations = pd.read_csv("results/top_destinations.csv")

# 1. Bar chart: Average price per airline
plt.figure(figsize=(8,5))
plt.bar(avg_price_airline["airline"], avg_price_airline["avg_price"], color="skyblue")
plt.title("Average Price per Airline")
plt.xlabel("Airline")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("results/avg_price_per_airline.png")
plt.close()

# 2. Line chart: Average price by class
plt.figure(figsize=(6,4))
plt.plot(avg_price_class["class"], avg_price_class["avg_price"], marker="o", linestyle="-", color="green")
plt.title("Average Price by Class")
plt.xlabel("Class")
plt.ylabel("Average Price")
plt.tight_layout()
plt.savefig("results/avg_price_by_class.png")
plt.close()

# 3. Pie chart: Top destinations
plt.figure(figsize=(6,6))
plt.pie(top_destinations["count"], labels=top_destinations["destination"], autopct="%1.1f%%", startangle=140)
plt.title("Top Destinations Distribution")
plt.tight_layout()
plt.savefig("results/top_destinations.png")
plt.close()
