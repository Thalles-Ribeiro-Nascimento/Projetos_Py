#Faça um programa em Python que leia 3 valores de ponto flutuante e efetue o cálculo das raízes usando a equação de Bhaskara.
# Se não for possível calcular as raízes, caso haja uma divisão por 0 ou uma raiz quadrada de número negativo, apresente
# a mensagem “impossível calcular a raiz”.
print('-------------------------------------------------------------------')
print('Bem-vindo a calculadora de Baskhara!!')
print('-------------------------------------------------------------------')

print('Vamos começar, digite abaixo os valores das icógnitas: a, b e c')
#Input's
a = float(input('Insira um valor: '))
b = float(input('Insira um valor: '))
c = float(input('Insira um valor: '))

print(f'A equação ficou {a:.0f}x² + {b:.0f}x + {c:.0f} = 0')
#Variável delta
delta = b**2 - 4 * a * c

print(f'Delta = {b:.0f}² - 4 x {a:.0f} x {c:.0f}\n'
      f'Delta = {delta}')


#Raízes
x1 = (-b + delta**(1/2))/2*a
print(f'x1 = -{b:.0f} + raiz de {delta}/2x{a:.0f}')
x2 = (-b - delta**(1/2))/2*a
print(f'x2 = -{b:.0f} - raiz de {delta}/2x{a:.0f}')

#Condições
if a == 0:
    print('Impossível calcular a raiz!! O valor do a não pode ser zero.')

elif delta < 0:
    print('Impossível calcular a raiz!! O valor do delta não pode ser menor que zero.')

else:
    print(f'x1 = {x1:.2f}\n'
          f'x2 = {x2:.2f}')

#Fim
print('Obrigado por usar nosso programa. Volte sempre!!')








