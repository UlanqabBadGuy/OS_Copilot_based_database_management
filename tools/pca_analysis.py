from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv

def pca_analysis(csv_file_path, selected_columns, output_image_path):
    """
    Performs PCA on selected features from a CSV file and visualizes the first two principal components.

    Args:
        csv_file_path (str): Path to the CSV file containing the dataset.
        selected_columns (list): List of column names to use for PCA.
        output_image_path (str): Path to save the PCA scatter plot.

    Returns:
        None: Saves the PCA scatter plot.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        # Step 2: Extract selected columns and convert to numerical values
        features = [[float(row[col]) for col in selected_columns] for row in data]

        # Step 3: Perform PCA
        pca = PCA(n_components=2)  # Reduce to 2 components for visualization
        pca_features = pca.fit_transform(features)

        # Step 4: Visualize PCA results
        plt.figure(figsize=(10, 8))
        plt.scatter(pca_features[:, 0], pca_features[:, 1], c='blue', alpha=0.7, s=50)
        plt.title('PCA Visualization', fontsize=16)
        plt.xlabel('Principal Component 1', fontsize=14)
        plt.ylabel('Principal Component 2', fontsize=14)
        plt.tight_layout()

        # Save the plot
        plt.savefig(output_image_path, dpi=300)
        print(f"PCA scatter plot saved to {output_image_path}")
        plt.show()

    except Exception as e:
        raise RuntimeError(f"Error in PCA visualization: {e}")