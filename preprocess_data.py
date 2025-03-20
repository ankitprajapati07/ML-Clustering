import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ML Dataset.csv', delimiter=';')
#print(data.head(5))

#Remove Duplicates
data_no_duplicates = data.drop_duplicates()
print(f"Rows after removing duplicates: {len(data_no_duplicates)} (Original: {len(data)})")

# Outlier Detection and Removal
# using a simple statistical method: remove points beyond 1.5 * IQR (Interquartile Range)
# This is a common approach for outlier detection
Q1 = data_no_duplicates.quantile(0.25)
Q3 = data_no_duplicates.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out outliers
data_cleaned = data_no_duplicates[
    (data_no_duplicates['Longitude'].between(lower_bound['Longitude'], upper_bound['Longitude'])) &
    (data_no_duplicates['Latitude'].between(lower_bound['Latitude'], upper_bound['Latitude']))
]
print(f"Rows after removing outliers: {len(data_cleaned)}")

# the cleaned data with a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data_cleaned['Longitude'], data_cleaned['Latitude'], s=10, alpha=0.5)
plt.title('Geospatial Data After Preprocessing')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.show()

# Prepare the data for clustering
# We are use raw coordinates for now, but we can switch to Haversine distance if needed
coords = data_cleaned[['Longitude', 'Latitude']].values

output_file = 'locations_preprocessed.csv'
data_cleaned.to_csv(output_file, index=False)
#print(f"Preprocessed dataset saved to: {output_file}")

#results:
#Rows after removing duplicates: 5930 (Original: 9895)
#Rows after removing outliers: 5878