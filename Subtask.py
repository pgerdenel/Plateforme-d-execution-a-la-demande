# Objet Subtask représentant une sous-tâche d'une Mtask
import json

class Subtask:

	# Constructor
	def __init__(self, id_projet, id_task, id_subtask, mot) :
		self.id_projet = id_projet		# id du projet de la tache
		self.id_task = id_subtask 		# id de la tache
		self.id_subtask = id_subtask	# id de la sous tâche	
		self.mot = mot					# ressource de la sous tâche

	# Convertit l'objet en String
	def toString(self) : 
		return (
			"id_projet= "+str(self.id_projet)
			+"\n"+"id_task= " + str(self.id_task)
			+"\n"+"id_subtask= " + str(self.id_subtask)
			+"\n"+"mot= " + str(self.mot)
			)

	# Affiche l'objet
	def print(self) :
		print("Affichage de la sub tache :\n"+self.toString())

	# Convertit l'objet en JSON
	def toJson(self) :
		jo = {}
		jo['id_projet'] = self.id_projet
		jo['id_task'] = self.id_task
		jo['id_subtask'] = self.id_subtask
		jo['mot'] = self.mot
		return jo

# Convertit le JSONObjet en Mtask
def fromJson(jo) :
	return Subtask(jo['id_projet'], jo['id_task'], jo['id_subtask'], jo['mot'])	


########### TEST DE LA CLASSE ###################
# Objet standard
# t = Subtask(0, 0, 0, "salut")
#print("obj str= "+t.toString())

# Objet converted to JSON
# t1 = t.toJson()
# print("obj json= "+str(t1))
# print("obj json key= "+str(t1['id_projet']))

# JSONObject converted to Python Obj
# t2 = fromJson(t1)
# print("obj str= "+t2.toString())
