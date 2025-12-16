def calcula_atingimento(v , m):
    r = v / m
    return r


for num in range(1,4):
    try:
        venda = float(input('Informe o valor da venda: '))
        meta = float(input('Informe a meta: '))
        resultado = calcula_atingimento(venda , meta)
        

    except ValueError:
        print('\nErro!!! Digite apenas números: ')
    except ZeroDivisionError:
        print('\nErro!!! A meta não pode ser zero! ')
    else:
        print(f'Resultado: {resultado}')
    finally:
        print('Operação finalizada!' )
        



