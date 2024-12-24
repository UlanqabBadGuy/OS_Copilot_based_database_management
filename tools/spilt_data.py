from sklearn.model_selection import train_test_split

def split_data(data, target_column, test_size=0.2, random_state=1):
    """
    Splits the dataset into training and testing sets.

    Args:
        data (pd.DataFrame): The dataset to split.
        target_column (str): The target column for supervised learning.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.

    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    try:
        X = data.drop(columns=[target_column])
        y = data[target_column]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        raise RuntimeError(f"Error in splitting data: {e}")