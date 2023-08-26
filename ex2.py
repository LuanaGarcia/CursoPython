#importar pacote SO
import os
#limpar tela
os.system('cls')
print('------------------------------------------------')
nome = input('Digite o seu nome: ')
print('Você digitou seu nome: ' + nome)
idade = input('Digite a sua idade: ')
print(f'Sua idade é {idade}')
print('O '+ nome + ' tem a idade de ' + idade)
print(f'O {nome} tem idade de {idade} anos')
dias = 365*idade
print(f'O {nome} viveu {dias} dias')


