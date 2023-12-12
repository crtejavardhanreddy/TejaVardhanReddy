from minio import Minio
from minio.error import S3Error
import os

class MinioHandler:
    def __init__(self, endpoint, access_key, secret_key, secure=False):
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure)

    def create_bucket(self, bucket_name):
        try:
            if self.client.bucket_exists(bucket_name):
                return f"Bucket '{bucket_name}' already exists."
            self.client.make_bucket(bucket_name)
            print(f"Bucket '{bucket_name}' created successfully")
        except S3Error as e:
            print(f"Error: {e}")

    def upload_directory(self, bucket_name, directory_path):
        for root, dir, files in os.walk(directory_path):
            for file in files:
                local_path = os.path.join(root, file)
                object_name = os.path.relpath(local_path, directory_path).replace(os.path.sep, "/")
                try:
                    self.client.fput_object(bucket_name=bucket_name, object_name=object_name, file_path=local_path)
                    print(f"Uploaded from {local_path} to {bucket_name}")
                except S3Error as e:
                    print(f"Error while uploading directory: {e}")

    def upload_file(self, bucket_name, object_name, upload_file_path):
        try:
            self.client.fput_object(bucket_name=bucket_name, object_name=object_name, file_path=upload_file_path)
            print("File uploaded")
        except Exception as e:
            print(f"Error in Uploading model: {e}")

    def download_file(self, bucket_name, object_name, save_file_path):
        try:
            self.client.fget_object(bucket_name=bucket_name, object_name=object_name, file_path=save_file_path)
            print("File downloaded")
        except Exception as e:
            print(f"Error in downloading: {e}")

    def delete_bucket(self, bucket_name):
        try:
            self.client.remove_bucket(bucket_name)
            print(f"Bucket deleted {bucket_name}")
        except Exception as e:
            print(f"Error: {e}")

    def delete_files(self, bucket_name):
        try:
            objects = self.client.list_objects(bucket_name, recursive=True)
            for obj in objects:
                self.client.remove_object(bucket_name, obj.object_name)
                print(f"Deleted: {obj.object_name}")
        except S3Error as e:
            print(f"Error: {e}")

    def list_all_buckets(self):
        try:
            buckets = self.client.list_buckets()
            for bucket in buckets:
                print(bucket.name)
        except S3Error as e:
            print(f"Error{e}")

# Example Usage:
minio_handler = MinioHandler(
    endpoint="127.0.0.1:9000",
    access_key="Wi0JuwXy67cnOQEvZLNB",
    secret_key="Hkv08g9TYqrOn1on8qc5GAiM9ba7hK3IIYkxEUcr"
)

# minio_handler.create_bucket("bert-bucket")
# minio_handler.upload_directory("bert-bucket", r"C:\Users\User\Desktop\MINIO\MinIO_C")
# minio_handler.upload_file("bert-bucket", "distilbert-base-cased", r"C:\Users\User\Desktop\MINIO\app.py")
# minio_handler.download_file("bert-bucket", "distilbert-base-cased", "test_save")
# minio_handler.delete_files("bert-bucket")
# minio_handler.delete_bucket("bert-bucket")
# minio_handler.list_all_buckets()
