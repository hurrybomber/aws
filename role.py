

import boto3
client = boto3.client('iam')
response = client.create_role(
response = client.attach_role_policy(
    RoleName='S3DynamoDBPolicya', PolicyArn='<arn:aws:iam::117200066118:policy/S3DynamoDBPolicy>')
)