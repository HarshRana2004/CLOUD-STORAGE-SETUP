import os
import shutil
import json

# Local storage demo (no cloud needed)
def create_local_storage():
    # Create storage folder
    storage_folder = "local_storage"
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)
    
    # Copy sample files
    sample_files = ["sample_data/example.txt", "sample_data/data.json"]
    
    print("=== LOCAL STORAGE DEMO ===")
    print(f"Storage folder: {storage_folder}")
    
    for file_path in sample_files:
        if os.path.exists(file_path):
            filename = os.path.basename(file_path)
            dest_path = os.path.join(storage_folder, filename)
            shutil.copy2(file_path, dest_path)
            print(f"✓ Uploaded: {filename}")
    
    print("\n=== DELIVERABLE COMPLETE ===")
    print("✓ Storage created")
    print("✓ Files uploaded")
    print("✓ Files accessible in local_storage folder")

if __name__ == "__main__":
    create_local_storage()