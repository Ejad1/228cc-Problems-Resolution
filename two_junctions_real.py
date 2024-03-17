import os

listes_chemins = []

def listeNoeudsSuivants(fromListe1 : list, toListe1 : list, a : int):
    indicesApparition = []

    for i in range(len(fromListe1)):
        if fromListe1[i] == a:
            indicesApparition.append(i)
    noeudSuivant = []
    for i in range(len(indicesApparition)):
        noeudSuivant.append( toListe1[indicesApparition[i]] )

    return noeudSuivant

def lierNoeuds(chemin : list, imagePrime : list):
    mesChemins = []
    if len(imagePrime) != 0:
        for i in range(len(imagePrime)):
            copieChemin = chemin.copy()
            copieChemin.append(imagePrime[i])
            mesChemins.append(copieChemin)

    return mesChemins

def destructionDeListe(destructible : list, prendDestructible : list):
    for i in range(len(destructible)):
        if not (destructible[i] in prendDestructible):
            prendDestructible.append(destructible[i])

    return prendDestructible

def unChemin(imagePrime : list, endNoeud : int, fromListe1 : list, toListe1 : list, chemin : list):
    if len(imagePrime) != 0:
        diversChemins = lierNoeuds(chemin, imagePrime)
        for i in range(len(diversChemins)):
            if diversChemins[i][-1] != endNoeud:
                suitesChemins = lierNoeuds(diversChemins[i], listeNoeudsSuivants(fromListe1, toListe1, diversChemins[i][-1]))
                diversCheminsPrime = suitesChemins.copy()
                copieDiversChemins = diversCheminsPrime.copy()
                diversChemins.extend(diversCheminsPrime)
                for j in range(len(copieDiversChemins)):
                    if copieDiversChemins[j][-1] != endNoeud:
                        for j in range(len(suitesChemins)):
                            nouveau = unChemin(
                                listeNoeudsSuivants(fromListe1, toListe1, suitesChemins[j][-1]), 
                                endNoeud,
                                fromListe1,
                                toListe1,
                                copieDiversChemins[j]
                            )

                            if isinstance(nouveau[0], list):
                                if (len(nouveau) == 1):
                                    diversCheminsPrime[j] = nouveau[0].copy()
                                else:
                                    del diversCheminsPrime[j]
                                    destructionDeListe(nouveau, diversCheminsPrime)
                            else:
                                diversCheminsPrime[j] = nouveau.copy()

                            if (len(diversCheminsPrime) == 1):
                                bon = []
                                for element in diversCheminsPrime:
                                    bon.extend(element)
                                
                                diversCheminsPrime = list(bon)
                            diversChemins = destructionDeListe(diversCheminsPrime, diversChemins)
                    else:
                        diversChemins[i] = diversCheminsPrime[j]

        return diversChemins
    else:
        return chemin


def calculDistance(fromListe : list, toListe : list, longListe : list, a : int, b : int):
    maDistance = 0
    indicesApparition = []

    for i in range(len(fromListe)):
        if (fromListe[i] == a):
            indicesApparition.append(i)

    if (len(indicesApparition) == 1):
        maDistance = longListe[indicesApparition[0]]
    else:
        for i in range(len(indicesApparition)):
            if ( toListe[indicesApparition[i]] == b ):
                maDistance = longListe[indicesApparition[i]]

    return maDistance

def returnTuple(a : list, b : int):
    return (a, b)

def maFunction(fromListe : list, toListe : list, weigthListe : list, endNode : int):
    mesTuples = []
    distances = []
    chemins = []

    indiceArray = []

    for i in range(len(fromListe)):
        if fromListe[i] == 1:
            indiceArray.append(i)


    for i in range(len(indiceArray)):
        fictif = [1]
        distance = 0

        images = listeNoeudsSuivants(fromListe, toListe, 1)

        fictif = unChemin(images, endNode, fromListe, toListe, fictif)

        # Suppression de tous les chemins ne contenant pas le point d'arrivé
        vraisChemins = []
        for i in range(len(fictif)):
            if (endNode in fictif[i]):
                vraisChemins.append(fictif[i])
        fictif = vraisChemins.copy()

        # Calcul de la distance de chaque chemin
        for i in range(len(fictif)):
            for j in range(len(fictif[i]) - 1):
                distance += calculDistance(fromListe, toListe, weigthListe, fictif[i][j], fictif[i][j + 1])

            distances.append(distance)
            distance = 0

        chemins = fictif.copy()

    # Creation of the tuples (chemins, distance)
    for i in range(len(chemins)):
        mesTuples.append( returnTuple(chemins[i], distances[i]) )

    return mesTuples


def verificationOfXY(tuples : list, x : int, y : int, fin : int):
    mesVraisTuples = []
    for i in range(len(tuples)):
        if (x in tuples[i][0] and y in tuples[i][0] and fin in tuples[i][0] ):
            mesVraisTuples.append(tuples[i])

    return mesVraisTuples


def minCostPath(tuples : list):
    listeDistances = []
    for i in range(len(tuples)):
        listeDistances.append(tuples[i][1])

    return min(listeDistances)
            

# Demandes des infos à l'utilisateur
g_nodes = int(input("Entrer le nombre de noeuds : "))

g_from = []
g_to = []
g_weigth = []

infos = ""
i = 0
while infos != '0':
    i += 1
    array = []
    infos = input(f"Entrer les infos { i } (entrer 0 pour terminer): ")

    if infos != '0':
        array.extend(infos.split())
        g_from.append(int(array[0]))
        g_to.append(int(array[1]))
        g_weigth.append(int(array[2]))

arrival = g_nodes

node_x = int(input("Entrer le noeud X : "))
node_y = int(input("Entrer le noeud Y : "))

mesTuples = maFunction(g_from, g_to, g_weigth, arrival)

trueTuples = verificationOfXY(mesTuples, node_x, node_y, arrival)

print( minCostPath(trueTuples) )

os.system("pause")
