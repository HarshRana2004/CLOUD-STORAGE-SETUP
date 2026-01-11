import boto3
import os

# Put your credentials here temporarily
AWS_ACCESS_KEY_ID = "your_access_key_here"
AWS_SECRET_ACCESS_KEY = "your_secret_key_here"

# Create S3 client with credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name='us-east-1'
)

bucket_name = "my-test-bucket-12345"

try:
    # Create bucket
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created!")
    
    # Upload files
    s3_client.upload_file('sample_data/example.txt', bucket_name, 'example.txt')
    s3_client.upload_file('sample_data/data.json', bucket_name, 'data.json')
    print("Files uploaded!")
    
except Exception as e:
    print(f"Error: {e}")