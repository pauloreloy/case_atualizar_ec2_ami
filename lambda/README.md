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
