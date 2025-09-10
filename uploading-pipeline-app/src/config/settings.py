from pathlib import Path
import os

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# AWS S3 configuration
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'your_access_key_id')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'your_secret_access_key')
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME', 'your_bucket_name')
AWS_S3_REGION = os.getenv('AWS_S3_REGION', 'your_region')

# LanceDB configuration
LANCEDB_URL = os.getenv('LANCEDB_URL', 'your_lancedb_url')
LANCEDB_API_KEY = os.getenv('LANCEDB_API_KEY', 'your_api_key')

# Other configurations
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
EMBEDDING_DIMENSION = 512  # Example dimension for embeddings
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10 MB limit for uploads

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)