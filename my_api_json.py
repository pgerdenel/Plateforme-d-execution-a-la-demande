import json

### Parse et affiche un JSON Array depuis un fichier
# @param string file_name  	path et nom de fichier.json
# @return NULL
def parse_json_array_from_file(file_name) :
	input_file = open (file_name)
	json_array = json.load(input_file)
	store_list = []

	for item in json_array:
		print(str(item))
	    # store_details = {"name":None, "city":None}
	    # store_details['name'] = item['name']
	    # store_details['city'] = item['city']
	    # store_list.append(store_details)    

### Creer un fichier.json et stocke le contenu du jsonobject json_list_task
# @param string file_name  		path et nom de fichier.json
# @param JSON json_list_task  	json_list_task.json
# @return BOOLEAN				TRUE si fichier crée, FALSE sinon
def store_json_array_in_file(file_name, json_list_task) :
	try:
		file = open(file_name, "w")
		file.write(json_list_task)
		file.close()
		print("fichier "+file_name+" created")
		return True
	except IOError:
		print("impossible de créer le fichier json_list_task")
		return False

### Permet d'afficher un JSON Object de tache (renvoyé par create)
# @param JSON json_list_task  	json_list_task.json
# @return NULL
def display_list_task(json_list_task) :
	l = json.loads(json_list_task)
	i =0;
	for task in l :
		for key, value in task.items() :
			i+=1
			if i == 6:
				for stask in value :
					print(stask)
			else :	
				print(key + " : " + str(value))
		i =0
		print("\n")	

### Creer un fichier comportant un json_array
# @param string file_name  		path et nom de fichier.json
# @param JSON json_list_task  	json_list_task.json
# @return NULL
# def create_json_array_in_file(file_name, json_list_task) :
# 	with open(file_name, 'wb') as outfile:
# 		json.dump(list, outfile)	