print("**********************************")
print('Bem vindo ao jogo de adivinhação!!')
print("**********************************")

print("Você terá 3 chances de acertar o número secreto, digite abaixo o seu palpite!")

#Número Secreto;

num_secreto = 42

#Variáveis

tentativa = 3
rodada = 1

#O progrma principal

for rodada in range(1,4):
    print(f"Tentativa {rodada} de {tentativa}")
    chute = int(input("Insira o seu número: "))
    print('Você digitou', chute)

    if chute <1 or chute > 100:
        print('Por favor, tente números de 1 à 100!!')
        continue

    acertou = num_secreto == chute
    maior = num_secreto < chute
    menor = num_secreto > chute

    if acertou:
        print('VOCÊ ACERTOU!!! Meus parabêns!!!')
        break

    else:
        if maior:
            print('Você errou, o número escolhido é maior que o número secreto!')
        elif menor:
            print('Você errou, o número escolhido é menor do que o número secreto!')

print(f'Fim do jogo. O número secreto é o: {num_secreto}')

