# 1008 - Salario

# Entrada / Conversão
number, horasTrabalhadas, salarioPorHora = input().split()

number = int(number)
horasTrabalhadas = int(horasTrabalhadas)
salarioPorHora = float(salarioPorHora)

# Calculo
salario = salarioPorHora * horasTrabalhadas

print('NUMBER = %d' % number)
print('SALARY = U$ %.2f' % salario)
