# 83 Faça um programa onde o usuário digite uma expressão qualquer que use parênteses. O programa dirá se a expressão passada está com os parênteses abertos e fechados na ordem correta.

def Main083():
    exp = input('Digite a expressão: ')
    cont = 0
    for simb in exp:
        if simb == '(':
            cont += 1
        elif simb == ')':
            if cont > 0:
                cont -= 1
            else:
                cont += 1
                break
    
    if cont == 0:
        print('Expressão válida!')
    else:
        print('Expressão não válida!')

Main083()
