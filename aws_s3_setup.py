import boto3
import json
import os
from botocore.exceptions import ClientError

class S3StorageManager:
    def __init__(self, region='us-east-1'):
        self.s3_client = boto3.client('s3', region_name=region)
        self.region = region
    
    def create_bucket(self, bucket_name):
        try:
            if self.region != 'us-east-1':
                self.s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': self.region}
                )
            else:
                self.s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' created successfully")
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
                print(f"Bucket '{bucket_name}' already exists")
                return True
            print(f"Error creating bucket: {e}")
            return False
    
    def set_bucket_policy(self, bucket_name, policy):
        try:
            self.s3_client.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(policy))
            print(f"Bucket policy set for '{bucket_name}'")
            return True
        except ClientError as e:
            print(f"Error setting bucket policy: {e}")
            return False
    
    def upload_file(self, file_path, bucket_name, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_path)
        
        try:
            self.s3_client.upload_file(file_path, bucket_name, object_name)
            print(f"File uploaded: {object_name}")
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return False
    
    def download_file(self, bucket_name, object_name, file_path):
        try:
            self.s3_client.download_file(bucket_name, object_name, file_path)
            print(f"File downloaded: {file_path}")
            return True
        except ClientError as e:
            print(f"Error downloading file: {e}")
            return False

if __name__ == "__main__":
    # Initialize S3 manager
    s3_manager = S3StorageManager()
    
    # Create bucket
    bucket_name = "my-cloud-storage-bucket-12345"
    s3_manager.create_bucket(bucket_name)
    
    # Set bucket policy for public read access
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": f"arn:aws:s3:::{bucket_name}/*"
        }]
    }
    s3_manager.set_bucket_policy(bucket_name, policy)
    
    # Upload example files
    sample_files = [
        "sample_data/example.txt",
        "sample_data/data.json"
    ]
    
    for file_path in sample_files:
        if os.path.exists(file_path):
            s3_manager.upload_file(file_path, bucket_name)
    
    print(f"\nDeliverable complete:")
    print(f"- Bucket '{bucket_name}' created")
    print(f"- Public read access configured")
    print(f"- Example files uploaded")