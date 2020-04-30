import math
c = float(input('Digite o valor do cateto oposto:'))
c2 = float(input('Digite o valor do cateto adjacente:'))

h = c**2 + c2**2
h1 = h**(1/2)
print('A hipotenusa vale {}'.format(h1))