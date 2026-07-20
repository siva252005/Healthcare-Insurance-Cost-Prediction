from sklearn.linear_model import LinearRegression


def train_linear_regression(X_train, y_train):
    """
    Train a Linear Regression model.

    Parameters:
        X_train: Training features
        y_train: Training target

    Returns:
        Trained Linear Regression model
    """

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

from sklearn.tree import DecisionTreeRegressor

def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree Regressor.

    Parameters:
        X_train: Training features
        y_train: Training target

    Returns:
        Trained Decision Tree model
    """

    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)

    return model

from sklearn.ensemble import RandomForestRegressor

def train_random_forest(X_train, y_train):
    """
    Train a Random Forest Regressor.

    Parameters:
        X_train: Training features
        y_train: Training target

    Returns:
        Trained Random Forest model
    """

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    return model
from sklearn.ensemble import GradientBoostingRegressor

def train_gradient_boosting(X_train, y_train):
    """
    Train a Gradient Boosting Regressor.

    Parameters:
        X_train: Training features
        y_train: Training target

    Returns:
        Trained Gradient Boosting model
    """

    model = GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=3,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model