import pandas as pd


def load_data(file_path):
    """Load dataset from CSV."""
    return pd.read_csv(file_path)


def remove_identifier(df):
    """Remove identifier column."""
    return df.drop(columns=["person_id"])


def split_features_target(df, target_column):
    """Split dataset into features and target."""
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y


def identify_feature_types(X):
    """
    Identify numerical and categorical features.
    """
    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    return numerical_features, categorical_features