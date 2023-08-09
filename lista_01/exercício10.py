cd= int(input('quantos cigarros são fumados por dia?: '))
a= int(input('o consumo ocorre há quantos anos?: '))
cdam= cd*a*365*10
ch= cdam/60
cpd= ch/24
print (f'o fumante perderá aproximadamente {cpd: .0f} dias de vida.')
