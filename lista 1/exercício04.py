s=float(input('qual é o seu salário?: '))
p= int(input('seu aumento será de quantos por cento?: '))
a= s*p/100
ns= a+s
print (f'seu aumento será de R${a: .2f}, resultando em um salário de R${ns: .2f}!')
