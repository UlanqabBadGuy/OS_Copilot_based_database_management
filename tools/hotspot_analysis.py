import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def hotspot_analysis(csv_file_path, x_column, y_column, value_column, output_image_path):
    """
    Performs hotspot analysis using data from a CSV file and plots a heatmap.

    Args:
        csv_file_path (str): Path to the CSV file containing the dataset.
        x_column (str): Name of the column to use as the X-axis.
        y_column (str): Name of the column to use as the Y-axis.
        value_column (str): Name of the column to use as the heatmap value.
        output_image_path (str): Path to save the heatmap image.

    Returns:
        None: Displays and saves the heatmap.
    """
    try:
        # Step 1: Read data from CSV file
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]

        # Step 2: Extract X, Y, and value columns
        x_values = [row[x_column] for row in data]
        y_values = [row[y_column] for row in data]
        heat_values = [float(row[value_column]) for row in data]

        # Step 3: Create a pivot table for the heatmap
        unique_x = sorted(set(x_values))
        unique_y = sorted(set(y_values))
        heatmap_data = np.zeros((len(unique_y), len(unique_x)))

        for x, y, value in zip(x_values, y_values, heat_values):
            x_idx = unique_x.index(x)
            y_idx = unique_y.index(y)
            heatmap_data[y_idx, x_idx] = value

        # Step 4: Plot the heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(
            heatmap_data,
            annot=True,  # Show the heatmap values
            fmt=".1f",  # Format for annotations
            xticklabels=unique_x,
            yticklabels=unique_y,
            cmap="YlGnBu"  # Beautiful color map
        )
        plt.title("Hotspot Analysis Heatmap", fontsize=16)
        plt.xlabel(x_column, fontsize=14)
        plt.ylabel(y_column, fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Save and show the heatmap
        plt.savefig(output_image_path, dpi=300)
        print(f"Heatmap saved to {output_image_path}")
        plt.show()

    except Exception as e:
        raise RuntimeError(f"Error in hotspot analysis: {e}")