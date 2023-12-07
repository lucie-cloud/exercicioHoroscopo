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
        print(f'Touro')
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print(f'Gêmeos')
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 21):
        print(f'Cancer')
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print(f'Leão')
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23):
        print(f'Virgem')
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print(f'Libra')
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        print(f'Escorpião')
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 21):
        print(f'Sagitário')
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 21):
        print(f'Capricórnio')
    elif (mes == 1 and dia >= 21) or (mes == 2 and dia <= 19):
        print(f'Aquário')
    else:
        print(f'Peixes')

# Imprimir signo
signo = signo (mes,dia)

