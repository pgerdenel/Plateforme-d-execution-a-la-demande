import os,sys
from github import Github
import pybase64

### Vérifie si un repo Github existe
# @param User_github user_github  	Objet utilisateur github
# @param string nom_remote_repo     nom du repo tache_a_faire
# @return BOOLEAN					True si existant, False sinon
def check_if_remote_repo_exist(user_github, nom_remote_repo) :
	is_repo_exist = False
	# using username and password
	g = Github(user_github.login, user_github.password)
	# or using an access token
	g = Github(user_github.token)
	repos = g.get_user().get_repos()
	# on vérifie si un repo de l'utilisateur porte le nom du nom_remote_repo
	for repo in repos :
		#print("repo= "+repo)
		repo_name = (str(repo).rsplit('/', 1)[-1])[:-2]
		#print("est ce que "+repo_name+" est = a "+nom_remote_repo)
		if((str(repo).rsplit('/', 1)[-1])[:-2] == nom_remote_repo) :
			is_repo_exist = True
			#print("repo exist")	
	return is_repo_exist

### Créer un nouveau repo sur Github
# @param User_github user_github  	Objet utilisateur github
# @param string nom_remote_repo     nom du repo tache_a_faire
# @return NULL					
def create_remote_repo(user_github, nom_remote_repo) :
	if(check_if_remote_repo_exist(user_github, nom_remote_repo) == False) :
		# using username and password
		g = Github(user_github.login, user_github.password)
		# or using an access token
		g = Github(user_github.token)
		user = g.get_user()
		repo = user.create_repo(nom_remote_repo)
	#else : 
		#print("repo already exist")	

### Push local repo to remote github repo
# @param string base_path_repo  path du git local
# @param string nom_repo     	nom du repo tache_a_faire
# @param string repo_url     	url du github de l'user
# @param string branch     		branch du projet github du projet
# @return NULL			
def push_github(base_path_repo, nom_repo, repo_url, branch, github_user) :
	if check_if_remote_repo_exist(github_user, nom_repo) :
		try :
			nom_repo = nom_repo+"/"
			# configure the repository
			# git remote add nouveau_repo https://github.com/****/nouveau_repo
			# os.system("git push "+project)
			os.chdir(base_path_repo+nom_repo+".git")
			os.system("git remote set-url origin git@github.com:****/"+nom_repo+".git")
			# adding a remote repo
			os.system("git remote add origin "+repo_url+nom_repo)
			# troublehsoot
			#os.system("git remote -v")
			os.system("git push --set-upstream "+base_path_repo+nom_repo+" "+branch)
			os.system("git push --set-upstream origin master")
			# on se place dans le repo local et on push
			os.chdir(base_path_repo+nom_repo+".git")
			# os.system("push -u "+base_path_repo+nom_repo+".git")
			#os.system("git push -u "+base_path_repo+nom_repo+"/"+" "+branch)	
			os.system("git push -u origin master")
			# os.system("git push")
		except :
			print.warning("error")	
	else :
		print("le repo n'existe pas, on ne peut pas push les taches JSON")	

### update remote github repo with local repo change
# @param string base_path_repo  path du git local
# @param string nom_repo     	nom du repo tache_a_faire
# @param string repo_url     	url du github de l'user
# @param string branch     		branch du projet github du projet
# @return NULL			
def update_github_repo(base_path_repo, nom_repo, repo_url, branch, github_user) :
	if check_if_remote_repo_exist(github_user, nom_repo) :
		os.chdir(base_path_repo+nom_repo+"/.git")
		os.system("git remote set-url origin https://github.com/*****/"+nom_repo+".git")
		os.system("git push -u origin master")
	else :
		print("le repo n'existe pas, on ne peut pas push les modifications du repo")

def delete_github_repo(user_github, nom_remote_repo) :
	if(check_if_remote_repo_exist(user_github, nom_remote_repo) == True) :
		# using username and password
		g = Github(user_github.login, user_github.password)
		# or using an access token
		g = Github(user_github.token)
		# repo = g.get_repo("*****/tache_a_faire")
		repo = g.get_repo("*****/"+nom_remote_repo)
		repo.delete()
		print("repo "+nom_remote_repo+" deleted")
	else : 
		print("repo don't exist")
	
