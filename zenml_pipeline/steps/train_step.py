from zenml import step
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import mlflow
import joblib

@step
def train_model() -> str:
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    model = LogisticRegression(solver='lbfgs', penalty='l2', max_iter=200)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)

    # Log parameters and metric to MLflow
    mlflow.log_param("solver", "lbfgs")
    mlflow.log_param("penalty", "l2")
    mlflow.log_metric("accuracy", accuracy)

    # Save the model
    joblib.dump(model, "inference_api/model.pkl")
    return "inference_api/model.pkl"
