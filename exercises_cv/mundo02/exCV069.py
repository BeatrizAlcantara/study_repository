# 69. Faça um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: quantas pessoas tem mais de 18 anos; quantos homens foram cadastrados; quantas mulheres tem menos de 20 anos.

def Main069():
    idades = list(); maior = 0;
    sexo = list(); mulherMenor = 0;
    continua = 1
    print("Cadastro de pessoas:")

    while (continua == 1):        
        s = str(input("\nSexo: M - masculino / F - feminino: ")).upper()
        sexo.append(s)
        i = int(input("\nIdade: "))
        idades.append(i)

        if (i > 18):
            maior = maior + 1
        if (s == 'F' and i < 20):
            mulherMenor = mulherMenor + 1

        continua = int(input("\nDeseja continuar? 1 - Sim / 2 - Não: "))
    
    print(f"Há {maior} pessoas com mais de 18 anos.")
    print(f"Há {sexo.count('M')} homens.")
    print(f"Há {mulherMenor} mulheres com menos de 20 anos.")

Main069()
