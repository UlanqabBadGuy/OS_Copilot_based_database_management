# 所需包
from transformers import pipeline
import pandas as pd

def simple_sentiment_analysis(data, text_column):
    """
    Performs sentiment analysis on a column of text data from a Pandas DataFrame.

    Args:
        data (pd.DataFrame): A Pandas DataFrame containing the text data.
        text_column (str): The name of the column containing text for sentiment analysis.

    Returns:
        pd.DataFrame: The original DataFrame with two new columns:
                      'sentiment' (classification label) and 'confidence' (confidence score).
    """
    try:
        # Step 1: Ensure the specified column exists
        if text_column not in data.columns:
            raise ValueError(f"Column '{text_column}' not found in the DataFrame.")

        # Step 2: Extract text data
        texts = data[text_column].astype(str).tolist()

        # Step 3: Initialize sentiment analysis pipeline
        sentiment_pipeline = pipeline("sentiment-analysis")

        # Step 4: Perform sentiment analysis
        results = sentiment_pipeline(texts)

        # Step 5: Append sentiment results to the original DataFrame
        data['sentiment'] = [result['label'] for result in results]
        data['confidence'] = [result['score'] for result in results]

        return data
    except Exception as e:
        raise RuntimeError(f"Error in sentiment analysis: {e}")