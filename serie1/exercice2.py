def exo2(input1):
    majuscules = input1.upper()
    print("En majuscules:", majuscules)
    minuscules = input1.lower()
    print("En minuscules:", minuscules)
    mots = len(input1.split())
    print("Nombre de mots:", mots)


if __name__ == "__main__":
    input1 = input("Saisissez une phrase : ")
    if input1.strip():
        exo2(input1)
    else:
        print("Erreur : La phrase ne peut pas être vide.")
        exit(84)
