import random
n = random.randint(0,5)
k = int(input('Tenta advinhar um numero de 0 a 5:  '))
if k == n:
    print('Voce acertou! o numero que eu escolhi foi o {}'.format(n))
else:
    print('Voce errou.')