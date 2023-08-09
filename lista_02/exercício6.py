q=float(input('quanto você ganha por hora?'))
h=int(input('quantas horas você trabalha por mês?'))
e=q*h
d=e*0.05
c=e*0.08
b=e*0.11
a=e-b-c-d
print(f'+ salário bruto: R${a: .2f}')
print(f'- IR(11%): R${b: .2f}')
print(f'- INSS(8%): R${c: .2f}')
print(f'- sindicato(5%): R${d: .2f}')
print(f'= salário líquido: R${e: .2f}')
