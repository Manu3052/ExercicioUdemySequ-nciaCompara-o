from time import sleep
import re
print('Olá, seja bem vindo ao comparador de fitas de DNA.')
primeira = input('Insira aqui a primeira fita de DNA').upper()
segunda = input('Insira aqui a segunda fita de DNA').upper()
busca = re.match(primeira,segunda)
print('Calculando')
sleep(2)
if busca:
    print('Ambas as fitas de DNA são idênticas')
    print(busca.group())
else:
    print('As fitas de DNA são diferentes')

