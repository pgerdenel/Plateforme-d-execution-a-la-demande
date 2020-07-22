import os, sys, subprocess, git, time, string
from os import path
from my_api_io import *
from git import *
#sys.path.append("..")

### permet de vérifier si un dépot git du même nom existe
# @param int local_git_folder  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @return BOOLEAN				True si dossier existe
def check_if_local_git_repo_exist(local_git_folder, nom_repo) :
	#print("repo= "+local_git_folder+nom_repo)
	#print("repo exist ?"+str(os.path.exists(local_git_folder+nom_repo)))
	return os.path.exists(local_git_folder+nom_repo)

### Creer un dossier et son repository localement puis apelle git init
# @param int local_git_folder  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @return STRING				nom du repo
def create_repo(local_git_folder, nom_new_repo) :
	nom_new_repo = nom_new_repo
	# si le dossier du repo n'existe pas on le crée
	if(check_if_local_git_repo_exist(local_git_folder, nom_new_repo) == False) :
		os.system("git init "+local_git_folder+nom_new_repo)
		return nom_new_repo

### Clone localement le contenu d'un dépôt github dans notre dossier de repos
# @param int local_git_folder  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @return STRING				nom du repo cloné
def clone_repo(repo_url, local_git_folder, nom_depot_a_cloner) :
	os.system('git clone '+repo_url+' '+local_git_folder+nom_depot_a_cloner)
	return nom_depot_a_cloner

### Ajouter et commit un fichier au projet github précédemment créé
# @param int local_repo_path  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @param string file 			nom du fichier @TODO
# @param string msg_commit 		message qui sera ajouté lors du commit
# @return NULL					
def add_file(local_repo_path, nom_repo, file, msg_commit) :
	# init(1, file)
	if(check_if_local_git_repo_exist(local_repo_path, nom_repo)) :
		os.chdir(local_repo_path+nom_repo)
		os.system("git add "+file.rsplit('/', 1)[-1])
		time.sleep(1)
		os.system("git commit -m '"+msg_commit+"'")
		#os.system("rm "+file) 
	else :
		print("le repo local n'existe pas")	

### Supprimer un fichier au projet github précédemment créé
# @param int local_repo_path  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @param string file 			nom du fichier @TODO
# @param string msg_commit 		message qui sera ajouté lors du commit
# @return NULL					
def del_file(local_repo_path, nom_repo, file, msg_commit) : 
	# si c'est un dossier à ajouter
	if is_type==True :
		# se placer dans le repos, faire un git add sur ce fichier + commit
		os.chdir(local_repo_path+nom_repo)
		os.system("git rm "+file.rsplit('/', 1)[-1])
		time.sleep(1)
		os.system("git commit -m '"+msg_commit+"'")
	else :
		print("il faut supprimer le dossier dans le repo local")

### Supprimer un repo local git
# @param string base_path_repo  path du dossier git local
# @param string nom_repo      	nom du repo tache_a_faire
# @return NULL		
# 
def del_local_repo(base_path_repo, nom_repo) :
	# se placer dans le repos, faire un git add sur ce fichier + commit
	os.chdir(base_path_repo)
	os.system("rm -rf "+nom_repo)

### Met à jour un fichier du repo (projet github) précédemment créé
# @param int local_repo_path  	path du git local
# @param string nom_repo      	nom du repo tache_a_faire
# @param string file 			nom du fichier @TODO
# @param string msg_commit 		message qui sera ajouté lors du commit
# @return NULL		
def update_file(local_repo_path, nom_repo, file, msg_commit) :
	time.sleep(1)
	# se placer dans le repos, faire un git add sur ce fichier + commit
	os.chdir(local_repo_path+nom_repo)
	os.system("git add "+file.rsplit('/', 1)[-1])
	time.sleep(1)
	os.system("git commit -m '"+msg_commit+"'")

### Afficher toute l'arborescence d'un repo local
# @param string url_repo  	path du dossier git local où sont stockés les repos
# @param string nom_repo    nom du repo à afficher
# @return NULL		
def display_local_repo(url_repo, nom_repo) :
	print("Le repo local "+nom_repo+" contient :\n")
	os.system("ls -lR "+url_repo)
