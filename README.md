# Cloud Storage Setup - Deliverable

## Quick Deploy

```
pip install -r requirements.txt
python deploy.py
```

## What's Included

**Bucket Setup:**
- Creates cloud storage bucket
- Configures public read access permissions
- Uploads example files automatically

**Example Files:**
- `sample_data/example.txt` - Text file
- `sample_data/data.json` - JSON data

**AWS S3 Setup:**

1. Configure credentials:
   ```
   set AWS_ACCESS_KEY_ID=your_access_key
   set AWS_SECRET_ACCESS_KEY=your_secret_key
   ```

2. Run setup:
   ```
   python aws_s3_setup.py
   ```

**Google Cloud Storage Setup:**

1. Set authentication:
   ```
   set GOOGLE_APPLICATION_CREDENTIALS=path\to\service-account-key.json
   ```

2. Update project_id in gcs_setup.py

3. Run setup:
   ```
   python gcs_setup.py
   ```

## Deliverable Output

✓ Bucket created with unique name  
✓ Public read access permissions configured  
✓ Example files uploaded and accessible