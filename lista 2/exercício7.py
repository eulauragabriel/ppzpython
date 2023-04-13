m=float(input('tamanho em metros quadrados da área a ser pintada:'))
if m % 54 == 0:
    lata=m/54
else:
    lata=int(m/54)+1
valor=lata*80
print(f'precisará de {lata: .0f} lata(s), resultando em um valor de R${valor: .2f}')
