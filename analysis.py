import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
housing_data = pd.read_csv('housing.csv')

# 1. Price Range Distribution
price_ranges = [0, 2500000, 5000000, 7500000, 10000000, float('inf')]
labels = ['0-25 lakhs', '26-50 lakhs', '51-75 lakhs', '76-100 lakhs', '100+ lakhs']

housing_data['price_range'] = pd.cut(housing_data['price'], bins=price_ranges, labels=labels)
price_range_counts = housing_data['price_range'].value_counts().sort_index()

print(price_range_counts)

plt.figure(figsize=(10,6))
plt.plot(price_range_counts.index.astype(str), price_range_counts.values, marker='o')
plt.title('Price Range Distribution')
plt.xlabel('Price Range')
plt.ylabel('Number of Houses')
plt.xticks(rotation=45)
plt.show()

# 2. AC vs Non-AC
avg_price_ac = housing_data[housing_data['AC'] == 'Yes']['price'].mean()
avg_price_non_ac = housing_data[housing_data['AC'] == 'No']['price'].mean()

plt.figure(figsize=(8,6))
plt.bar(['AC', 'Non-AC'], [avg_price_ac, avg_price_non_ac])
plt.title('Average House Prices for AC and Non-AC Houses')
plt.xlabel('Type')
plt.ylabel('Average Price')
plt.show()

# 3. Parking vs Price
avg_price_parking = housing_data[housing_data['parking'] == 'Yes']['price'].mean()
avg_price_no_parking = housing_data[housing_data['parking'] == 'No']['price'].mean()

plt.figure(figsize=(8,6))
plt.bar(['Parking', 'No Parking'], [avg_price_parking, avg_price_no_parking])
plt.title('Parking vs Price')
plt.xlabel('Parking')
plt.ylabel('Average Price')
plt.show()

# 4. Price Gap Analysis
avg_price_small_no_pref = housing_data[(housing_data['area'] < 5000) & (housing_data['prefarea'] == 'No')]['price'].mean()
avg_price_large_pref = housing_data[(housing_data['area'] > 5000) & (housing_data['prefarea'] == 'Yes')]['price'].mean()

price_gap = avg_price_large_pref - avg_price_small_no_pref

print("Price Gap:", price_gap)