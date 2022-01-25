# Faça um programa que leia o nome e o preço de vários produtos, ele deverá perguntar se o usuário vai continuar. No final, mostre: qual é o total gasto na compra; quantos produtos custam mais de R$1000; qual é o nome do produto mais barato.

def Main070():
    produtos = list(); maior = 0;
    precos = list(); total = 0;
    barato_nome = ''; barato_p = 1000000000000.0
    continua = 1
    print("Cadastro de produtos:")

    while (continua == 1):        
        prod = str(input("\nNome do produto: "))
        produtos.append(prod)
        prec = input("\nPreço: ").replace(',','.')
        prec = float(prec)
        precos.append(prec)
        total = total + prec

        if (prec > 1000):
            maior = maior + 1
        if (prec < barato_p):
            barato_p = prec
            barato_nome = prod

        continua = int(input("\nDeseja continuar? 1 - Sim / 2 - Não: "))
    
    print(f"\nTotal da compra: R$ {total:.2f} .")
    print(f"São {maior} produtos custam mais de R$ 1000.")
    print(f"O produto mais barato é: {barato_nome}.")

Main070()
