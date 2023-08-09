a=int(input('digite o tamanho do primeiro lado: '))
b=int(input('digite o tamanho do segundo lado: '))
c=int(input('digite o tamanho do terceiro lado: '))
if b-c<a<b+c and a-c<b<a+c and a-b<c<a+b:
    if a==b==c:
        print('é um triângulo equilátero!')
    elif a==b or a==c or b==c:
        print('é um triângulo isóceles!')
    elif a!=b and b!=c and c!=a:
        print('é um triângulo escaleno!')
else:
    print('não é um triângulo!')
