import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split


def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
        file_path (str): Path to the dataset.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)


def remove_identifier(df):
    """
    Remove the unique identifier column.

    Parameters:
        df (DataFrame): Input dataset.

    Returns:
        DataFrame: Dataset without the identifier column.
    """
    return df.drop(columns=["person_id"])


def split_features_target(df, target_column):
    """
    Split the dataset into features (X) and target (y).

    Parameters:
        df (DataFrame): Input dataset.
        target_column (str): Name of the target column.

    Returns:
        tuple:
            X (DataFrame): Feature dataset.
            y (Series): Target variable.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return X, y


def identify_feature_types(X):
    """
    Identify numerical and categorical feature columns.

    Parameters:
        X (DataFrame): Feature dataset.

    Returns:
        tuple:
            numerical_features (list)
            categorical_features (list)
    """

    numerical_features = X.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    categorical_features = X.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    return numerical_features, categorical_features


def create_preprocessor(numerical_features, categorical_features):
    """
    Create a preprocessing pipeline for numerical and categorical features.

    Numerical Features:
        - StandardScaler

    Categorical Features:
        - OneHotEncoder

    Returns:
        ColumnTransformer: Complete preprocessing pipeline.
    """

    # Numerical Pipeline
    numerical_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler())
        ]
    )

    # Categorical Pipeline
    categorical_pipeline = Pipeline(
        steps=[
            ("encoder", OneHotEncoder(handle_unknown="ignore"))
        ]
    )

    # Combine both pipelines
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_pipeline, numerical_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )

    return preprocessor

def split_train_test(X, y, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )
