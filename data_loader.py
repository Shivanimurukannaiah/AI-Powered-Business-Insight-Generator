
import pandas as pd

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except Exception as e:
        raise ValueError(f"Error loading data: {e}")
