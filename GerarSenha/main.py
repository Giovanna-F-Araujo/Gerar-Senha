import random
#Declarando variáveis para armazenar as opções para a senha
cMax = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cMin = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
cEsp = "!@#$%&*"

composicao = cMax + cMin + num + cEsp
digitos = 15

#Criando random 
senha = "".join(random.sample(composicao, digitos));

#Saída de dados
print('Senha: ' + senha)