import json
import boto3
SUCCESS = "SUCCESS"
FAILED = "FAILED"
role_name = "EC2_ROLE_S3READ"
user_data = """
#!/bin/bash
mkdir /app
aws s3 cp s3://bucket-xxx/app/app.bin /app/app.bin
aws s3 cp s3://bucket-xxx/app/config1.cfg /app/config1.cfg
aws s3 cp s3://bucket-xxx/app/config2.cfg /app/config2.cfg
aws s3 cp s3://bucket-xxx/app/config3.cfg /app/config3.cfg
instance_id=`curl http://169.254.169.254/latest/meta-data/instance-id`
region=`curl http://169.254.169.254/latest/meta-data/placement/region`
role_assoc_id=`aws ec2 describe-iam-instance-profile-associations --region $region --filters "Name=instance-id,Values=$instance_id" --query 'sort_by(IamInstanceProfileAssociations , &AssociationId)[0].AssociationId' --output text`
aws ec2 disassociate-iam-instance-profile --region $region --association-id $role_assoc_id 
"""

def get_latest_ami_id(ami_name):
    ssm_client = boto3.client('ssm')
    latest_ami_id = ssm_client.get_parameter(Name="/aws/service/ami-amazon-linux-latest/" + ami_name + "")['Parameter']['Value']
    return latest_ami_id
    
def stop_older_instance(old_instance):
    ec2_client = boto3.client('ec2')
    stop = ec2_client.terminate_instances(
        InstanceIds=[
            old_instance.instance_id
        ]
    )

def deploy_ec2(old_instance, latest_ami_id):
    ec2_client = boto3.resource('ec2')
    if(old_instance.tags == None):
        instance_name_new = ""
    else:
        for tag in old_instance.tags:
            if tag['Key'] == "Name":
                instance_name = tag['Value']
    instance_type = old_instance.instance_type
    key_name = old_instance.key_name
    iam_instance_profile = role_name
    new_instance = ec2_client.create_instances(
        MinCount=1,
        MaxCount=1,
        ImageId=latest_ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        UserData=user_data,
        IamInstanceProfile={
            'Name': iam_instance_profile
        },
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': instance_name
                },
            ]
        }
        ]
    )
    stop_older_instance(old_instance)

def check_instances(latest_ami_id):
    ec2_client = boto3.resource('ec2')
    for instance in ec2_client.instances.all():
        instance_state = instance.state['Name']
        if(instance_state == "running"):
            
            if(instance.image.id == latest_ami_id):
                deploy_ec2(instance, latest_ami_id)

def lambda_handler(event, context):
    latest_ami_id = get_latest_ami_id("amzn2-ami-kernel-5.10-hvm-x86_64-gp2")
    check = check_instances(latest_ami_id)
    return(f'OK')
    
