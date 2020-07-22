import os, sys, subprocess, git, time, string, docker,pathlib
from git import *
#sys.path.append("..")


### Exécuter un conteneur simple
# @param string image  		nom de l'image
# @param string spec  		version de l'image
# @param boolean is_in_back TRUE si lancer en background
# @return NULL
def start_simple_container(image, spec, is_in_back) :
	# connect to docker using the default socket or environnement'sconfiguration
	client = docker.from_env()
	image = (image, image+":latest")[spec]
	#client.images.pull(image)
	#client.images.list()
	client.containers.run(image+':latest', detach=is_in_back)

### Creer un *dockerfile*
# @param string container_name	nom du container
#...
# @return NULL
def create_docker_file(container_name) :
	return 0

### Récupérer la liste des conteneurs en cours exécution
# @return NULL
# 	
def list_container() :
	os.system("docker ps -a")

### Agence la création d'un dossier pour le *dockerfile*
# @param string path			path du dossier où enregistrer
# @param string container_name	nom du container
# @return NULL
def prepare_env_docker_file(path, container_name) :
	print("building container")

	# nom des fichiers qui seront créées
	file_git=".gitignore"
	file_readme="README.md"
	file_dockerf="dockerfile"

	# contenus des fichiers
	git_content = ".git"
	readme_content = "i will write some container explanations"
	dockerf_content = ""

	# on crée le dossier du container
	current_path = create_folder(container_name)
	
	# on crée les fichiers et on insère leur contenu
	create_file(current_path, file_git, git_content, 1)
	create_file(current_path, file_readme, readme_content, 1)
	create_file(current_path, file_dockerf, dockerf_content, 1)

### Build un dockerfile
#
#
def build_dockerfile(name) :
	#os.system("docker build "+path+" -t "+name)
	if name == "worker" :
		os.system("docker build "+str(pathlib.Path(__file__).parent.absolute())+"/docker_file/ubuntu/ -t worker")
	elif name == "flask_srv" :	
		os.system("docker build "+str(pathlib.Path(__file__).parent.absolute())+"/docker_file/flask/ -t flask_srv")
	elif name == "rabbitmq_srv" :
		os.system("docker build "+str(pathlib.Path(__file__).parent.absolute())+"/docker_file/rabbitmq/ -t rabbitmq_srv")
	else :
		print("nom de container invalide")	

### Clean docker container
def clean_container(name) :
	if name == "worker" :
		os.system("docker rm -f worker")
	elif name == "flask_srv" :	
		print("suppression de docker flask_srv")
		os.system("docker rm -f flask_srv")
	elif name == "rabbitmq_srv" :
		os.system("docker rm -f rabbitmq_srv")
	elif name == "all" :
		os.system("docker rm -f worker && docker rm -f flask_srv && docker rm -f rabbitmq_srv")
	else :
		print("nom de container invalide")	

### start docker container
def start_container(name) :
	client = docker.from_env()
	clean_container(name)
	os.system("docker run -d --name "+name+" "+name)

### start docker container Worker only
def start_worker(id_projet, id_task, cmd, phrase) :
	client = docker.from_env()
	clean_container(name)
	os.system("docker run -d --name worker worker")


############## TEST ####################
# build_container("test")
# start_simple_container("ubuntu", True)
# list_container()

#build_dockerfile("worker")
#build_dockerfile("flask_srv")
#build_dockerfile("rabbitmq_srv"