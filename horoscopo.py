# Sistema Horóscopo

# Apresentação
print('\n\t\t\t -- Horóscopo -- \n')

# Entradas
mes = int(input('Informe o mês: '))
dia = int(input('Informe o dia: '))

# Processamento
def signo(mes,dia):

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        print(f'Aries')
    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        print(f'{mes}Touro')
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print(f'{mes}Gêmeos')
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 21):
        print(f'{mes}Cancer')
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print(f'{mes}Leão')
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23):
        print(f'{mes}Virgem')
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print(f'{mes}Libra')
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        print(f'{mes}Escorpião')
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        print(f'{mes}Sagitário')
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 21):
        print(f'{mes}Capricórnio')
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        print(f'{mes}Aquário')
    else:
        print(f'{mes}Peixes')

# Imprimir signo
signo = signo (mes, dia)

