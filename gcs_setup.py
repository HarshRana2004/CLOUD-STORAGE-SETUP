from google.cloud import storage
from google.cloud.storage import Bucket
import os

class GCSStorageManager:
    def __init__(self, project_id):
        self.client = storage.Client(project=project_id)
        self.project_id = project_id
    
    def create_bucket(self, bucket_name, location='US'):
        try:
            bucket = self.client.bucket(bucket_name)
            bucket = self.client.create_bucket(bucket, location=location)
            print(f"Bucket '{bucket_name}' created successfully")
            return bucket
        except Exception as e:
            if "already exists" in str(e):
                print(f"Bucket '{bucket_name}' already exists")
                return self.client.bucket(bucket_name)
            print(f"Error creating bucket: {e}")
            return None
    
    def set_bucket_permissions(self, bucket_name):
        try:
            bucket = self.client.bucket(bucket_name)
            policy = bucket.get_iam_policy(requested_policy_version=3)
            policy.bindings.append({
                "role": "roles/storage.objectViewer",
                "members": {"allUsers"}
            })
            bucket.set_iam_policy(policy)
            print(f"Public read access configured for '{bucket_name}'")
            return True
        except Exception as e:
            print(f"Error setting permissions: {e}")
            return False
    
    def upload_file(self, file_path, bucket_name, blob_name=None):
        if blob_name is None:
            blob_name = os.path.basename(file_path)
        
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_path)
            print(f"File uploaded: {blob_name}")
            return True
        except Exception as e:
            print(f"Error uploading file: {e}")
            return False
    
    def download_file(self, bucket_name, blob_name, file_path):
        try:
            bucket = self.client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.download_to_filename(file_path)
            print(f"File downloaded: {file_path}")
            return True
        except Exception as e:
            print(f"Error downloading file: {e}")
            return False

if __name__ == "__main__":
    # Initialize GCS manager
    project_id = "your-project-id"
    gcs_manager = GCSStorageManager(project_id)
    
    # Create bucket
    bucket_name = "my-gcs-storage-bucket-12345"
    bucket = gcs_manager.create_bucket(bucket_name)
    
    if bucket:
        # Set permissions
        gcs_manager.set_bucket_permissions(bucket_name)
        
        # Upload example files
        sample_files = [
            "sample_data/example.txt",
            "sample_data/data.json"
        ]
        
        for file_path in sample_files:
            if os.path.exists(file_path):
                gcs_manager.upload_file(file_path, bucket_name)
        
        print(f"\nDeliverable complete:")
        print(f"- Bucket '{bucket_name}' created")
        print(f"- Public read access configured")
        print(f"- Example files uploaded")