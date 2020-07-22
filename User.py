# Objet User représentant un utilisateur git avec les informations liées
class User():
    def __init__(self, a, b, c):
        self.name = a 		# nom de l'utilisateur
        self.git_user = b	# nom de l'utilisateur
        self.git_repo = c 	# nom du repo

# Objet User représentant un utilisateur github avec ses informations liées
class User_Github():
    def __init__(self, a, b, c):
        self.login = a 		# login de l'utilisateur
        self.password = b 	# password de l'utilisateur
        self.token = c 		# token d'accès github

######## TEST DE LA CLASSE USER_GITHUB
# user = User_Github("*****", "******(-", "cc7bf94ec0f7aaeab8521a66bd839e423a8093c3")
