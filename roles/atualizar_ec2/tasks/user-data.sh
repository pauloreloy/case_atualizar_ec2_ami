#!/bin/bash
mkdir /app
aws s3 cp s3://bucket-XXX/app/app.bin /app/app.bin
aws s3 cp s3://bucket-XXX/app/config1.cfg /app/config1.cfg
aws s3 cp s3://bucket-XXX/app/config2.cfg /app/config2.cfg
aws s3 cp s3://bucket-XXX/app/config3.cfg /app/config3.cfg
instance_id=`curl http://169.254.169.254/latest/meta-data/instance-id`
region=`curl http://169.254.169.254/latest/meta-data/placement/region`
role_assoc_id=`aws ec2 describe-iam-instance-profile-associations --region $region --filters "Name=instance-id,Values=$instance_id" --query 'sort_by(IamInstanceProfileAssociations , &AssociationId)[0].AssociationId' --output text`
aws ec2 disassociate-iam-instance-profile --region $region --association-id $role_assoc_id 
