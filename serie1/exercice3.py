def findCal(type, input1):
    for indice, caractere in enumerate(input1):
        if caractere == type:
            return indice
    return -1
def doCal(indice, input):
    if input[indice] == 'x':
        resultat = int(input[indice-1]) * int(input[indice+1])
        input2 = input[:indice-1] + str(resultat) + input[indice+2:]
        return input2
    elif input[indice] == '/':
        if input[indice+1] == '0':
            print("Erreur : division par 0.")
            exit(84)
        else:
            resultat = int(input[indice-1]) / int(input[indice+1])
            input2 = input[:indice-1] + str(resultat) + input[indice+2:]
            return input2
    elif input[indice] == '+':
        resultat = int(input[indice-1]) + int(input[indice+1])
        input2 = input[:indice-1] + str(resultat) + input[indice+2:]
        return input2
    elif input[indice] == '-':
        resultat = int(input[indice-1]) - int(input[indice+1])
        input2 = input[:indice-1] + str(resultat) + input[indice+2:]
        return input2
    else:
        return input

def findOp(operateurs, input):
    for indice, caractere in enumerate(input):
        if caractere in operateurs:
            return indice
    return -1

if __name__ == "__main__":
    input1 = input("Saisissez votre calcul : ")
    operation = "x/+-"
    while True:
        indice_operateur = findOp(operation, input1)
        if indice_operateur != -1:
            indice = findCal(input1[indice_operateur], input1)
            input1 = doCal(indice, input1)
        else:
            break
        print("Résultat est :", input1)

