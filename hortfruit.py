def Desconto(fruta):
    desconto = fruta * (10/100)
    valorfinal = fruta - desconto
    return valorfinal

kg_morango = int(input('Insira quantos kg de morango você irá levar: '))
kg_maca = int(input('Insira quantos kg de maçã você irá levar: '))
morango1 = 2.50 * kg_morango
morango2 = 2.20 * kg_morango
maca1 = 1.80 * kg_maca
maca2 = 1.50 * kg_maca

if kg_morango <= 5:
    print(f'Você irá pagar R$ {morango1:.2f} no morango')

elif 5 < kg_morango <= 8:
    print(f'Você irá pagar R$ {morango2:.2f} no morango')

elif kg_morango > 8 or morango2 > 25:
    print(f'Você recebeu um desconto de 10% sobre o valor do morango e irá pagar R$ {Desconto(morango2):.2f}')


if kg_maca <= 5:
    print(f'Você irá pagar R$ {maca1:.2f} na maçã')

elif 5 < kg_maca <= 8:
    print(f'Você irá pagar R$ {maca2:.2f} na maçã')

elif kg_maca > 8 or maca2 > 25:
    print(f'Você recebeu um desconto de 10% sobre o valor da maçã e irá pagar R$ {Desconto(maca2):.2f}')

