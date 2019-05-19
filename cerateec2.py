import os
import boto3

AMI = os.environ['AMI']
Instance_TYPE = os.environ['INSTANCE_TYPE']
Key_NAME = os.environ['KEY_NAME']
Subnet_ID = os.environ['SUBNET_ID']
ec2 = boto3.resource('ec2')

def lambda_handler(event,context):
    instance = ec2.create_instances(
        ImageId = AMI,
        InstanceType = Instance_TYPE,
        KeyName = Key_NAME,
        SubnetID = Subnet_ID,
        MaxCount = 1,
        MinCount =1
        )
    print("New instance created:",instance[0].id)
