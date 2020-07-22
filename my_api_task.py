import json, sys
#sys.path.append("..")
from my_api_json import *
from my_api_git import *
from my_api_github import *
from Mtask import Mtask
from Mtask import MtaskS
from Project_T import Project_T

### Génère des tâches au format JSON pour un projet spécifié
# @param int current_id_projet   		id du projet de la liste de tâche
# @param string tache_phrase 			la phrase qui sera modelé dans la double boucle pour génrérer une phrase par tâche
# @param string task_nb       			nombre de tâche par projet
# @param string nom_repo_tache_a_faire  nom_repo_tache_a_faire
# @param string nom_repo_tache_suivi  	nom_repo_tache_suivi
# @param string nom_repo_tache_termine  nom_repo_tache_termine
# @return JSON 							liste des tâches au format JSON
def generate_task(id_projet, tache_phrase, task_nb, base_path_repo, nom_repo_tache_a_faire) :
	list_task = list()
	# pour la tache N° j du projet N° i
	for j in range(task_nb):
		# génération d'une tâche
		mtask = Mtask(id_projet, str(j), "la tache numero "+str(j)+" dit bonjour au projet numero "+str(id_projet), "echo ", base_path_repo+nom_repo_tache_a_faire)
		t_ins = mtask.toJson()
		list_task.append(t_ins)
		#print(t_ins)
	return list_task

### Génère le tâches_suivi au format JSON pour un projet spécifié
# @param int current_id_projet  id du projet de la liste de tâche
# @param list() list_t 			liste des tâches à faire au format JSON
# @return JSON 					liste des tâches de suivi au format JSON
def generate_task_suivi(id_projet, list_t) :
	#print("type = "+str(type(list_t)))
	list_task = list_t
	length = len(list_task) 
	list_taskS = list()
	#print("on itere les taches a faire")
	for i in range(length):
		# génération d'une tâche
		mtaskS = MtaskS(id_projet, str(list_task[i]['id_task']), False)
		t_ins = mtaskS.toJson()
		list_taskS.append(t_ins) 
		#print(str(t_ins)) 	
	return list_taskS

### Génère le tâches_suivi au format JSON pour un projet spécifié
# @param int current_id_projet  id du projet de la liste de tâche
# @param list() list_t 			liste des tâches à faire au format JSON
# @return JSON 					liste des tâches terminée au format JSON
def generate_task_terminee(id_projet, list_ts) :
	list_tasks = list_ts
	length = len(list_ts) 
	projectT = Project_T(id_projet, list_tasks, length)
	#print(str(t_ins)) 
	return json.dumps(projectT.toJson(), sort_keys=True, indent=4, separators=(',', ': '))

### Déposer les tâches générés dans le dépôt local puis dans le dépôt Github tache_a_faire
# @param JSON json_list_task 	liste des tâches au format JSON
# @param int id_projet      	id du projet de la liste de tâche
# @param string base_path 		path du dossier courant
# @param string base_path_repo  url du git de l'user
# @param nom_repo       		nom repo tache_a_faire
# @param User_Github 			user github 
# @return Boolean 				0 if ok, 1 if pas ok
def push_task(json_list_task, id_projet, base_path, base_path_repo, nom_repo, github_user) :
	# on génère le fichier
	if store_json_array_in_file(base_path_repo+nom_repo+"/"+str(id_projet)+"_json_list_task.json", json_list_task) :
		# on push ce fichier dans le repo local
		add_file(base_path_repo, nom_repo, base_path+str(id_projet)+"_json_list_task.json", "Ajout de la liste de Tache pour le projet "+str(id_projet))	
	return 0

### Déposer les tâches de suivi générés dans le dépôt local puis dans le dépôt Github tache_suivie
# @param JSON json_list_task_suivi 	liste des tâches suivi au format JSON
# @param int id_projet      		id du projet de la liste de tâche
# @param string base_path 			path du dossier courant
# @param string base_path_repo  	url du git de l'user
# @param nom_repo       			nom repo_tache_suivi
# @param User_Github 				user github 
# @return Boolean 					0 if ok, 1 if pas ok
def push_taskS(json_list_task_suivi, id_projet, base_path, base_path_repo, nom_repo, github_user) :
	# on génère le fichier
	if store_json_array_in_file(base_path_repo+nom_repo+"/"+str(id_projet)+"_json_list_task_suivi.json", json_list_task_suivi) :
		# on push ce fichier dans le repo local
		add_file(base_path_repo, nom_repo, base_path+str(id_projet)+"_json_list_task_suivi.json", "Ajout de la liste de Tache pour le projet "+str(id_projet))	
	return 0	

### Déposer les tâches générés dans le dépôt local puis dans le dépôt Github tache_a_faire
# @param JSON json_ProjectT 	liste des tâches au format JSON
# @param int id_projet      	id du projet de la liste de tâche
# @param string base_path 		path du dossier courant
# @param string base_path_repo  url du git de l'user
# @param nom_repo       		nom repo_tache_termine
# @param User_Github 			user github 
# @return Boolean 				0 if ok, 1 if pas ok
def push_ProjectT(json_ProjectT, id_projet, base_path, base_path_repo, nom_repo, github_user) :
	# on génère le fichier
	if store_json_array_in_file(base_path_repo+nom_repo+"/"+str(id_projet)+"_json_list_task_termine.json", json_ProjectT) :
		# on push ce fichier dans le repo local
		add_file(base_path_repo, nom_repo, base_path+str(id_projet)+"_json_list_task_termine.json", "Ajout de la liste de Tache pour le projet "+str(id_projet))	
	return 0

# permet de sauvegarder localement le résultat d'une partie d'une tâche effectuées 
def local_save_result_part_task() :
	return 0
# permet de sauvegarder sur github le résultat d'une partie d'une tâche effectuées sur le repo 'github tache_suivi'
def remote_save_result_part_task() :
	return 0
# permet de sauvegarder les informations d'une tâche temrinées sur le repo github 'tache_termine'
def remote_update_task_ended() :
	return 0
# permet de reconstruire une tâche avec le résultat de toutes ses parties terminées
def build_task_from_part() :
	return 0
# permet de récupérer l'état de traitement d'une tâche
def get_task_state() :
	return 0
# permet de récupérer la liste des tâches terminées(et leur information)
def get_task_ended() :	
	return 0
# afficher le contenu du dépôt tache_suivi
def get_task_state() :
	return 0	


### Génère des tâches au format JSON pour un projet spécifié
# @param int curren_id_projet     		id du projet de la liste de tâche
# @param string tache_phrase 	la phrase qui sera modelé dans la double boucle pour génrérer une phrase par tâche
# @param string projet_nb       nombre de projet 
# @param string task_nb       	nombre de tâche par projet
# @param string base_path       path du dossier où l'on se trouve
# @param string base_url_repo  	message to display
# @return JSON 					liste des tâches au format JSON
# def generate_task(curren_id_projet, tache_phrase, projet_nb, task_nb, base_path, base_url_repo) :
# 	list_task = list()
# 	# pour le projet N° i
# 	for i in range(projet_nb):
# 		# pour la tache N° j du projet N° i
# 		for j in range(task_nb):
# 			# génération d'une tâche
# 			mtask = Mtask(str(i), str(j), "la tache numero "+str(j)+" dit bonjour au projet numero "+str(i), "echo ", base_url_repo)
# 			t_ins = mtask.toJson()
# 			list_task.append(t_ins)
# 			#print(t_ins)
# 	return json.dumps(list_task, sort_keys=True, indent=4, separators=(',', ': '))	