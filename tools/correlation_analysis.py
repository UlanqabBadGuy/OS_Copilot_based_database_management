import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv


def correlation_analysis(csv_file_path, target_column, output_txt_path, output_image_path):
    """
    Computes the correlation of all features with the target column from a CSV file,
    saves the correlation values to a text file, and plots a full heatmap of correlations.

    Args:
        csv_file_path (str): Path to the input CSV file containing the dataset.
        target_column (str): The name of the target column to calculate correlations with.
        output_txt_path (str): Path to save the correlation results as a text file.
        output_image_path (str): Path to save the correlation heatmap image.

    Returns:
        None: Saves results to a text file and an image.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Step 2: Extract header and data
        header = rows[0]  # First row as column names
        data = rows[1:]  # Remaining rows as data

        # Step 3: Convert to DataFrame
        df = pd.DataFrame(data, columns=header)

        # Ensure numeric data types for correlation
        df = df.apply(pd.to_numeric, errors='coerce')

        # Check if target_column exists in the dataset
        if target_column not in df.columns:
            raise ValueError(f"The target column '{target_column}' is not found in the dataset.")

        # Step 4: Compute correlations for all columns
        correlation_matrix = df.corr()

        # Step 5: Save correlation results with the target column to a text file
        correlations_with_target = correlation_matrix[target_column].drop(target_column)
        with open(output_txt_path, 'w') as txt_file:
            txt_file.write(f"Correlation Analysis with Target Column: {target_column}\n")
            txt_file.write("=" * 50 + "\n\n")
            for col, corr in correlations_with_target.items():
                txt_file.write(f"{col}: {corr:.4f}\n")
        print(f"Correlation results saved to {output_txt_path}")

        # Step 6: Plot the full correlation heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
        plt.title(f"Correlation Heatmap", fontsize=16)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(fontsize=10)
        plt.tight_layout()

        # Save the heatmap image
        plt.savefig(output_image_path, dpi=300)
        print(f"Correlation heatmap saved to {output_image_path}")
        plt.show()

    except Exception as e:
        raise RuntimeError(f"Error in correlation analysis: {e}")