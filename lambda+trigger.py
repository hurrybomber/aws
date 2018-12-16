import json
import boto3

l = boto3.client('lambda')
role = {}
s3 = boto3.client('s3')


def create_function(name, zfile,lsize=512, timeout=10, update=False):
    triggername = "{0}-Trigger".format(name)
    role['Arn']=''
    with open(zfile, 'rb') as zipfile:
        if name in [f['FunctionName'] for f in l.list_functions()['Functions']]:
            if update:
                print('Updating %s lambda function code' % (name))
                return l.update_function_code(FunctionName=name, ZipFile=zipfile.red())
            else:
                print('No')
                for f in funcs:
                    if f ['FunctionName'] == name:
                        lfunc = f
                    else:
                        print('Creating')
                        lfunc = l.create_function(
                            FunctionName=name,
                            Runtime='python3.6',
                            Role=role['Arn'],
                            Hnadler='LoadPermitData.handler',
                            Description='1',
                            Timeout=timeout,
                            MemorySize=lsize,
                            Publish=True,
                            Code={'ZipFile': zipfile.read()},
                        )
                        permissionResponse = l.add_permission(
                            FunctionName='',
                            StatementID="{0}-Event".format(triggername),
                            Action='lambda:InvokeFunction',
                            Principal='s3.amazonaws.com',
                            SourceArn=''
                        )
                        print(permissionResponse)

                              response = s3.put_bucket_notification_confugaration(
                                  Bucket='',
                                  NotificationConfiguration = {'LambdaFunctionConfigurations':[
                                      {
                                          'LambdaFunctionArn':'',
                                          'Events':[
                                              's3:objectCreated:*'
                                          ]
                                      }
                                  ]})
                        lfunc['Role'] = role
                    return lfunc
            name = 'LoadPermitData'
                    lfunc = create_function(name, 'lambda.zip', update=True)
