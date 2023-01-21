# case_atualizar_ec2_ami

Playbook com a finalidade de checar as instâncias EC2 e atualizar as que estiverem utilizando uma AMI ID antiga.

## Variáveis

Ajustar o nome da AMI que será utilizado:

./main.yml
```bash
ami_name: 'amzn2-ami-kernel-5.10-hvm-x86_64-gp2'
```

## Rodar playbook

```bash
ansible-playbook main.yml

```
