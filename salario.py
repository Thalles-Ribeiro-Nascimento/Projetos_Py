#Salario por hora
sal_hr = int(input('Informe quanto você ganha por hora: R$ '))

print(f'Você recebe por hora R$ {sal_hr}')

#Horas trabalhadas
num_hr_trab = int(input('Informe as horas trabalhadas no mês: '))
num_hr_sem = num_hr_trab/4
sal_sem = num_hr_sem * sal_hr

print(f'Trabalhando {num_hr_trab} horas por mês equivale a {num_hr_sem} horas semanais. Você recebe por semana R$ {sal_sem}.')

#Calculo do salário bruto
sal_bruto = sal_hr * num_hr_trab

print(f'Recebendo R$ {sal_hr} por hora, você receberá um salário bruto de R$ {sal_bruto} por mês.')

#Calculo do imposto de renda
i_r = sal_bruto * 11/100

#Calculo do INSS
inss = sal_bruto * 8/100

#Calculo do sindicato
sind = sal_bruto * 5/100

#Salário líquido
sal_liq = sal_bruto - i_r - inss - sind

print(f'+ salário bruto = R$ {sal_bruto}\n'
      f'- IR (11%) = R$ {i_r}\n'
      f'- INSS (8%) = R$ {inss}\n'
      f'- Sindicato (5%) = R$ {sind}\n'
      f' Salário líquido = R$ {sal_liq}')