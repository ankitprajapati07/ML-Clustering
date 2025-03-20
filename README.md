# Geospatial Data Clustering Project

## Overview
This project involves clustering geospatial data (latitude, longitude) using Python. The dataset, containing 9,895 locations, was preprocessed and clustered with four methods: K-Means, DBSCAN, HDBSCAN, and Hierarchical Clustering. DBSCAN was selected for its highest silhouette score (0.548). The final script was executed on an AWS EC2 t2.micro instance.

### Why DBSCAN?
DBSCAN was chosen over K-Means, HDBSCAN, and Hierarchical Clustering due to its superior silhouette score (0.548 with `eps=0.2`) and ability to handle noise in the dataset, which has varying densities. This makes DBSCAN ideal for identifying natural clusters, such as population centers.

## Repository Structure
- **Results/**
  - `final_clusters.png`: Plot of the final clusters.
  - `locations_clustered.csv`: Preprocessed dataset with cluster labels.
- **Data_exploration_and_preprocessing.ipynb**: Notebook for initial data exploration and preprocessing.
- **final_clustering_script.py**: Script for final clustering with DBSCAN.
- **pre_process_data.py**: Script for preprocessing the original dataset.
- **requirements.txt**: List of required Python libraries.
- **README.md**: This file.

## Major Steps Taken

### 1. Data Exploration
- The dataset (9,895 rows, 2 columns: Longitude, Latitude) was loaded.
- Summary statistics and a scatter plot were used for exploration.
- Duplicates (3,965 rows) and outliers (52 rows) were identified.

### 2. Data Preprocessing
- Duplicates were removed, leaving 5,930 rows.
- Outliers were removed using the IQR method, resulting in 5,878 rows.
- The preprocessed dataset was saved as `locations_preprocessed.csv`.

### 3. Clustering
- Four methods were tested:
  - K-Means: Best score 0.526 (`n_clusters=5`).
  - DBSCAN: Best score 0.548 (`eps=0.2`).
  - HDBSCAN: Best score 0.412 (`min_cluster_size=10`).
  - Hierarchical: Best score 0.490 (`n_clusters=4`).
- DBSCAN (`eps=0.2`) was selected for final clustering.

### 4. Final Clustering
- Clustering was performed with DBSCAN (`eps=0.2`, `min_samples=5`).
- Results were saved as `locations_clustered.csv` and `final_clusters.png`.

### 5. AWS EC2 Deployment
- A t2.micro instance (Amazon Linux 2) was launched.
- Connection was established via SSH, and Python/libraries were installed in a virtual environment.
- The script was executed, outputs were retrieved, and the instance was terminated.

## How to Run Locally

### Prerequisites
- Python 3.6 or higher
  - Install Python: Download from [python.org](https://www.python.org/downloads/) or use a package manager:
    ```bash
    # On Windows (using Chocolatey)
    choco install python

### Steps to Run
## Clone the Repository:
  - https://github.com/ankitprajapati07/ML-Clustering

## Set Up a Virtual Environment:
  - python -m venv venv
  - source venv/Scripts/activate  # On Windows

## Install Required Libraries:
   - pip install -r requirements.txt
## Run the Final Clustering Script: Ensure locations_preprocessed.csv is in the same directory, then:
   - python final_clustering_script.py
