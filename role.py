import boto3
import json
iam = boto3.client('iam')
assume_role_policy_document = json.dumps({
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "lambda.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
})

create_role_response = iam.create_role(
    RoleName='maaaaay-role-name',
    AssumeRolePolicyDocument=assume_role_policy_document
)
