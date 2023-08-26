#importar pacote SO
import os
#limpar tela
os.system('cls')
print('------------------------------------------------')
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
if (idade>= 18):
    print('Pode entrar na festa dos enxutos')
    print(f'Parabéns {nome}')
else:
    print('Pode ir para a festa da Xuxa')
    
print('------------------------------------------------')