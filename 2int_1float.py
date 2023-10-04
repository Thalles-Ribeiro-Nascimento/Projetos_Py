# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#    a. o produto do dobro do primeiro com metade do segundo .
#    b. a soma do triplo do primeiro com o terceiro.
#    c. o terceiro elevado ao cubo.

# Entrada do 1° inteiro
num_int1 = int(input('Insira um número inteiro: '))
print(f'1° número inteiro = {num_int1}')

# Entrada do 2° inteiro
num_int2 = int(input('Insira outro número inteiro: '))
print(f'2° número inteiro = {num_int2}')

# Entrada do número real (3° número)
num_real = float(input('Insira um número real: '))
print(f'Número real = {num_real}')

# a) o produto do dobro do primeiro com metade do segundo .
p = (num_int1 * 2) * (num_int2 / 2)

# b) a soma do triplo do primeiro com o terceiro.
s = (num_int1 * 3) + num_real

# c) o terceiro elevado ao cubo.
potencia = num_real ** 3

print(f'a) ({num_int1} x 2) x ({num_int2} / 2) = {p}\n'
      f'b) ({num_int1} x 3) + {num_real} = {s}\n'
      f'c) {num_real}³ = {potencia}')
