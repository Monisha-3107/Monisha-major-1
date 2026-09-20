import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
housing_data = pd.read_csv("housing.csv")

# Remove extra spaces from column names
housing_data.columns = housing_data.columns.str.strip()

# Convert numerical columns to numbers
housing_data["price"] = pd.to_numeric(
    housing_data["price"],
    errors="coerce"
)

housing_data["area"] = pd.to_numeric(
    housing_data["area"],
    errors="coerce"
)

# Remove rows with missing price or area
housing_data = housing_data.dropna(
    subset=["price", "area"]
)

# Clean text columns
for column in ["AC", "parking", "prefarea"]:
    housing_data[column] = (
        housing_data[column]
        .astype(str)
        .str.strip()
        .str.lower()
    )


# --------------------------------------------------
# 1. Price Range Distribution
# --------------------------------------------------

price_ranges = [
    0,
    2_500_000,
    5_000_000,
    7_500_000,
    10_000_000,
    float("inf")
]

labels = [
    "0-25 lakhs",
    "26-50 lakhs",
    "51-75 lakhs",
    "76-100 lakhs",
    "100+ lakhs"
]

housing_data["price_range"] = pd.cut(
    housing_data["price"],
    bins=price_ranges,
    labels=labels,
    include_lowest=True
)

price_range_counts = (
    housing_data["price_range"]
    .value_counts()
    .reindex(labels, fill_value=0)
)

print("Price Range Distribution:")
print(price_range_counts)

plt.figure(figsize=(10, 6))

plt.plot(
    price_range_counts.index.astype(str),
    price_range_counts.values,
    marker="o",
    linewidth=2,
    color="blue"
)

plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Houses")
plt.xticks(rotation=45)
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 2. AC vs Non-AC Average Price
# --------------------------------------------------

avg_price_ac = housing_data[
    housing_data["AC"] == "yes"
]["price"].mean()

avg_price_non_ac = housing_data[
    housing_data["AC"] == "no"
]["price"].mean()

print("\nAverage Price of AC Houses:")
print(f"₹{avg_price_ac:,.2f}")

print("\nAverage Price of Non-AC Houses:")
print(f"₹{avg_price_non_ac:,.2f}")

plt.figure(figsize=(8, 6))

plt.bar(
    ["AC", "Non-AC"],
    [avg_price_ac, avg_price_non_ac],
    color=["steelblue", "orange"]
)

plt.title("Average House Prices: AC vs Non-AC")
plt.xlabel("House Type")
plt.ylabel("Average Price")
plt.ticklabel_format(
    style="plain",
    axis="y"
)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 3. Parking vs No Parking Average Price
# --------------------------------------------------

avg_price_parking = housing_data[
    housing_data["parking"] == "yes"
]["price"].mean()

avg_price_no_parking = housing_data[
    housing_data["parking"] == "no"
]["price"].mean()

print("\nAverage Price of Houses with Parking:")
print(f"₹{avg_price_parking:,.2f}")

print("\nAverage Price of Houses without Parking:")
print(f"₹{avg_price_no_parking:,.2f}")

plt.figure(figsize=(8, 6))

plt.bar(
    ["Parking", "No Parking"],
    [avg_price_parking, avg_price_no_parking],
    color=["green", "gray"]
)

plt.title("Average House Prices: Parking vs No Parking")
plt.xlabel("Parking Availability")
plt.ylabel("Average Price")
plt.ticklabel_format(
    style="plain",
    axis="y"
)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 4. Price Gap Analysis
# --------------------------------------------------

small_no_pref = housing_data[
    (housing_data["area"] < 5000) &
    (housing_data["prefarea"] == "no")
]

large_pref = housing_data[
    (housing_data["area"] > 5000) &
    (housing_data["prefarea"] == "yes")
]

avg_price_small_no_pref = small_no_pref["price"].mean()
avg_price_large_pref = large_pref["price"].mean()

price_gap = (
    avg_price_large_pref -
    avg_price_small_no_pref
)

print("\nAverage Price of Small Houses in Non-Preferred Areas:")
print(f"₹{avg_price_small_no_pref:,.2f}")

print("\nAverage Price of Large Houses in Preferred Areas:")
print(f"₹{avg_price_large_pref:,.2f}")

print("\nPrice Gap:")
print(f"₹{price_gap:,.2f}")