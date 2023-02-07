# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year

print(f'Quem nasceu em {ano}, em {anoatual} tem {anoatual - ano} anos de idade')

if anoatual - ano < 18:
    print(f'Você deverá se alistar em {18 - (anoatual - ano)} anos')
    print(f'Seu alistamento será em {anoatual + (18 - (anoatual - ano))}')
elif anoatual - ano == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    print(f'Você deveria ter se alistado há {(anoatual - ano) - 18} anos')
    print(f'Seu alistamento foi em {anoatual - ((anoatual - ano) - 18)}')