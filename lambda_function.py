import boto3
import json
import numpy as np

sagemaker_runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    endpoint_name = "sagemaker-scikit-endpoint"
    payload = json.loads(event["body"])
    
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType="application/json",
        Body=json.dumps(payload)
    )
    
    prediction = json.loads(response["Body"].read().decode())
    
    return {
        "statusCode": 200,
        "body": json.dumps({"prediction": prediction})
    }
