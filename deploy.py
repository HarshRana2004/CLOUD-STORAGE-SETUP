import subprocess
import sys
import os

def run_setup():
    print("=== CLOUD STORAGE DELIVERABLE SETUP ===\n")
    
    # Check if sample files exist
    sample_files = ["sample_data/example.txt", "sample_data/data.json"]
    for file_path in sample_files:
        if not os.path.exists(file_path):
            print(f"Error: {file_path} not found")
            return False
    
    print("Sample files ready:")
    for file_path in sample_files:
        print(f"  ✓ {file_path}")
    
    print("\nChoose cloud provider:")
    print("1. AWS S3")
    print("2. Google Cloud Storage")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == "1":
        print("\nRunning AWS S3 setup...")
        try:
            subprocess.run([sys.executable, "aws_s3_setup.py"], check=True)
        except subprocess.CalledProcessError:
            print("Error running AWS S3 setup")
            return False
    elif choice == "2":
        print("\nRunning Google Cloud Storage setup...")
        try:
            subprocess.run([sys.executable, "gcs_setup.py"], check=True)
        except subprocess.CalledProcessError:
            print("Error running GCS setup")
            return False
    else:
        print("Invalid choice")
        return False
    
    print("\n=== DELIVERABLE COMPLETE ===")
    return True

if __name__ == "__main__":
    run_setup()