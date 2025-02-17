import argparse
import pandas as pd
import numpy as np
import joblib
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    # Argument parser for SageMaker inputs
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-file", type=str, default="/opt/ml/input/data/training/train.csv")
    parser.add_argument("--model-dir", type=str, default="/opt/ml/model")
    args = parser.parse_args()

    # Load dataset
    df = pd.read_csv(args.train_file)
    X = df[['feature1', 'feature2']].values  # Replace with actual feature names
    y = df['target'].values

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Save the model
    model_path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
