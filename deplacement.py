import os, time

# Fonctions d'avancer par rapport à l'abscicce ou à l'ordonnée
def avanceX(x, y):
    return (x + y, y)

def avanceY(x, y):
    return (x, x + y)


def canReach(a, b, c, d):
    endTuple = (c, d)
    # If the start point is above the end point we can't make the operation
    if (a > c or b > d):
        return 'No'

    # If the a and b values are 'pairs' and the c and d are odd (impair) then the result is No
    if (((a % 2 == 0 and b % 2 == 0) and (c % 2 != 0 and d % 2 != 0)) or ((c % 2 == 0 and d % 2 == 0) and (a % 2 != 0 and b % 2 != 0))):
        return 'No'
    
    # Array of the values
    array = []

    firstX = avanceX(a, b)
    firstY = avanceY(a, b)

    array.append([firstX, firstY])

    i = 0
    enter = 'TRUE'
    while (enter == 'TRUE'):
        long = len(array[i])

        newArray = []
        for j in range(long):
            myTuple = array[i][j]
            newA = myTuple[0]
            newB = myTuple[1]

            firstX = avanceX(newA, newB)
            firstY = avanceY(newA, newB)

            newArray.extend([firstX, firstY])

        array.append(newArray)

        good = 0
        lengthJustificator = 0
        for k in array[i]:           
            if (k == endTuple):
                return 'Yes'
            else:
                if (k[0] > endTuple[0] or k[1] > endTuple[1]):
                    good += 1
                    lengthJustificator = len(array[i]); 
                else:
                    good += 0

        if (good != 0):
            if (good == lengthJustificator):
                enter = 'FALSE'
                return 'No'
        

        i += 1


continuer = 0
while (continuer == 0):
    # Demande des infos à l'utilisateur
    x1 = int(input('Entrer x1 : '))
    y1 = int(input('Entrer y1 : '))
    x2 = int(input('Entrer x2 : '))
    y2 = int(input('Entrer y2 : '))

    start_time = time.time()
    print(canReach(x1, y1, x2, y2))
    end_time = time.time()

    print(f"Temps d'exécution : { end_time - start_time}")

    continuer = int(input("\nVoulez-vous continuer : "))


os.system('pause')
