import string, random

### Génère un string aléatoire
# @param int stringLength  	longueur de la chaine générée
# @return STRING			chaine aléatoire
def randomString(stringLength):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
