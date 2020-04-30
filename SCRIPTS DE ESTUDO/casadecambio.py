print('\033[1;34mSeja bem-vindo ao Carvalho Cambios\033[m')
S = float(input('\033[1;31mQuantos reais voce tem?\033[m'))
Z = str(input('\033[1;32mQual moeda voce quer comprar?\033[m')).lower()
if Z == 'dolar':
       D = float(5.22)
if Z == 'euro':
    D = float(5.67)
if Z == 'libra':
    D = float(6.52)
T = S / D

if D == 5.22:
    print('\033[1;31mVoce pode comprar {:.0f} dolares'.format(T))
if D == 5.67:
    print('Voce pode comprar {:.0f} euros'.format(T))
if D == 6.52:
    print('Voce pode comprar {:.0f} libras\033[m'.format(T))

print('\033[1;34mobrigado por comprar na carvalho cambios\033[m')
