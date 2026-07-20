import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file.
    """
    return pd.read_csv(file_path)


def remove_identifier(df):
    """
    Remove the unique identifier column.
    """
    return df.drop(columns=["person_id"])


def split_features_target(df, target_column):
    """
    Split the dataset into features (X) and target (y).
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y