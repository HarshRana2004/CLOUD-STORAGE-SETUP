import os
import boto3

# Test credentials
print("Testing AWS credentials...")

# Check environment variables
access_key = os.environ.get('ENTER_YOU_ACCESS_KEY')
secret_key = os.environ.get('ENTER_YOUR_SECRET_KEY')

if access_key and secret_key:
    print(f"Access Key: {access_key[:10]}...")
    print(f"Secret Key: {secret_key[:10]}...")
    
    try:
        # Test connection
        s3 = boto3.client('s3')
        s3.list_buckets()
        print("✓ Credentials working!")
    except Exception as e:
        print(f"✗ Credentials invalid: {e}")
else:
    print("✗ No credentials found")
    print("\nSet credentials first:")
    print("set AWS_ACCESS_KEY_ID=your_key")
    print("set AWS_SECRET_ACCESS_KEY=your_secret")