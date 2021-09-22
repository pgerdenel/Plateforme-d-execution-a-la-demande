# Explications rapides

- python3 MAIN.py
- Mise en place d'une plateforme d'exécution à la demande
- Traiter les tâches stockées sur une file de message RabbitMQ
- Exécuter les tâches sur plusieurs workers Docker (Thread) 
- Gestion du producteur de tâches par un interface web et des webs services (Flask, JS)
- Gestion du consommateur de résultats de tâche par un interface web et des webs services (Flask,JS)
- Récupération des tâches et configuration sur un dépôts Github


# Explications détaillés

__1. Introduction :__

L’objectif du projet est de mettre en place une plateforme de code à la demande.
Cette infrastructure utilisera plusieurs technologies comme Linux, RabbitMQ, 
Docker et Python.
Le but est de permettre à un client d’envoyer un projet vers un exécutant qui 
aura pour but de le diviser en plusieurs tâches et de répartir ses exécutions.


__2. Technologies utilisées :__

Système d’exploitation : Linux Ubuntu 18,04
Serveur de file de message : RabbitMQ
Serveur web : Flask (ubuntu 18.04)
OS worker : (ubuntu 18.04)
Technologie de virtualisation : Docker
Gestionnaire de dépôts : Git & Github
Langage de développement : Python
Visual Code
Putty (accès ssh)


__3. Organisation de l’infrastructure :__

La machine hôte sous Ubuntu 18.04 lancera :
- le code MAIN.py (situé dans /home/test/env/projet/MAIN.py)
- le code commanditaire qui sera un thread agira en tant que client
- le code exécutant qui sera thread agira en temps qu’exécutant
- les containers Worker et Flask seront sous Ubuntu 18.04
- le container RabbitMQ sera le container officiel docker RabbitMQ

__4. Modélisation globale du programme__

![image](https://user-images.githubusercontent.com/47711469/134269774-e4b5454b-5f9e-4c85-a3a3-992ae034a8de.png)


__5. Modélisation de l'intéraction entre les 2 threads de Main.py__

![image](https://user-images.githubusercontent.com/47711469/134269890-69f59541-0f8f-4d41-9708-f1f6093e8880.png)


