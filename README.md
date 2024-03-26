# Reaching points

Le problème consiste à vérifier si un robot en une position (x, y) peut atteindre le point (x_final, y_final) en se déplaçant suivant un principe donné : il ne peut se déplacer qu'en (x + y, y) ou qu'en (x, x + y)

Ma solution est assez simple : je calcule les deux possibilités de déplacement précédements cités et je les compare au point d'arriver.
Si après avoir fait les déplacements, les coordonnées obtenues sont tous supérieurs au point d'arrivé alors je m'arrête sinon je continue

Vous trouverez dans le fichier 'CASES.pdf' quelques exemples de points de départs et d'arrivés et ce que le programme doit retourner

Plus d'info dans le fichier 'EXPLANATION.pdf'

### <h3 style='color: blue; text-align: center'> EJAD
