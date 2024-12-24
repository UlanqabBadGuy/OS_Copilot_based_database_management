from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def clustering_analysis(data, n_clusters):
    """
    Performs K-Means clustering on the dataset.

    Args:
        data (pd.DataFrame): Dataset to cluster (numerical features only).
        n_clusters (int): Number of clusters to create.

    Returns:
        dict: A dictionary containing the model, cluster labels, and cluster centers.
    """
    try:
        model = KMeans(n_clusters=n_clusters, random_state=42)
        data['cluster'] = model.fit_predict(data)
        print(f"Clustering completed. Cluster Centers:\n{model.cluster_centers_}")

        # Plot the clusters (for 2D data)
        if data.shape[1] == 3:  # Assuming 2 features + cluster labels
            plt.scatter(data.iloc[:, 0], data.iloc[:, 1], c=data['cluster'], cmap='viridis', s=50)
            plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], c='red', marker='X', s=200)
            plt.title('K-Means Clustering')
            plt.xlabel('Feature 1')
            plt.ylabel('Feature 2')
            plt.show()

        return {
            "model": model,
            "cluster_labels": data['cluster'],
            "cluster_centers": model.cluster_centers_
        }
    except Exception as e:
        raise RuntimeError(f"Error in Clustering analysis: {e}")
