################################# Worker DockerFile Ubuntu ####################################################
# ip_adress: 172.17.0.4+ / gateway : 172.17.0.1 (mode bridge)
# exécutera le traitement d'une tâche d'un projet
# Plusieurs informations devront lui être communiquée
# - numéro de projet
# - numéro de la tâche
# - commande spécifié de la tâche (echo)
# - argument de la tâche(phrase)
# - dossier partagée pour ce docker
# - nom du script.sh lancé au démarrage
# - nom de l'image
# - nom du tag de version
# - alias de l'image
# - addresse ip du serveur flask 'http://172.18.10.10:51'
# - endpoint du service /send_result
# devra renvoyer la phrase affichée
#################################################################################################################

# Définie l'image qui sera utilisé et lui donne un nom 
FROM ubuntu:18.04 AS worker

# exécuter des commandes dans votre conteneur
RUN apt-get update -y
# RUN apt-get install -y ping
RUN apt-get install -y iputils-ping
# installation de pyhton
RUN apt-get install -y python3-pip python3-dev build-essential

# Créer un point de montage avec un nom spécifique 
# permet d'indiquer quel répertoire vous voulez partager avec l'hôte
# le répertoire de l'hôte qui sera partagé doit être spécifié au lancement du container 
VOLUME /dir_worker

# WORKDIR : défini le répertoire pour RUN, CMD, ENTRYPOINT, COPY, ADD
# permet de modifier le répertoire courant (équivalent de cd)
# si le dossier n'existe pas alors il sera crée automatiquement
WORKDIR /dir_worker

# COPY : copie un nouveau fichier, dossier ou données distante et de les ajouter au système de fichier de <dest>
COPY /worker_entry.sh /dir_worker/
COPY /dojob.py /dir_worker/

# ENTRYPOINT: Permet de configurer le container afin qu'il lance un script
# ENTRYPOINT ["/dir_worker/worker_entry.sh"]
ENTRYPOINT ["python3"]
CMD ["/dir_worker/dojob.py"]

##################################################################################################################