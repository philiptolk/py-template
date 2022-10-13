import os
import boto3

try:
    # For local development only
    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
except ModuleNotFoundError:
    pass

if os.getenv("is_localstack"):
    s3 = boto3.resource("s3", endpoint_url="http://localstack:4566")
else:
    s3 = boto3.resource("s3")


def test_me(bucket_name):
    print("get bucket")
    my_bucket = s3.Bucket(bucket_name)
    if my_bucket:
        print(my_bucket)
    print("got bucket")


def lambda_handler(event, context):
    test_me(bucket_name=event["bucket_name"])


if __name__ == "__main__":
    lambda_event = {"bucket_name": "s3-bucket-name"}
    lambda_context = []
    lambda_handler(lambda_event, lambda_context)
