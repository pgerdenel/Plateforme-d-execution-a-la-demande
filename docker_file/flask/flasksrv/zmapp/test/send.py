#!/usr/bin/env python3
# Permet de creer une queue et d'envoyer un message dans la queue
import pika

# Etablie une conneixon avec le server RabbitMQ
# ('localhost', 15672, '/', credentials))
credentials = pika.PlainCredentials('guest', 'guest') 
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create an hello queue sur laquelle notre message sera délivré
# on peut déclarer la queue n'importe quel nombre de fois, elle ne sera crée qu'une seule fois
channel.queue_declare(queue='hello')

# Envoie un message à la queue
# 1param(exchange): échange par default identifié par une chaine vide
# 2param(routing_key): on indique à quelle queud on souhaite délivré le message (queue hello içi)
# 3param(body): le corps du message 
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")

# On ferme la connexion
connection.close()