print('---------------------------------------------------------------------------------------------------------------')
print('Bem-vindo ao conversor de moedas!!')
print('---------------------------------------------------------------------------------------------------------------')

#Variável input
dinheiro = int(input('Digite o valor que você possui em reais e nós converteremos em dolar e em euro: R$ '))
cota_dolar = float(input('Digite a cotação do dólar atual: $ '))
cota_euro = float(input('Digite a cotação do euro atual: $ '))

#Conversão
dolar = dinheiro*cota_dolar

euro = dinheiro*cota_euro

#Cotações
print(f'R$ {dinheiro} em dólar ficam $ {dolar} \n'
      f'R$ {dinheiro} em euro ficam $ {euro}')
