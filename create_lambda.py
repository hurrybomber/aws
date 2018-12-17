import boto3
Arn=input()
lambda_client = boto3.client('lambda')
iam_client = boto3.client('iam')
with open ('lambda.zip', 'rb') as f:
    zipped_code = f.read()
    role = iam_client.get_role(RoleName='DynamoB')
    lambda_client.create_function(
        FunctionName='lambda',
        Runtime='python3.6',
        Role=Arn,
        Handler='lambda.handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=308,
    )
