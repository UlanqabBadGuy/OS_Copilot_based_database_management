import pandas as pd

def handle_missing_values(data, method='mean', columns=None):
    """
    Handles missing values in the dataset by filling or dropping them.

    Args:
        data (pd.DataFrame): The dataset to process.
        method (str): The method to handle missing values. Options: 'mean', 'median', 'mode', 'drop'.
        columns (list): List of columns to process. If None, all columns are processed.

    Returns:
        pd.DataFrame: The dataset with missing values handled.
    """
    try:
        if columns is None:
            columns = data.columns

        if method == 'mean':
            data[columns] = data[columns].fillna(data[columns].mean())
        elif method == 'median':
            data[columns] = data[columns].fillna(data[columns].median())
        elif method == 'mode':
            for col in columns:
                data[col] = data[col].fillna(data[col].mode()[0])
        elif method == 'drop':
            data = data.dropna(subset=columns)
        else:
            raise ValueError("Invalid method. Choose from 'mean', 'median', 'mode', 'drop'.")

        return data
    except Exception as e:
        raise RuntimeError(f"Error in handling missing values: {e}")