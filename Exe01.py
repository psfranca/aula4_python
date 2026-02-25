'''
1. Crie um programa que leia o salário de um funcionário e mostra na tela o seu salário
anual.
'''




#ENTRADA
#CAPTURANDO O SALÁRIO E CONVERTENDO PARA FLOAT
salário_mensal = float(input('informe o seu salário mensal:'))

#PROCESSAMENTO
salário_anual = salário_mensal *12

#SAÍDA
print('Salario anual: R$', salario_anual)