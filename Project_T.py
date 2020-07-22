# Objet Project_T
import json

class Project_T:

	# Constructor
	def __init__(self, id_projet, list_MtaskS, nb_task) :
		self.id_projet = id_projet  		# id du projet de la tache
		self.list_MtaskS = list_MtaskS		# liste des tâches suivi et de leur état
		self.nb_task = nb_task				# nombre de tâches du projet
		self.result = ""					# résultat de l'ensemble des tâches terminées

	# Convertit l'objet en String
	def toString(self) : 
		return (
			"id_projet= "+str(self.id_projet)
			+"\n"+"list_MtaskS= " + str(self.list_MtaskS)
			+"\n"+"nb_task= " + str(self.nb_task)
			+"\n"+"result= " + str(self.result)
			)

	# Affiche l'objet
	def print(self) :
		print("Affichage de la tâche :\n"+self.toString())

	# Convertit l'objet en JSON
	def toJson(self) :
		jo = {}
		jo['id_projet'] = self.id_projet
		jo['list_MtaskS'] = self.list_MtaskS
		jo['nb_task'] = self.nb_task
		jo['result'] = self.result
		return jo

# Convertit le JSONObjet en Project_T
def fromJson(jo) :
	return Project_T(jo['id_projet'], jo['list_MtaskS'], jo['nb_task'], jo['result'])
