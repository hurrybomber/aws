import boto3

s3=boto3.client('s3')
s3.upload_file('s3json.json','test-34','S3.json')