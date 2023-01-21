# case_atualizar_ec2_ami

Playbook com a finalidade de checar as instâncias EC2 e atualizar as que estiverem utilizando uma AMI ID antiga.

## Variáveis

Ajustar o nome da AMI que será utilizado:

main-playbook.yml
```python
ami_name: 'amzn2-ami-kernel-5.10-hvm-x86_64-gp2'
```

## Rodar playbook

```bash
ansible-playbook main-playbook.yml

```

## Requisitos

python version >= 3.9.2

ansible >= 2.14.1

ansible collections amazon.aws >= 5.1.0

botocore>=1.21.0

boto3>=1.18.0

Credenciais AWS configuradas pelo CLI: aws configure