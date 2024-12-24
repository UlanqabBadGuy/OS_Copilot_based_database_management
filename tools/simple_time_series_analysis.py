import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

def simple_time_series_analysis(data, date_column, value_column, forecast_steps=5):
    """
    Performs a simple time series analysis and forecasting using ARIMA.

    Args:
        data (pd.DataFrame): Dataset containing time series data.
        date_column (str): Column containing date information.
        value_column (str): Column containing values to predict.
        forecast_steps (int): Number of steps to forecast into the future.

    Returns:
        dict: A dictionary containing the ARIMA model, forecast values, and residuals.
    """
    try:
        # Step 1: Convert date column to datetime and set it as the index
        data[date_column] = pd.to_datetime(data[date_column])
        data.set_index(date_column, inplace=True)

        # Step 2: Fit ARIMA model
        model = ARIMA(data[value_column], order=(1, 1, 1))  # (p, d, q)
        result = model.fit()

        # Step 3: Forecast future values
        forecast = result.forecast(steps=forecast_steps)
        print(f"Forecasted Values:\n{forecast}\n")

        # Step 4: Plot actual values and forecast
        plt.figure(figsize=(10, 5))
        plt.plot(data[value_column], label="Actual")
        plt.plot(range(len(data), len(data) + forecast_steps), forecast, label="Forecast", color='red')
        plt.legend()
        plt.title("Time Series Forecast")
        plt.show()

        return {
            "model": result,
            "forecast": forecast,
            "residuals": result.resid
        }
    except Exception as e:
        raise RuntimeError(f"Error in simple time series analysis: {e}")