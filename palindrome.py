import os, time
from math import floor

def palindromeChecker(mot : str, start : list, end : list, substitut : list):
    result = []
    for i in range(len(start)):
        motPrime = mot[start[i]:end[i]]

        uniqueRepet = 0
        # Parcours du mot pour voir les lettres qui se répètent une seule fois
        for j in range(len(motPrime)):
            if motPrime.count(motPrime[j]) == 1:
                uniqueRepet += 1

        # Etude de la possibilité de former un palindrome en fonction du nombre de lettre qui ne se repètent pas
        if floor(uniqueRepet / 2) <= substitut[i]:
            result.append(1)
        else:
            result.append(0)

        
    finalResult = ''
    for i in range(len(result)):
        finalResult = finalResult + str(result[i])

    return finalResult
        

# Demande des infos à l'utilisateur
continuer = 'TRUE'
while continuer == 'TRUE':
    mot = input("Entrer le mot : ")

    startIndex = []
    nbreDebut = int(input("\nEntrer le nombre d'indexes de début : "))
    for i in range(0, nbreDebut):
        index = int(input(f"Entrer l'indexe { i + 1 } de début : "))
        startIndex.append(index)

    print("\n")
    endIndex = []
    for i in range(0, nbreDebut):
        index = int(input(f"Entrer l'indexe { i + 1 } de fin : "))
        endIndex.append(index)

    print("\n")
    subs = []
    for i in range(0, nbreDebut):
        index = int(input(f"Entrer l'indexe { i + 1 } de substitution: "))
        subs.append(index)

    
    start_time = time.time()
    print( palindromeChecker(mot, startIndex, endIndex, subs) )
    end_time = time.time()

    print(f"Temps d'exécution : { end_time - start_time}")

    continuer = input("Voulez-vous continuer ? (si oui entrer TRUE) : ").upper()


os.system('pause')
