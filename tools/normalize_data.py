from sklearn.preprocessing import MinMaxScaler

def normalize_data(data, columns):
    """
    Normalizes numerical features to a range of [0, 1].

    Args:
        data (pd.DataFrame): The dataset to process.
        columns (list): List of column names to normalize.

    Returns:
        pd.DataFrame: The dataset with normalized columns.
    """
    try:
        scaler = MinMaxScaler()
        data[columns] = scaler.fit_transform(data[columns])
        return data
    except Exception as e:
        raise RuntimeError(f"Error in data normalization: {e}")