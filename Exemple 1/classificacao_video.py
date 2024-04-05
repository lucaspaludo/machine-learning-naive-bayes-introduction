'''[
    possui violência gráfica?,
    não possui violência gráfica?, 
    possui violação de direitos autorais?,
    não possui violação de direitos autorais?,
    possui conteúdo adulto?,
    não possui conteúdo adulto?
    ]
'''

video1 = [0, 1, 1, 0, 0, 1]
video2 = [1, 0, 1, 0, 1, 0]
video3 = [1, 0, 0, 1, 1, 0]
video4 = [0, 1, 0, 1, 0, 1]
video5 = [0, 1, 1, 0, 1, 0]
video6 = [1, 0, 1, 0, 0, 1]

dados = [video1, video2, video3, video4, video5, video6]
marcacoes = [-1, -1, -1, 1, -1, -1]

cobaia1 = [0, 1, 0, 1, 0, 1]
cobaia2 = [1, 0, 0, 1, 0, 1]
cobaia3 = [0, 1, 1, 0, 0, 1]

resultado = [cobaia1, cobaia2, cobaia3]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacoes)
print(modelo.predict(resultado))
