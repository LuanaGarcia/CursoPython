#importar pacote SO
import os
#limpar tela
os.system('cls')
print('------------------------------------------------')
nome = input('Digite o seu nome: ')
salario = float(input('Digite seu salário: '))
print(f'o {nome} ganha de salário {salario}')
print('O {0} ganha de salário {1}'. format(nome, salario))
#calculos dos descontos do breno
#se o salário >=5000 - desconto de 27%
# se o salario dor menor - desconto de 20%
if(salario>=5000):
    desconto = salario * 27/100
    print('O desconto do salario do {0} é de {1} ' . format(nome, desconto))
else: 
    desconto = salario * 20/100
    print('O desconto do salário do {0} é de {1} ' . format(nome, desconto))
