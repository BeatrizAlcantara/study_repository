# 76 Faça um programa que tenha uma tupla única com nomes de produtos e seus preços na sequência. No final, mostre uma listagem de preços, organizando os dados de forma tabular.

def Main076():
    t = ('Batom', 10, 'Brinco', 25, 'Pente', 20, 'Anel', 15)
    
    print('---TABELA DE PREÇOS---')
    print(22*'=')
    print(f'|  Produto  | Preço  |')
    for i in range(0,len(t),2):
        print(f'| {t[i]:10}| R$ {t[i+1]:3} |')
    print(22*'=')

Main076()


