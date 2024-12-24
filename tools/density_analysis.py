import seaborn as sns
import matplotlib.pyplot as plt
import csv

def density_analysis(csv_file_path, column, output_image_path):
    """
    Plots a kernel density estimation (KDE) curve for a given column from a CSV file.

    Args:
        csv_file_path (str): Path to the CSV file containing the dataset.
        column (str): The column name to use for density estimation.
        output_image_path (str): Path to save the KDE plot.

    Returns:
        None: Saves the KDE plot.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        # Step 2: Extract selected column and convert to numerical values
        values = [float(row[column]) for row in data]

        # Step 3: Plot KDE curve
        plt.figure(figsize=(10, 8))
        sns.kdeplot(values, fill=True, color='blue', alpha=0.7)
        plt.title(f'Density Estimation for {column}', fontsize=16)
        plt.xlabel(column, fontsize=14)
        plt.ylabel('Density', fontsize=14)
        plt.tight_layout()

        # Save the plot
        plt.savefig(output_image_path, dpi=300)
        print(f"KDE plot saved to {output_image_path}")
        plt.show()

    except Exception as e:
        raise RuntimeError(f"Error in density estimation: {e}")