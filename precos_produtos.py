nome = str(input('Insira seu nome, por favor: '))

#Loop
vetor = [str]*3

lista= []
for prod in range(len(vetor)):
    vetor[prod] = input(f'Insira o produto que você deseja comprar, {nome} = ')

#Invertendo o vetor para bater com a próxima execução do código
vetor.sort()

#Loop
vl = [0]*3

for preco in range(len(vetor)):
    vl[preco] = int(input(f'Insira o valor do produto ({vetor[prod]}): R$ '))
    prod = prod - 1

#Voltando o vetor ao normal
vetor.sort(reverse=True)

#Condição
primeiro_prod = vl[0] < vl[1] and vl[0] < vl[2]
segundo_prod = vl[1] < vl[0] and vl[1] < vl[2]
igual = vl[0] == vl[1] or vl[1] == vl[2] or vl[2] == vl[0]
maior = vl[0] > vl[1] or vl[1] > vl[2] or vl[2] > vl[0]

if primeiro_prod:
    print(f'O produto ideal para se comprar, {nome}, é: {vetor[0]}!!')
elif segundo_prod:
    print(f'O produto ideal para se comprar, {nome}, é: {vetor[1]}!!')
else:
    if igual:
        print(f'A escolha fica por sua conta, {nome}!!')
    else:
        print(f'O produto ideal para se comprar, {nome}, é: {vetor[2]}!! ')
