#importar pacote SO
import os
#limpar tela
os.system('cls')
print('------------------------------------------------')
nr = int(input('Diite um valor maior que 0: '))
nr += 1
for numero in range(1,nr):
    print(f'numero: {numero}')
