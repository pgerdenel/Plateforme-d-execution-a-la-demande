import sys, json, os
sys.path.append("..")
from my_api_github import *
from my_api_git import *
from User import *

user_github = User_Github("*****", "******(-", "cc7bf94ec0f7aaeab8521a66bd839e423a8093c3") # user github
base_url_remote_repo = "https://github.com/******/"		# url du github de l'use
base_path_repo =  '/home/env/mgit_repo/' 	# path du git local
repo_tache_a_faire = "tache_a_faire" # nom du repo tache_a_faire
repo_tache_suivi = "tache_suivi" 	 # nom du repo tache_suivi
repo_tache_termine = "tache_termine" # nom du repo tache_termin
repo_config = "config" # nom du repo config
branch = "master"


def delete_all_repo_local_and_remote(user_github, base_path_repo, repo_tache_a_faire, repo_tache_suivi, repo_tache_termine) :
    delete_github_repo(user_github, repo_tache_a_faire)
    delete_github_repo(user_github, repo_tache_suivi)
    delete_github_repo(user_github, repo_tache_termine)
    delete_github_repo(user_github, repo_config)
    del_local_repo(base_path_repo, repo_tache_a_faire)
    del_local_repo(base_path_repo, repo_tache_suivi)
    del_local_repo(base_path_repo, repo_tache_termine)
    del_local_repo(base_path_repo, repo_config)


delete_all_repo_local_and_remote(user_github, base_path_repo, repo_tache_a_faire, repo_tache_suivi, repo_tache_termine)

# update_file(base_path_repo, repo_tache_a_faire, "0_json_list_task.json", "tache_a_faire modified")
# update_github_repo(base_path_repo, repo_tache_a_faire, base_url_remote_repo, branch, user_github)