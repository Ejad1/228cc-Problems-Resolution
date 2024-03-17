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

def destructionDeListe(destructible : list, prendDestructible : list):
    for i in range(len(destructible)):
        if not (destructible[i] in prendDestructible):
            prendDestructible.append(destructible[i])

    return prendDestructible

def unChemin(imagePrime : list, endNoeud : int, fromListe1 : list, toListe1 : list, chemin : list):
    print(f"\nLe chemin en cours est : { chemin } et les images sont : { imagePrime } et sa longueur est : { len(imagePrime) }")
    if len(imagePrime) != 0:
        diversChemins = lierNoeuds(chemin, imagePrime)
        print(f"Les débuts des divers chemins : { diversChemins }")
        print(f"La longueur du tableau est : { len(diversChemins )}")
        for i in range(len(diversChemins)):
            print(f"La longueur de diversChemin est : { len(diversChemins) }")
            print(f"J'entre bien dans la boucle for pour la { i + 1 } eme fois")
            if diversChemins[i][-1] != endNoeud:
                suitesChemins = lierNoeuds(diversChemins[i], listeNoeudsSuivants(fromListe1, toListe1, diversChemins[i][-1]))
                diversCheminsPrime = suitesChemins.copy()
                print(f"La suite du chemin pour { diversChemins[i] } est : { suitesChemins }")

                copieDiversChemins = diversCheminsPrime.copy()
                print(f"Mes chemins sont : { diversCheminsPrime } et la copie est : { copieDiversChemins }")
                diversChemins.extend(diversCheminsPrime)
                print(f"diversChemins = { diversChemins }")
                print(f"Le dernier élément de { copieDiversChemins[i] } est : { copieDiversChemins[i][-1] }")
                for j in range(len(copieDiversChemins)):
                    print(f"J'entre dans cette deuxième boucle pour la { j + 1} ième fois")
                    if copieDiversChemins[j][-1] != endNoeud:
                        for j in range(len(suitesChemins)):
                            print(f"Le compteur est : { j + 1 } et la longueur totale est : { len(suitesChemins) } pour { suitesChemins }")
                            nouveau = unChemin(
                                listeNoeudsSuivants(fromListe1, toListe1, suitesChemins[j][-1]), 
                                endNoeud,
                                fromListe1,
                                toListe1,
                                copieDiversChemins[j]
                            )
                            print(f"Le nouveau chemin est : { nouveau } et diversCheminsPrime est : { diversCheminsPrime }")

                            if isinstance(nouveau[0], list):
                                if (len(nouveau) == 1):
                                    diversCheminsPrime[j] = nouveau[0].copy()
                                else:
                                    del diversCheminsPrime[j]
                                    destructionDeListe(nouveau, diversCheminsPrime)
                            else:
                                diversCheminsPrime[j] = nouveau.copy()

                            print(f"diversCheminsPrime : { diversCheminsPrime } et diversCheminsPrime[j] = { diversCheminsPrime[j] } avec j = { j }")

                            if (len(diversCheminsPrime) == 1):
                                bon = []
                                for element in diversCheminsPrime:
                                    bon.extend(element)
                                
                                diversCheminsPrime = list(bon)

                            print(f"Mon tableau à la fin du for j in avant changement est : { diversCheminsPrime }")
                           
                            print(f"diversChemins avant changement est : { diversChemins }")
                            diversChemins = destructionDeListe(diversCheminsPrime, diversChemins)
                            print(f"Mon tableau à la fin du for j in après changement est : { diversChemins } ou { diversCheminsPrime }")
                    else:
                        diversChemins[i] = diversCheminsPrime[j]
                        print(f"Le chemin est terminé et est : { diversChemins }")
            else:
                print(f"Le chemin est terminé ici et est : { diversChemins }")

        print(f"Le tableau retourné est : { diversChemins }")
        return diversChemins
    else:
        print(f"Le tableau retourné ici est : { chemin }")
        return chemin

def lierNoeuds(chemin : list, imagePrime : list):
    mesChemins = []
    if len(imagePrime) != 0:
        for i in range(len(imagePrime)):
            copieChemin = chemin.copy()
            copieChemin.append(imagePrime[i])
            mesChemins.append(copieChemin)

    return mesChemins

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


# Fonction ...
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

        print(f"Mon chemin fictif est : { fictif }")

        # Suppression de tous les chemins ne contenant pas le point d'arrivé
        vraisChemins = []
        for i in range(len(fictif)):
            if (endNode in fictif[i]):
                vraisChemins.append(fictif[i])
        fictif = vraisChemins.copy()

        print(f"Mes vrais chemins fictifs sont : { fictif }")

        # Calcul de la distance de chaque chemin
        for i in range(len(fictif)):
            for j in range(len(fictif[i]) - 1):
                distance += calculDistance(fromListe, toListe, weigthListe, fictif[i][j], fictif[i][j + 1])

            distances.append(distance)
            distance = 0

        chemins = fictif.copy()
        print(f"Mes chemins sont : { chemins }")

    # Creation of the tuples (chemins, distance)
    for i in range(len(chemins)):
        print(f"Le chemin{ i + 1 } : { chemins[i] } ; distance : { distances[i] }")
        mesTuples.append( returnTuple(chemins[i], distances[i]) )

    print(f"Les tuples retournés sont : { mesTuples }")
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

print(f"Mes tableaux sont : { g_from } + arrivé : { g_to } + weigth : { g_weigth }")

mesTuples = maFunction(g_from, g_to, g_weigth, arrival)

trueTuples = verificationOfXY(mesTuples, node_x, node_y, arrival)

print( minCostPath(trueTuples) )

os.system("pause")
