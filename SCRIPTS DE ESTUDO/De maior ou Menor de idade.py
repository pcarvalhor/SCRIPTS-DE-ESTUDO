from datetime import date
anoa = date.today().year
for c in range(1,7):
    input('Digite o ano que {} pessoa: '.format(c))
idade = anoa - c
    if idade >= 21:
        print('essa pessoa e de maior')