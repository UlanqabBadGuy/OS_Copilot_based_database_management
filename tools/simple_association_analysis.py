# 所需包
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def simple_association_analysis(data, min_support=0.1, min_confidence=0.5):
    """
    Performs a simple association rule mining using Apriori algorithm.

    Args:
        data (pd.DataFrame): One-hot encoded dataset for analysis.
        min_support (float): Minimum support threshold for frequent itemsets.
        min_confidence (float): Minimum confidence threshold for association rules.

    Returns:
        dict: A dictionary containing frequent itemsets and association rules.
    """
    try:
        # Step 1: Find frequent itemsets
        frequent_itemsets = apriori(data, min_support=min_support, use_colnames=True)
        print(f"Frequent Itemsets:\n{frequent_itemsets}\n")

        # Step 2: Generate association rules
        rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
        print(f"Association Rules:\n{rules}\n")

        return {
            "frequent_itemsets": frequent_itemsets,
            "rules": rules
        }
    except Exception as e:
        raise RuntimeError(f"Error in simple association analysis: {e}")