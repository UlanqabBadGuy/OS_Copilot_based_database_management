from sklearn.preprocessing import StandardScaler

def standardize_data(data, columns):
    """
    Standardizes numerical features to have zero mean and unit variance.

    Args:
        data (pd.DataFrame): The dataset to process.
        columns (list): List of column names to standardize.

    Returns:
        pd.DataFrame: The dataset with standardized columns.
    """
    try:
        scaler = StandardScaler()
        data[columns] = scaler.fit_transform(data[columns])
        return data
    except Exception as e:
        raise RuntimeError(f"Error in data standardization: {e}")