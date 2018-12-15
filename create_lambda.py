import boto3
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')
with open ('lambda.zip', 'rb') as f:
    zipped_code = f.read()
    role = iam_client.get_role(RoleName='S3DynamoDBPolicyaa')
    lambda_client.create_function(
        FunctionName='lambda',
        Runtime='python3.6',
        Role='arn:aws:iam::117200066118:role/S3DynamoDBPolicyaa',
        Handler='lambda.handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=308,
    )
