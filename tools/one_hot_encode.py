import pandas as pd

def one_hot_encode(data, columns):
    """
    Performs one-hot encoding for categorical columns.

    Args:
        data (pd.DataFrame): The dataset to process.
        columns (list): List of column names to encode.

    Returns:
        pd.DataFrame: The dataset with one-hot encoded columns.
    """
    try:
        data = pd.get_dummies(data, columns=columns)
        return data
    except Exception as e:
        raise RuntimeError(f"Error in one-hot encoding: {e}")