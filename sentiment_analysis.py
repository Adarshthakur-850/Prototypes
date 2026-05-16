import os
import logging
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import mlflow
import mlflow.sklearn
import joblib
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def train_model():
    try:
        mlflow.set_tracking_uri("file:./mlruns")
        mlflow.set_experiment("sentiment-analysis")
        data = {
            "text": [
                "I love this product, it's amazing!",
                "This is the worst experience I've had.",
                "Not bad, could be better.",
                "Absolutely fantastic service!",
                "I hate it, terrible",
                "Best purchase ever",
                "Do not buy this",
                "It is okay, average",
                "Highly recommended",
                "Waste of money"
            ],
            "label": [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
        }
        df = pd.DataFrame(data)
        X_train, X_test, y_train, y_test = train_test_split(
            df["text"], df["label"], test_size=0.2, random_state=42
        )
        pipeline = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=5000)),
            ("clf", LogisticRegression(max_iter=1000))
        ])
        with mlflow.start_run():
            pipeline.fit(X_train, y_train)
            preds = pipeline.predict(X_test)
            acc = accuracy_score(y_test, preds)
            mlflow.log_metric("accuracy", acc)
            mlflow.log_param("model_type", "LogisticRegression")
            mlflow.sklearn.log_model(pipeline, "model")
            os.makedirs("models", exist_ok=True)
            model_path = os.path.join("models", "sentiment_model.pkl")
            joblib.dump(pipeline, model_path)
            print(f"Model saved to {model_path} (accuracy: {acc:.4f})")
            return model_path, acc
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise
if __name__ == "__main__":
    train_model()