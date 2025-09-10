from botocore.exceptions import NoCredentialsError
import boto3
import os

class Uploader:
    def __init__(self, s3_bucket_name):
        self.s3_bucket_name = s3_bucket_name
        self.s3_client = boto3.client('s3')

    def validate_file(self, file_path):
        if not os.path.isfile(file_path):
            raise ValueError("File does not exist.")
        if not file_path.lower().endswith(('.pdf', '.docx', '.mp4', '.jpg', '.png')):
            raise ValueError("Unsupported file type.")
        return True

    def upload_file(self, file_path):
        self.validate_file(file_path)
        file_name = os.path.basename(file_path)
        try:
            self.s3_client.upload_file(file_path, self.s3_bucket_name, file_name)
            return f"File {file_name} uploaded successfully to {self.s3_bucket_name}."
        except NoCredentialsError:
            raise Exception("Credentials not available for S3 upload.")
        except Exception as e:
            raise Exception(f"An error occurred while uploading the file: {str(e)}")