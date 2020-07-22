################################# FLASK DockerFile #############################################################
# ip_adress: 172.17.0.3 / gateway : 172.17.0.1 (mode bridge)
# on installe le serveur flask sur la base d'une image Ubuntu
# et tous ce qui lui est nécessaire
# serveur web hébergeant les web services
# Plusieurs informaitons devront lui être communiquée
# - nom du script.sh lancé au démarrage
# - addresse ip du serveur rabbitmq
# hébergera les web services
#################################################################################################################

# serveur démarré sur l'ip du container port 8081
# Définie l'image utilisé
FROM ubuntu:18.04 AS flask_srv

# exécuter des commandes dans votre conteneur
# mise à jour de la liste de paquets
RUN apt-get update -y
# RUN apt-get install -y ping
# installation de l'utilitaire ping
RUN apt-get install -y iputils-ping
# installation de pyhton et pip3
RUN apt-get install -y python3-pip python3-dev build-essential

# Créer un point de montage avec un nom spécifique 
# permet d'indiquer quel répertoire vous voulez partager avec l'hôte
# le répertoire de l'hôte qui sera partagé doit être spécifié au lancement du container 
VOLUME /dir_flask

# WORKDIR : défini le répertoire pour RUN, CMD, ENTRYPOINT, COPY, ADD
# permet de modifier le répertoire courant (équivalent de cd)
# si le dossier n'existe pas alors il sera crée automatiquement
WORKDIR /dir_flask

# COPY : copie un nouveau fichier, dossier ou données distante et de les ajouter au système de fichier de <dest>
COPY flasksrv /dir_flask/flasksrv
COPY /flask_entry.sh /dir_flask/

# installation des modules flask, flask-cors et pika
RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install pika

# ENTRYPOINT: Permet de configurer le container afin qu'il lance un script
# ENTRYPOINT ["/dir_flask/flask_entry.sh"]
ENTRYPOINT ["python3"]

# démarrer le serveur web flask
CMD ["/dir_flask/flasksrv/run.py"]

# permet de rendre accessible les ports de puis l'extérieur du container(host)
EXPOSE 8081

##################################################################################################################