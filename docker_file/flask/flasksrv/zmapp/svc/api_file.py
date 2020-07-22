#!/usr/bin/env python3
# Permet de creer une queue et d'envoyer un message dans la queue
import pika, json

def create_rabbitmq_connection(host):

    # Etablie une conneixon avec le server RabbitMQ
    # ('localhost', 15672, '/', credentials))
    credentials = pika.PlainCredentials('guest', 'guest') 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host))
    return connection 
 
def create_queue(host, queue_name):
    print("create called")
    data = {}
    data['state'] = 'NO'
    connection = None

    try:
        # on se connecte au serveur rabbitMQ
        connection = create_rabbitmq_connection(host)
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

def send_queue(host, queue_name, msg):

    data = {}
    data['state'] = 'NO'
    connection = None

    try:
        # on se connecte au serveur rabbitMQ
        connection = create_rabbitmq_connection(host)
        channel = connection.channel()

        # Envoie un message à la queue
        # 1param(exchange): échange par default identifié par une chaine vide
        # 2param(routing_key): on indique à quelle queud on souhaite délivré le message (queue hello içi)
        # 3param(body): le corps du message 
        channel.basic_publish(exchange='', routing_key=queue_name, body=msg)
        print(" [x] Sent msg="+msg+" to queue= "+queue_name)

        # On ferme la connexion
        connection.close()

        # on met à jour l'objet JSON
        data['state'] = 'OK'

        return data

    except:
        return data 
        # On ferme la connexion
        connection.close()

def receive_queue(host, queue_name):
    print("receive queue called")
    data = {}
    data['state'] = 'NO'
    connection = None

    try:
        # on se connecte au serveur rabbitMQ
        connection = create_rabbitmq_connection(host)
        channel = connection.channel()

        # on définit un callback qui sera appelé(par pika) à chaque nouveau message inséré dans la file
        # et affichera le contenu du message
        def callback(ch, method, properties, body): 
            print(" [x] Received %r" % body)
            # on met à jour l'objet JSON
            data['state'] = 'OK'
            # on convertit les bytes du messages récupérés en string
            data['msg'] = body.decode("utf-8")
            print("data= "+json.dumps(data))
            return data

        #### On ne récupère qu'un seul message de la file ######
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)        
        if method_frame.NAME == 'Basic.GetEmpty':
            connection.close()
            # on met à jour l'objet JSON
            data['state'] = 'NO'
            data['msg'] = ''
            return data
        else:          
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            # on met à jour l'objet JSON
            data['state'] = 'OK'
            data['msg'] = body.decode("utf-8")
            print("mesg returned "+json.dumps(data));
            return data


        #### Callback ####
        # Reçoit les message de la queue lorsqu'il y a en a
        # on indique à RabbitMQ que le callback définit ci dessus doit recevoir les messages de la queue 'hello'
        # on doit bien sur s'assurer que la queue existe avant de s'abonner à ce callback
        #channel.basic_consume(queue=queue_name,
        #                    auto_ack=True,
        #                    on_message_callback=callback)

        # On boucle en attendant les données et appelons le callback quand message reçu
        #print(' [*] Waiting for messages. To exit press CTRL+C')
        #channel.start_consuming()

        # On ferme la connexion
        #connection.close() 

    except Exception as e:
        print("data exception")
        # On ferme la connexion
        connection.close() 
        return data 
        print("receive_queue error= "+e)

def delete_queue(host, queue_name):

    data = {}
    data['state'] = 'NO'

    try:
        # on se connecte au serveur rabbitMQ
        connection = create_rabbitmq_connection("host")
        channel = connection.channel()

        # Create an hello queue sur laquelle notre message sera délivré
        # on peut déclarer la queue n'importe quel nombre de fois, elle ne sera crée qu'une seule fois
        channel.queue_delete(queue=queue_name)

        # On ferme la connexion
        connection.close()

        # on met à jour l'objet JSON
        data['state'] = 'OK'

        return data

    except:
        return data   

