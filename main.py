#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Bruno Imperador Kneblewski
# Created Date: 08/09/2022
# Version = Python 3.9
# Description = CHECKPOINT - CODING FOR SECURITY
# License = PyCharm 2022.2.1 (Community Edition)
#----------------------------------------------------------------------------
import pyfiglet
from sklearn import tree

constantemente = "1"
regularmente = "2"
nunca = "3"
saudavel = "1"
normal = "2"
estragado = "3"

saude = [["10", "30", constantemente, constantemente, constantemente], ["5", "15", regularmente, regularmente, regularmente], ["5", "7", nunca, nunca, nunca]]
resultado = [saudavel, normal, estragado]

classificador = tree.DecisionTreeClassifier()
classificador = classificador.fit(saude, resultado)

ascii_banner = pyfiglet.figlet_format("BODY HEALTH")
print(ascii_banner)
print(f"O Body Health dirá sua saúde em 30 anos, baseada em hábitos atuais.\n")
atividade_fisica = input("Quanto do seu dia você pratica atividades físicas? (em porcentagem): ")
qualidade_sono = input("Quanto do seu dia você dorme? (em porcentagem): ")
frutas = input("Com que frequência come frutas? \n 1- Constantemente \n 2- Regularmente \n 3- Nunca: ")
refeicoes = input("Com que frequência faz 3 refeições ao dia? \n 1- Constantemente \n 2- Regularmente \n 3- Nunca: ")
sol = input("Com que frequência toma sol? \n 1- Constantemente \n 2- Regularmente \n 3- Nunca: ")
resultado_input = classificador.predict([[atividade_fisica, qualidade_sono, frutas, refeicoes, sol]])

if resultado_input == "1":
    print(f"\nVocê estará saudável daqui a 30 anos.")
elif resultado_input == "2":
    print(f"\nVocê estará normal daqui a 30 anos.")
elif resultado_input == "3":
    print(f"\nVocê estará estragado daqui a 30 anos.")
else:
    print("Ocorreu um erro.")
