# function.py

Função lambda para atualizar a AMI das instâncias.

Necessário criação das roles:

```
Role: EC2_ROLE_S3READ

Policy: arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
Policy: arn:aws:iam::aws:policy/AmazonEC2FullAccess
```

```
Role: LAMBDA_EC2_SSM_ACCESS

Policy: arn:aws:iam::aws:policy/IAMFullAccess
Policy: arn:aws:iam::aws:policy/AmazonEC2FullAccess
Policy: arn:aws:iam::aws:policy/AmazonSSMFullAccess
```

## Ajustes

Ajustar o nome do bucket no function.py:

```
ajustar bucket-xxx:

aws s3 cp s3://bucket-xxx/app/app.bin /app/app.bin
aws s3 cp s3://bucket-xxx/app/config1.cfg /app/config1.cfg
aws s3 cp s3://bucket-xxx/app/config2.cfg /app/config2.cfg
aws s3 cp s3://bucket-xxx/app/config3.cfg /app/config3.cfg
```
