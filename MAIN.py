import sys, json, os, time, threading, queue,pathlib
from threading import Thread, RLock
#sys.path.append("..")
from my_api_exec import *
from my_api_network import *
from User import *
from settings import *
from my_api_json import *
from my_api_docker import *
from my_api_task import *
from my_api_git import *
from my_api_file import *
from my_api_github import *
from my_api_exec import *
from my_api_rabbit_by_flask import *

# verrou d'accès
verrou = RLock()

# variables partagées entre les threads
shared_data = 1
is_beginning = False
is_repo_ready = False
is_container_ready = False
is_tache_ready = False
is_projet_ended = False
all_task_received = False

# Variables statiques
projet_nb = 2 # nb de projet
task_nb = 2   # nb de tâche par projet
current_id_projet = 0 # suivi des id de projet

repo_tache_a_faire = "tache_a_faire" # nom du repo tache_a_faire
repo_tache_suivi = "tache_suivi" 	 # nom du repo tache_suivi
repo_tache_termine = "tache_termine" # nom du repo tache_termine
repo_config = "config"               # bom du repo config

base_url_remote_repo = "https://github.com/******/"		# url du github de l'user
base_path_repo =  '/home/env/mgit_repo/' 	# path du git local
base_path = os.getcwd()+"/" 								# path du dossier courant
user_git = User('*****', '****', repo_tache_a_faire) 		# user git et repo tache_a_faire
user_github = User_Github("****", "******(-", "cc7bf94ec0f7aaeab8521a66bd839e423a8093c3") # user github
branch = "master"


def print_boolean_follow() :
    print("is_beginning= "+str(is_beginning))
    print("is_repo_ready= "+str(is_repo_ready));
    print("is_container_ready= "+str(is_container_ready));
    print("is_tache_ready= "+str(is_tache_ready));
    print("is_projet_ended= "+str(is_projet_ended));
    print("all_task_received= "+str(all_task_received));

