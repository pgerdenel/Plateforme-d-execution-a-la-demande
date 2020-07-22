#!/usr/bin/env python3
# Permet de lire/recevoir un message de la queue et d'afficher le contenu du msg
import pika

# Etablie une conneixon avec le server RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create an hello queue sur laquelle notre message sera lu/reçue
# on peut déclarer la queue n'importe quel nombre de fois, elle ne sera crée qu'une seule fois
channel.queue_declare(queue='hello')

# on définit un callback qui sera appelé(par pika) à chaque nouveau message inséré dans la file
# et affichera le contenu du message
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Reçoit les message de la queue lorsqu'il y a en a
# on indique à RabbitMQ que le callback définit ci dessus doit recevoir les messages de la queue 'hello'
# on doit bien sur s'assurer que la queue existe avant de s'abonner à ce callback
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

# On boucle en attendant les données et appelons le callback quand message reçu
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# On ferme la connexion
connection.close()