### Afficher toute l'arborescence d'un repo distant (Github)
# @param string url_repo  	url de base du compte github où sont stocker les repos
# @param string nom_repo    nom du repo a afficher
# @return NULL		
def display_remote_repo(user_github, nom_remote_repo) :
	if check_if_remote_repo_exist(user_github, nom_remote_repo) :
		print("Le repo local "+nom_remote_repo+" contient :\n")
		# using username and password
		g = Github(user_github.login, user_github.password)
		# or using an access token
		g = Github(user_github.token)
		repo = g.get_user().get_repo(nom_remote_repo)
		contents = repo.get_contents("")
		while contents:
			file_content = contents.pop(0)
			if file_content.type == "dir":
				contents.extend(repo.get_contents(file_content.path))
			else:
				print(file_content.name)
	else :
		print("le repo distant n'existe pas")

### Renvoie le nom de fichier qui contient la partie de string passé en paramètre
# @param string url_repo  	url de base du compte github où sont stocker les repos
# @param string nom_repo    nom du repo a afficher
# @param str_part			bout de chaine que le fichier doit contenir
# @return NULL	
def get_file_name_from_remote_repo(user_github, nom_remote_repo, str_part) :
	if check_if_remote_repo_exist(user_github, nom_remote_repo) :
		name_file = ""
		# using username and password
		g = Github(user_github.login, user_github.password)
		# or using an access token
		g = Github(user_github.token)
		repo = g.get_user().get_repo(nom_remote_repo)
		contents = repo.get_contents("")
		while contents:
			file_content = contents.pop(0)
			if file_content.type == "dir":
				contents.extend(repo.get_contents(file_content.path))
			else:
				if str_part in file_content.name :
					name_file = file_content.name		
	else :
		print("le repo distant n'existe pas")

	return name_file

### Créer un fichier local du fichier récupéré sur le repo github
# @param string url_repo  	url de base du compte github où sont stocker les repos
# @param string nom_repo    nom du repo a afficher
# @param str_part			bout de chaine que le fichier doit contenir
# @param path_tmp			chemin du dossier où le fichier sera stocké temporairement
# @return STRING			nom du fichier généré	
def get_file_content_from_remote_repo(user_github, nom_remote_repo, str_part, path_tmp) :
	f_name = ""
	if check_if_remote_repo_exist(user_github, nom_remote_repo) :
		# using username and password
		g = Github(user_github.login, user_github.password)
		# or using an access token
		g = Github(user_github.token)
		repo = g.get_user().get_repo(nom_remote_repo)
		# print("file retrived = "+get_file_name_from_remote_repo(user_github, nom_remote_repo, str_part))
		f_name=get_file_name_from_remote_repo(user_github, nom_remote_repo, str_part)
		file_content = repo.get_contents(f_name)
		file_data = pybase64.b64decode(file_content.content)
		file_out = open(path_tmp+file_content.name, "wb")
		file_out.write(file_data)
		file_out.close()
	else :
		print("pas de repo de ce nom")	
	return 	path_tmp+f_name


### Vérifie si un repo Github existe (2eme manière)
# @param User_github user_github  	Objet utilisateur github
# @param string nom_remote_repo     nom du repo tache_a_faire
# @return BOOLEAN					True si existant, False sinon
# def check_if_repo_exit(user_github, nom_repo): 
# 	random_name = randomString(5)+"/"
# 	try:
# 	    git.Repo.clone_from(f'https://github.com@github.com/{user_github.git_user}/' + \
# 	         f'{user_github.git_repos}.git', f'{random_name}{user_github.name}')
# 	    os.system('rm -rf '+base_path+random_name)
# 	    return True
# 	except git.exc.GitError:
# 	    #print(f'ERROR! {user_github.name}: {user_github.git_user}/{user_github.git_repos} does not exist')
# 	    return False



