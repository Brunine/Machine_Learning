#!/usr/bin/env python3
from sklearn import tree

lisa = 1
irregular = 0
maça = 1
laranja = 0


pomar = [[150, lisa], [130, lisa], [180, irregular], [160, irregular]]
resultado = [maça, maça, laranja, laranja]
classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(pomar, resultado)
peso = input("Por favor, entre com o peso da fruta: ")
superficie = input("Por favor, informe a superficie, (0) irregular, (1) lisa : ")
resultodousuario = classificador.predict([[peso, superficie]])


if resultodousuario == 1:
    print("É uma Maça.")
else:
    print("É uma Laranja.")