from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv

def clustering_analysis_from_csv(
        csv_file_path, selected_columns, n_clusters, output_image_path):
    """
    Performs K-Means clustering on selected features from a CSV file,
    plots results with enhanced visualization, and saves the plot.

    Args:
        csv_file_path (str): Path to the CSV file containing the dataset.
        selected_columns (list): List of column names to use for clustering.
        n_clusters (int): Number of clusters to create.
        output_image_path (str): Path to save the scatter plot image.

    Returns:
        dict: A dictionary containing the model, cluster labels, and cluster centers.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        # Step 2: Extract selected columns and convert to numerical values
        features = [[float(row[col]) for col in selected_columns] for row in data]

        # Step 3: Perform K-Means clustering
        model = KMeans(n_clusters=n_clusters, random_state=42)
        labels = model.fit_predict(features)
        cluster_centers = model.cluster_centers_
        print(f"Clustering completed. Cluster Centers:\n{cluster_centers}")

        # Step 4: Visualize clustering results
        if len(selected_columns) > 2:
            # Perform PCA for dimensionality reduction if more than 2 features
            pca = PCA(n_components=2)
            reduced_features = pca.fit_transform(features)
            reduced_centers = pca.transform(cluster_centers)
            x_label, y_label = "PCA Component 1", "PCA Component 2"
        else:
            # Use original features if only 2 dimensions
            reduced_features = features
            reduced_centers = cluster_centers
            x_label, y_label = selected_columns[0], selected_columns[1]

        plt.figure(figsize=(10, 8))
        plt.scatter(
            [point[0] for point in reduced_features],
            [point[1] for point in reduced_features],
            c=labels,
            cmap='viridis',
            s=50,
            alpha=0.8,
            label="Data Points"
        )
        plt.scatter(
            [center[0] for center in reduced_centers],
            [center[1] for center in reduced_centers],
            c='red',
            marker='X',
            s=200,
            label='Cluster Centers'
        )
        plt.title('K-Means Clustering Results', fontsize=16)
        plt.xlabel(x_label, fontsize=14)
        plt.ylabel(y_label, fontsize=14)
        plt.legend()
        plt.tight_layout()

        # Save the plot
        plt.savefig(output_image_path, dpi=300)
        print(f"Cluster plot saved to {output_image_path}")
        plt.show()

        # Step 5: Return clustering results
        return {
            "model": model,
            "cluster_labels": labels,
            "cluster_centers": cluster_centers.tolist()
        }
    except Exception as e:
        raise RuntimeError(f"Error in Clustering analysis: {e}")