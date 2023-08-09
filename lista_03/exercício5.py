x=int(input('digite o valor de x: '))
y=int(input('digite o valor de y: '))
while x % y != 0:
    x, y = y, x%y
print(f'o mdc é igual a {y}')
