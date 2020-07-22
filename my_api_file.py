### creer un dossier dans le current répertoire
# @param string path  		path du dossier où enregistrer
# @param string name  		nom du fichier
# @return NULL
def create_folder(path, name) :
	path = os.path.dirname(os.path.realpath(__file__))+"/"+name # on récupère le dossier courant
	try:
		if os.path.exists(path) == False :
			print("le dossier n'existe pas")
			os.mkdir(path)	
	except OSError:
	    print ("Creation of the directory %s failed" % path)
	else:
		return str(path)+"/"
		print ("Successfully created the directory %s " % path)

### creer un fichier au path spécifié
# @param string path  		path du dossier où enregistrer
# @param string name  		nom du fichier
# @param string content  	contenu du fichier
# @param boolean reset  	TRUE si on écrase
# @return NULL
def create_file(path, name, content, reset) :
	file=path+name
	if os.path.isfile(file) == True :
		if os.path.getsize(file) != 0 and reset == 0 :
			f = open(file, "a")
			f.write("\n"+content)
			f.close()	
		else :
			f = open(file, "w+")
			f.write(content)	
			f.close()	
	else :
		f = open(file, "w+")
		f.write(content)	
		f.close()
	print("File "+file+" created|edited")		