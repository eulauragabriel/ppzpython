p=float(input('insira o preço da mercadoria: '))
d=int(input('insira o percentual de desconto: '))
d1= p*d/100
pp= p-d1
print (f'R${d1: .2f} será o valor descontado e R${pp: .2f} será o preço a pagar!')
