import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_33112.csv", skiprows=4)

# Select year
year = "2023"

# Keep required columns
df = df[["Country Name", "Country Code", year]].dropna()

# Keep only valid country codes (3 uppercase letters)
df = df[df["Country Code"].str.match(r"^[A-Z]{3}$", na=False)]

# Remove regional and aggregate codes
exclude = [
    "ARB","CEB","CSS","EAR","EAS","EAP","TEA","EMU","ECS","TEC","EUU",
    "FCS","HIC","HPC","IBD","IBT","IDA","IDB","IDX","LAC","LCN","LDC",
    "LIC","LMC","LMY","LTE","MEA","MNA","MIC","NAC","OED","OSS","PSS",
    "PST","PRE","SAS","SSA","SSF","TSA","TSS","UMC","WLD"
]

df = df[~df["Country Code"].isin(exclude)]

# Get Top 10 countries
top10 = df.sort_values(by=year, ascending=False).head(10)

print(top10)

# ------------------ Bar Chart ------------------
plt.figure(figsize=(12,6))
plt.bar(top10["Country Name"], top10[year], color="royalblue")
plt.title("Top 10 Most Populous Countries (2023)")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Top10_Population_BarChart.png")
plt.show()

# ------------------ Histogram ------------------
plt.figure(figsize=(10,6))
plt.hist(df[year], bins=20, color="orange", edgecolor="black")
plt.title("Population Distribution of Countries (2023)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("Population_Histogram.png")
plt.show()