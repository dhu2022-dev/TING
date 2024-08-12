import boto3

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

# Specify the bucket name and file name
bucket_name = 'my-database-storage'
file_name = 'example_file.json'

# Upload a file to the bucket
s3.upload_file(file_name, bucket_name, file_name)

# Download the file from the bucket
s3.download_file(bucket_name, file_name, 'downloaded_file.json')
