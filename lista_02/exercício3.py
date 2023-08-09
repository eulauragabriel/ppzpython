p=float(input('digite a o peso dos peixes em kg: '))
if p>50:
    e=p-50
    m=e*4
    print(f'peso excedente em {e}kg, pague uma multa de R${m: .2f}!')
else:
    print(f'peso excedente em 0kg, pague uma multa de R$0.00!')

