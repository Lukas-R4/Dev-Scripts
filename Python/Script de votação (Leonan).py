lucas = 0
leo = 0
bruno = 0

cont = 0

while (cont <5):
    cont += 1
    voto = int(input("Em quem você vota?\n"))

    if voto == 1:
        lucas +=1
        print("Você votou em Lucas!")
    elif voto == 2:
        leo +=1
        print("Você votou em Leo!")
    elif voto == 3:
        bruno +=1
        print("Você votou em Bruno!")
    else:
        print ("Opção inválida!")
        cont -=1

else:
    print ("Votação Encerrada!\n Resultado Final:")
    print ("\nTotal de votos: {}\n".format(cont))
#Pleo = (leo * cont) / 100
#Plucas = (lucas * cont) / 100
#Pbruno = (bruno * cont) / 100
#print ("Percentual de votos: \n Léo: {}% \n Bruno: {}% \n Lucas: {}%".format (Pleo, Pbruno, Plucas))

if (lucas > leo) and (lucas > bruno):
    winner = "01 - Lucas"
    print ("O vencedor é: {}".format(winner))
elif (leo > lucas) and (leo > bruno):
    winner = "02 - Léo"
    print ("O vencedor é: {}".format(winner))
elif (bruno > leo) and (bruno > lucas):
    winner = "03 - Bruno"
    print ("O vencedor é: {}".format(winner))
else:
    if (lucas == leo):
        print("Empate entre Lucas e Léo!\n Votos:\n Lucas: {}\n Léo {}".format(lucas, leo))
    elif (lucas == bruno):
        print("Empate entre Lucas e Bruno!\n Votos:\n Lucas: {}\n Bruno {}".format(lucas, bruno))
    elif (bruno == leo):
        print("Empate entre Bruno e Léo!\n Votos:\n Bruno: {}\n Léo {}".format(bruno, leo))


