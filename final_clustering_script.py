import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Load the preprocessed dataset
print("Loading preprocessed dataset...")
data_cleaned = pd.read_csv('locations_preprocessed.csv')
coords = data_cleaned[['Longitude', 'Latitude']].values

# Final clustering with DBSCAN (eps=0.2)
print("Running DBSCAN clustering...")
dbscan_final = DBSCAN(eps=0.2, min_samples=5)
dbscan_final_labels = dbscan_final.fit_predict(coords)
dbscan_final_silhouette = silhouette_score(coords, dbscan_final_labels) if len(set(dbscan_final_labels)) > 1 else -1

# the final silhouette score
print(f"Final DBSCAN (eps=0.2) Silhouette Score: {dbscan_final_silhouette:.3f}")

# Adding cluster labels to the DataFrame
data_cleaned['Cluster'] = dbscan_final_labels

# Saving the dataset with cluster labels
print("Saving clustered dataset...")
data_cleaned.to_csv('locations_clustered.csv', index=False)
print("Clustered dataset saved to: locations_clustered.csv")

# Visualizing the final clusters and saving the plot
print("Generating and saving cluster plot...")
plt.figure(figsize=(10, 6))
plt.scatter(coords[:, 0], coords[:, 1], c=dbscan_final_labels, s=10, cmap='viridis')
plt.title(f'Final Clustering with DBSCAN (eps=0.2, Silhouette: {dbscan_final_silhouette:.3f})')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.savefig('final_clusters.png')
print("Cluster plot saved to: final_clusters.png")