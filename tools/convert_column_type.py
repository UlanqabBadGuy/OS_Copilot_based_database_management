import pandas as pd

def convert_column_type(data, column, dtype):
    """
    Converts a single column to the specified data type.

    Args:
        data (pd.DataFrame): The dataset to process.
        column (str): The column name to convert.
        dtype (type): The target data type (e.g., int, float, str).

    Returns:
        pd.DataFrame: The dataset with the converted column type.
    """
    try:
        data[column] = data[column].astype(dtype)
        print(f"Column '{column}' converted to {dtype}.")
        return data
    except Exception as e:
        raise RuntimeError(f"Error in converting column '{column}' to {dtype}: {e}")