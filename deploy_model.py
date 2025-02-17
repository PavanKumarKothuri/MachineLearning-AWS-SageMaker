from sagemaker.sklearn.model import SKLearnModel
import boto3

role = "arn:aws:iam::<ACCOUNT_ID>:role/<SAGEMAKER_EXECUTION_ROLE>"
s3_model_path = "s3://my-sagemaker-model-bucket/sagemaker-scikit/model.tar.gz"

# Load the trained model
model = SKLearnModel(
    model_data=s3_model_path,
    role=role,
    entry_point="train.py",
    framework_version="0.23-1"
)

# Deploy the model
predictor = model.deploy(instance_type="ml.m5.large", initial_instance_count=1)
print("Model deployed successfully!")
