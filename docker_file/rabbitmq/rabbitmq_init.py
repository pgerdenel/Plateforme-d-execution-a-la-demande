#!/usr/bin/env python3
import pika, json, os

def create_queue(host, queue_name):

    data = {}
    data['state'] = 'NO'
    connection = None

    try:
        # on se connecte au serveur rabbitMQ
        connection = create_rabbitmq_connection("host")
        channel = connection.channel()

        # Create an hello queue sur laquelle notre message sera délivré
        # on peut déclarer la queue n'importe quel nombre de fois, elle ne sera crée qu'une seule fois
        channel.queue_declare(queue=queue_name)

        # On ferme la connexion
        connection.close()

        # on met à jour l'objet JSON
        data['state'] = 'OK'

        return data

    except:
        return data
        # On ferme la connexion
        connection.close()

# on crée la file done et la file todo
create_queue('172.17.0.3', 'TODO')
create_queue('172.17.0.3', 'DONE')