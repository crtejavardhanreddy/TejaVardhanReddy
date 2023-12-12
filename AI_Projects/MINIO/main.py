from minio import Minio
from minio.error import S3Error
import os 


# Credintials for accessing the minio server
MINIO_ENDPOINT = "127.0.0.1:9000"
MINIO_ACCESS_KEY = "Wi0JuwXy67cnOQEvZLNB"
MINIO_SCRET_KEY = "Hkv08g9TYqrOn1on8qc5GAiM9ba7hK3IIYkxEUcr"

# Create a Minio Client to interact with server with proper Authentication keys
client = Minio(MINIO_ENDPOINT,access_key= MINIO_ACCESS_KEY, secret_key=MINIO_SCRET_KEY,secure=False)

# Name of Bucket and object
bucket_name = "bert-bucket"
object_name = "distilbert-base-cased"
directory_path = r"C:\Users\User\Desktop\MINIO\MinIO_C"
upload_file_path = r"C:\Users\User\Desktop\MINIO\app.py"
save_file_path = "test_save"

# Creating new bucket
def Create_Bucket(bucket_name):
    try:
        if client.bucket_exists(bucket_name):
            return f"Bucket '{bucket_name}' already exists."
        client.make_bucket(bucket_name)
        print(f"Bucket '{bucket_name}' created successfully")
    except S3Error as e:
        print(f"Error: {e}")

# To upload the directory
def Upload_directory(bucket_name,directory_path):
    for root, dir, files in os.walk(directory_path):
        for file in files:
            local_path = os.path.join(root,file)
            object_name = os.path.relpath(local_path,directory_path)
            object_name = object_name.replace(os.path.sep,"/") # Path seperators
            try:
                client.fput_object(bucket_name = bucket_name, object_name = object_name, file_path = local_path)
                print(f"Uploaded from {local_path} to {bucket_name}")
            except S3Error as e:
                print(f"Error while uploading directory: {e}")


# file_path is the local path of the file
# object_name is the file name of the uploading file in the minio bucket
def Upload_file(bucket_name,object_name,upload_file_path):
    try:
        client.fput_object(bucket_name = bucket_name, object_name = object_name, file_path = upload_file_path)
        print("File uploaded")
    except Exception as e:
        print(f"Error in Uploading model: {e}")

# To download a specific file from minio server
def Download_file(bucket_name,object_name, save_file_path):
    try:
        # Here object_name is the name of the object in the minio server and file_path is the path of file you want to save
        client.fget_object(bucket_name=bucket_name, object_name=object_name, file_path=save_file_path)
        print("File dowloaded")
    except Exception as e:
        print(f"Error in downloading: {e}")

# To delete a bucket
def Delete_bucket(bucket_name):
    try:
        client.remove_bucket(bucket_name)
        print(f"Bucket deleted {bucket_name}")
    except Exception as e:
        print(f"Error: {e}")

def Delete_files(bucket_name):
    # List all objects in the bucket
    try:
        objects = client.list_objects(bucket_name, recursive=True)
        for obj in objects:
            # Delete each object in the bucket
            client.remove_object(bucket_name, obj.object_name)
            print(f"Deleted: {obj.object_name}")
    except S3Error as e:
        print(f"Error: {e}")

# Lists all the available buckets
def List_all_buckets():
    try:
        buckets = client.list_buckets()
        for bucket in buckets:
            print(bucket.name)
    except S3Error as e:
        print(f"Error{e}")

# Create_Bucket(bucket_name)
# Upload_directory(bucket_name,directory_path)
# Upload_file(bucket_name,object_name,upload_file_path)
# Download_file(bucket_name,object_name,save_file_path)
# Delete_files(bucket_name)
# Delete_bucket(bucket_name)
# List_all_buckets