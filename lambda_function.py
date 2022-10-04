import boto3
import json
from collections import defaultdict

region = 'us-east-1'

ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    
    client = boto3.client('ec2')

    running_instances = client.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [ #Change values in here to match your conditions and naming convention
                    '*test*', 
                    'test*', 
                    '*test',
                    'Test*',
                    '*Test',
                    '*Test*',
                    'TEST*',
                    '*TEST',
                    '*TEST*'
                    ],
            }
            ]
        )
    
    instance_ids = []    
    
    for reservation in running_instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])
    
    for id in instance_ids:
        ec2.stop_instances(InstanceIds=[id])
