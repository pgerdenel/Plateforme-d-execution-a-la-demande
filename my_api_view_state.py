import sys, json, os
sys.path.append("..")
from my_api_git import *
from my_api_github import *
from User import *

repo_tache_suivi = "tache_suivi" 	 # nom du repo tache_suivi
repo_tache_termine = "tache_termine" # nom du repo tache_termine
user_github = User_Github("*****", "*****(-", "cc7bf94ec0f7aaeab8521a66bd839e423a8093c3") # user github

# display_remote_repo(user_github, repo_tache_suivi)
# print(get_file_name_from_remote_repo(user_github, repo_tache_suivi, "json"))
# get_file_content_from_remote_repo(user_github, repo_tache_suivi, "json", "/home/test/env/projet/com/")

def display_task_suivi(user_github, nom_remote_repo, str_part, path_tmp) :
    f_name = get_file_content_from_remote_repo(user_github, nom_remote_repo, str_part, path_tmp)
    print("file_name = "+f_name)
    os.system("cat "+f_name)

def display_task_termine(user_github, nom_remote_repo, str_part, path_tmp) :
    f_name = get_file_content_from_remote_repo(user_github, nom_remote_repo, str_part, path_tmp)
    print("file_name = "+f_name)
    os.system("cat "+f_name)

### TEST ####    
display_task_suivi(user_github, repo_tache_suivi, "json", "/home/test/env/projet/com/")
display_task_termine(user_github, repo_tache_termine, "json", "/home/test/env/projet/com/")      