class t_com(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        # définition des variables globales partagées entre les threads
        global shared_data
        global is_beginning
        global is_repo_ready
        global is_container_ready
        global is_tache_ready
        global is_projet_ended
        global all_task_received

        print("\n\n#####################################################")
        print("## ThreadName started"+self.name+" ## ")
        print("#####################################################\n\n")

        is_beginning = True
        #print("recuperation de la valeur de la variable globale= "+str(shared_data))  
        #with verrou:
            #shared_data = shared_data +1
            #print("shared_data modif= "+str(shared_data)) 

        # variables globales (settings)
        print_boolean_follow()

        # on génère les 4 repos github
        create_remote_repo(user_github, repo_tache_a_faire)
        create_remote_repo(user_github, repo_tache_suivi)
        create_remote_repo(user_github, repo_tache_termine)
        create_remote_repo(user_github, repo_config)

        # on génère les 4 repos git local
        create_repo(base_path_repo, repo_tache_a_faire)
        create_repo(base_path_repo, repo_tache_suivi)
        create_repo(base_path_repo, repo_tache_termine)
        create_repo(base_path_repo, repo_config)

        ## on devrait boucler içi pour générer de nouvelle boucle de traitement

        # on génère la liste de tache + liste de suivi de tache + liste de tache terminée
        list_task = generate_task(current_id_projet, "la phrase", task_nb, base_path_repo, repo_tache_a_faire)
        json_list_task = json.dumps(list_task, sort_keys=True, indent=4, separators=(',', ': ')) 
        # on génère liste de suivi de tache + liste de tache terminée
        list_taskS = generate_task_suivi(current_id_projet, list_task)
        json_list_taskS = json.dumps(list_taskS, sort_keys=True, indent=4, separators=(',', ': '))
        # on génère liste de tache terminée
        json_ProjectT = generate_task_terminee(current_id_projet, list_taskS)

        # on push la liste de tâche à faire sur le repot git local
        push_task(json_list_task, current_id_projet, base_path, base_path_repo, repo_tache_a_faire, user_github)
        # on push la liste de tâche suivi  sur le repot git local
        push_taskS(json_list_taskS, current_id_projet, base_path, base_path_repo, repo_tache_suivi, user_github)
        # on push la liste de tâche suivi  sur le repot git local
        push_ProjectT(json_ProjectT, current_id_projet, base_path, base_path_repo, repo_tache_termine, user_github)

        # on push les 3 différents repos vers les repos github correspondant
        push_github(base_path_repo, repo_tache_a_faire, base_url_remote_repo, branch, user_github)
        push_github(base_path_repo, repo_tache_suivi, base_url_remote_repo, branch, user_github)
        push_github(base_path_repo, repo_tache_termine, base_url_remote_repo, branch, user_github)

        # on génère le dockerfile worker dans le dépôts config/worker

        # on génère le dockerfile flask dans le dépôts config/flask

        # on génère le dockerfile file dans le dépôts config/file

        # on push le repo local config vers le repo github config

        # on informe l'éxécutant que les repos sont prêts et que le traitement peut commencer
        print("\n## ThreadName "+self.name+" ## \nis_repo_ready OK \nis_beginning = True\n");
        is_repo_ready = True

        while is_container_ready == False :
            print_period("\n\n## ThreadName "+self.name+" ## \nen attente du demarrage des containers de la part de l'executant\n");

        # on push les tâches à faire dans la file de messages TODO
       push_task_todo()

        ## on informe l'exécutant que les tâches à faire ont été placées dans la file de message
        is_tache_ready = True
        # on s'abonne à la File Done

        while is_projet_ended == False :
            print_period("\n## ThreadName "+self.name+" ## \ntant que toute les taches du projet n'ont pas ete traitees\n");
            #print_boolean_follow()
            # A chaque résultat reçue :
            # on stockera le résultat de la tâche dans la list_tache_suivi
            # on affichera l'ensemble des tâches déjà effectuées par rapport à celles reçues

        # si toutes les tâches d'un projet sont reçues alors on reconstruira le résultat que l'on stockera dans la list_tache_termine
        # le résultat d'une tâche terminée sera stockée dans le dépot github tâche terminée

        # on informe l'exécutant que le résultat de toutes les tâches du projet ont été reçues
        all_task_received = True

        # on peut consulter à tout moment les tâches_suivi en affichant le repo tache_suivi
        # on peut consulter à tout moment les tâches_termine en affichant le repo tache_termine

        # on remet l'état des taches à False
        time.sleep(10)
        # on informe l'exécutant de ne pas commencer une nouvelle boucle de traitement
        is_repo_ready = False
        is_tache_ready = False
        all_task_received = False    
        is_beginning = False

class t_exec(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        # définition des variables globales partagées entre les threads
        global shared_data
        global is_beginning
        global is_repo_ready
        global is_container_ready
        global is_tache_ready
        global is_projet_ended
        global all_task_received

        print("\n\n#####################################################")
        print("## ThreadName started"+self.name+" ## ")
        print("#####################################################\n\n")
        #print("recuperation de la valeur de la variable globale= "+str(shared_data))   
        #with verrou:
            #shared_data = shared_data +1
            #print("shared_data modif= "+str(shared_data))  
        while is_beginning == True:
            while is_repo_ready != True:
                print_period("\n## ThreadName "+self.name+" ## \nen attente de l'initialisation des repots de la part du commanditaire\n\n");

            # le commanditaire a initialisé les repos

            # on clone localement le dépôts Github tâche_suivi

            # on récupère le dockerfile rabbitmq dans le dépôts Github config/file
            ## on build l'image correspondant à ce dockerfile
            build_dockerfile("rabbitmq_srv")
            ## on démarre le docker RabbitMQ
            start_container("rabbitmq_srv")

            # on récupère le dockerfile flask serveur dnas le dépôts Github config/flask
            ## on build l'image correspondant à ce dockerfile
            build_dockerfile("flask_srv")
            ## on démarre le docker
            start_container("flask_srv")

            # on récupère le dockerfile worker dans le dépôts Github config/worker
            ## on build l'image correspondant à ce dockerfile
            build_dockerfile("worker")  

            # on doit savoir quand le docker flask et rabbitmq sont démarrés
            while ping("172.17.0.2") != True or ping("172.17.0.3") != True :
                pr = str(ping("172.17.0.2"))
                pf = str(ping("172.17.0.3"))
                print_lperiod("\n## ThreadName "+self.name+" ## \nen attente du demarrage du container rabbitmq et du container flask\nrabbitmq up= "+pr+"\nflask_srv up= "+pf+"\n");

            # on crée les files de message DONE et TODO par l'url du serveur flask
            if create_queue('TODO') == True and create_queue('DONE') == True :
                print("file de message TOTO et DONE created")
            else :
                print("ERREUR files de message non created")    

            # on informe le commanditaire que les containers sont prêts
            print("\n## ThreadName "+self.name+" ## \is_container_read OK \n");
            is_container_ready = True

            while is_tache_ready != True:
                print_period("\n## ThreadName "+self.name+" ## \nen attente de taches dans la file TODO\n\n");

            # le commanditaire a placé des tâches dans la file TODO
            ## on démarre le traitement des tâches
            
            ##### Tant qu'il y a des messages dans la file todo ( == getTask != none)
            is_empty_file = False
            while : is_empty_file != False
                # on récupère une tache dans la file Todo
                ## request to Flask serveur /getTask
                msg = get_msg('TODO')
                id_projet = msg['id_projet']
                id_task = msg('id_task')
                cmd = msg['cmd']
                phrase = msg['phrase']

                # on lance un worker avec les attributs(id_projet, id_task, id_projet, cmd, phrase) de cette tâche récupéré dans le message par /getTask
                ## on démarre le docker
                start_container(id_projet, id_task, cmd, phrase)

                # on met à jour le dépôts local tache_suivi avec le resultat et l'état ended à TRUE de la tâche terminée
                ## on push cette modification sur le dépôts Github tache_suivi
            ####     

            # il n'y a plus de tâches dans la file TODO
            # on avertit le commanditaire que toutes les tâches du projet ont été traité
            is_projet_ended = True

            while all_task_received == False :
                print_period("\n## ThreadName "+self.name+" ## \nen attente de la confirmation du commanditaire\n\n");
                print_period("\n## ThreadName "+self.name)
                #print_boolean_follow()
                print("########")

            # le commanditaire a confirmé que les résultats de toutes les tâches ont été reçues
            ## on stop le container Flask
            ## on stop le container RabbitMQ    
            ## on remet l'état des containers à False
            is_projet_ended = False
            is_container_ready = False

            # on boucle sur le traitement
            # le commanditaire devra relancer le thread commanditaire pour relancer le traitement exécutant
            while is_beginning == False :
                print_period("\n## ThreadName "+self.name+" ## \nen attente du commanditaire pour une nouvelle boucle de traitement\n\n");


# Création des threads
com_t = t_com("commanditaire")
exec_t = t_exec("executant")

# q = queue.Queue()

# Lancement des threads
com_t.start()
exec_t.start()

# Attend que les threads se terminent
com_t.join()
exec_t.join()
