import boto3
import sagemaker
from sagemaker.sklearn.estimator import SKLearn

s3_bucket = "my-sagemaker-model-bucket"
role = "arn:aws:iam::<ACCOUNT_ID>:role/<SAGEMAKER_EXECUTION_ROLE>"

session = sagemaker.Session()
script_path = "train.py"

# Define the Scikit-Learn Estimator
sklearn_estimator = SKLearn(
    entry_point=script_path,
    role=role,
    instance_count=1,
    instance_type="ml.m5.large",
    framework_version="0.23-1",
    sagemaker_session=session
)

# Train the model
sklearn_estimator.fit(f"s3://{s3_bucket}/train.csv")
