valor_porhoratblhd= 60.20
horas_trabalhadas= int(input(" Quantas horas trabalhadas? "))
if horas_trabalhadas<=20:
    salario = valor_porhoratblhd*horas_trabalhadas
else:
    extra = valor_porhoratblhd*0.3
    salario = valor_porhoratblhd*horas_trabalhadas+extra
print(f" O salário do funcionário é {salario} de reais")
