a=int(input('digite o primeiro valor: '))
b=int(input('digite o segundo valor: '))
c=int(input('digite o terceiro valor: '))
if a>=b and a>=c:
    print(f'{a} é o maior valor!')
elif b>=a and b>=c:
    print(f'{b} é o maior valor!')
elif c>=a and c>=b:
    print(f'{c} é o maior valor!')
