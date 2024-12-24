from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def linear_regression_analysis(data, feature_columns, target_column):
    """
    Performs Linear Regression to predict a continuous variable.

    Args:
        data (pd.DataFrame): Dataset containing features and target column.
        feature_columns (list): List of column names used as features.
        target_column (str): Name of the target column.

    Returns:
        dict: A dictionary containing the model, predictions, and evaluation metrics.
    """
    try:
        X = data[feature_columns]
        y = data[target_column]

        # Train Linear Regression model
        model = LinearRegression()
        model.fit(X, y)

        # Predict on the training set
        predictions = model.predict(X)
        mse = mean_squared_error(y, predictions)
        print(f"Linear Regression completed. Mean Squared Error (MSE): {mse:.2f}")

        return {
            "model": model,
            "predictions": predictions,
            "mse": mse,
            "coefficients": model.coef_
        }
    except Exception as e:
        raise RuntimeError(f"Error in Linear Regression analysis: {e}")