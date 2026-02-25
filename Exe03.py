'''
Desenvolva um programa para calcular e escrever a área e o perímetro de um retângulo.
Exemplo: 
Base= 5
Altura = 4
Área = 20
Perímetro = 18
'''

#ENTRADA
base = float(input('informe a base do retangulo'))
altura = float(input('informe a altura do retângulo'))

#PROCESSAMENTO
area = base*altura
perimetro = (base*2) + (altura*2)

#SAÍDA
print('Area do retangulo', area)
print('Perimetro do retangulo', perimetro)