################################# RabbitMQ DockerFile ###########################################################
# ip_adress: 172.17.0.2 / gateway : 172.17.0.1 (mode bridge)
# le serveur rabbitMQ devra ouvrir les ports 15672 et 5672
# accès à l'interface web http://container_ip:15672
## login from localhost (user guest, pass guest)
# création d'un utilisateur admin
## rabbitmqctl add_user admin StrongPassword  (test vm mdp)
## rabbitmqctl set_user_tags admin administrator 
#################################################################################################################

# Défininie l'image qui sera build
FROM rabbitmq:latest AS rabbitmq_srv

# exécuter des commandes dans votre conteneur
RUN apt-get update -y
# installation de pyhton
RUN apt-get install -y python3-pip python3-dev build-essential

# Créer un point de montage avec un nom spécifique 
# permet d'indiquer quel répertoire vous voulez partager avec l'hôte
# le répertoire de l'hôte qui sera partagé doit être spécifié au lancement du container 
#VOLUME /dir_rabbitmq

# WORKDIR : défini le répertoire pour RUN, CMD, ENTRYPOINT, COPY, ADD
# permet de modifier le répertoire courant (équivalent de cd)
# si le dossier n'existe pas alors il sera crée automatiquement
#WORKDIR /dir_rabbitmq

# COPY : copie un nouveau fichier, dossier ou données distante et de les ajouter au système de fichier de <dest>
#COPY rabbitmq_create_user.sh /

# installation du plugins interface web management

#RUN chmod +x /rabbitmq_create_user.sh
#CMD ["/rabbitmq_create_user.sh"]

# permet d'ouvrir les ports nécessaires à rabbitMQ
EXPOSE 15672/tcp
EXPOSE 5672/tcp

RUN rabbitmq-plugins enable rabbitmq_management
#     rabbitmqctl start_app && \
#     rabbitmqctl add_user user test1 && \
#     rabbitmqctl set_user_tags test1 administrator && \
#     rabbitmqctl set_permissions -p / test1 ".*" ".*" ".*"

#ENTRYPOINT ["/rabbitmq_create_user.sh"]

##################################################################################################################