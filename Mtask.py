# Objet Mtask représentant une tâche d'un projet
# Objet MtaskS représentant une tâche de suivi d'un projet
import json
# from Subtask import Subtask

class Mtask:

	# Constructor
	def __init__(self, id_projet, id_task, phrase, cmd, url) :
		self.id_projet = id_projet  # id du projet de la tache
		self.id_task = id_task		# id de la tache
		self.phrase = phrase		# phrase / ressource de la tâche
		self.cmd = cmd				# commande à lancer et liées à la tâche
		self.url = url				# url du repo github contenant le dockerfile
		# self.list_sub_task = list() # list des sous tâches == tâches divisés en sous tâches
		# i = 0
		# for mot in phrase.split(' '):
		# 	t = Subtask(id_projet, id_task, i, mot)
		# 	self.list_sub_task.append(t.toJson())
		# 	i = i+1

	# Convertit l'objet en String
	def toString(self) : 
		return (
			"id_projet= "+str(self.id_projet)
			+"\n"+"id_task= " + str(self.id_task)
			+"\n"+"phrase= " + str(self.phrase)
			+"\n"+"cmd= " + str(self.cmd)
			+"\n"+"url= " + str(self.url)
			# +"\n"+"list_sub_task= " + str(self.list_sub_task)
			)

	# Affiche l'objet
	def print(self) :
		print("Affichage de la tâche :\n"+self.toString())

	# Convertit l'objet en JSON
	def toJson(self) :
		jo = {}
		jo['id_projet'] = self.id_projet
		jo['id_task'] = self.id_task
		jo['phrase'] = self.phrase
		jo['cmd'] = self.cmd
		jo['url'] = self.url
		# jo['list_sub_task'] = self.list_sub_task
		return jo

# Convertit le JSONObjet en Mtask
def fromJson(jo) :
	#return Mtask(jo['id_projet'], jo['id_task'], jo['phrase'], jo['cmd'], jo['url'], jo['list_sub_task'])	
	return Mtask(jo['id_projet'], jo['id_task'], jo['phrase'], jo['cmd'], jo['url'])

class MtaskS:

	# Constructor
	def __init__(self, id_projet, id_task, ended) :
		self.id_projet = id_projet  # id du projet de la tache
		self.id_task = id_task		# id de la tache
		self.ended = ended			# statut de la tâche (-1 = non traitée, 0= terminée, 1=en cours)

	# Convertit l'objet en String
	def toString(self) : 
		return (
			"id_projet= "+str(self.id_projet)
			+"\n"+"id_task= " + str(self.id_task)
			+"\n"+"ended= " + str(self.ended)
			)

	# Affiche l'objet
	def print(self) :
		print("Affichage de la tâche de suivie:\n"+self.toString())

	# Convertit l'objet en JSON
	def toJson(self) :
		# jo = { 'id_projet' : { 'id_task' : self.id_task, 'ended' : self.ended }}
		jo = {}
		jo['id_projet'] = self.id_projet
		jo['id_task'] = self.id_task
		jo['ended'] = self.ended
		return jo

# Convertit le JSONObjet en MtaskS
def fromJson(jo) :	
	return MtaskS(jo['id_projet'], jo['id_task'], jo['ended'])	


########### TEST DE LA CLASSE ###################
# Objet standard
# t = Mtask(0, 0, "la phrase", "echo ", "https://github.com/*****/")
# print("obj str= "+t.toString())

# Objet converted to JSON
# t1 = t.toJson()
# print("obj json= "+str(t1))
# print("obj json key= "+str(t1['id_projet']))

# JSONObject converted to Python Obj
# t2 = fromJson(t1)
# print("obj str= "+t2.toString())
