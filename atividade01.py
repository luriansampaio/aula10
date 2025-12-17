# Atividade 01 
# VScode - github 



def calcula_a_soma(n1 , n2):
    s = n1 + n2
    print(f'O resultado é: {s}' )
    return s


for num in range(3):
    try:
        num1 = float(input('Digite um número:' ))
        num2 = float(input('Digite aqui um outro número:' ))
        soma = float(num1 + num2)
        print(f'A soma é: {soma}')

    except ValueError:
        print('\n Erro! Digite apenas números!')
    except TypeError:
        print('\n Erro! Digite apenas números!' )
    finally:
        print('Operação finalizada!')