salario_hora = float(input('Insira seu salário por hora: '))

horas_trabalhadas = int(input('Insira suas horas trabalhadas por dia: '))
h_mes = horas_trabalhadas * 30
salario_mes = salario_hora * h_mes

print(f'Seu salário é de: R$ {salario_mes}')
