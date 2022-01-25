# 73 Faça um programa com uma tupla contendo 20 times de futebol na ordem da colocação. Depois mostre: os 5 primeiros colocados; os últimos 4 colocados; os times em ordem alfabética; e em qual posição está o timão.

# Como eu odeio futebol, fiz dos top 20 rated movies do imdb.

def Main073():
    top_movies = ('Um Sonho de Liberdade', 'O Poderoso Chefão', 'O Poderoso Chefão II', 'Batman O Cavaleiro das Trevas', '12 Homens e uma Sentença', 'A Lista de Schindler', 'O Senhor dos Anéis O Retorno do Rei', 'Pulp Fiction Tempo de Violência', 'Três Homens em Conflito', 'O Senhor dos Anéis A Sociedade do Anel', 'Clube da Luta', 'Forrest Gump O Contador de Histórias', 'A Origem', 'O Senhor dos Anéis As Duas Torres', 'O Império Contra-Ataca', 'Matrix', 'Os Bons Companheiros', 'Um Estranho no Ninho', 'Os Sete Samurais', 'Seven Os Sete Crimes Capitais')    

    print(f'\nOs 5 top filmes são: {top_movies[0:4]}.')
    print(f'\nOs 5 ultimos filmes são: {top_movies[-4:]}.')
    print(f'\nEm ordem são: {sorted(top_movies)}.')
    ord = top_movies.index('Matrix')+ 1
    print(f'\nE Matrix está em {ord} º lugar.')



Main073()

