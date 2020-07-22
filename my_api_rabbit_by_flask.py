#!/usr/bin/env python3
import requests, json, time
from Mtask import MtaskS
url_base = 'http://172.17.0.3:8081/rabbit/'

# POST permet de creer une queue rabbitMQ
# 'http://172.17.0.3/rabbit/'
# param queue_name et message
def create_queue(queue_name) :
    result = False
    x = requests.post(url_base, data={'nom_queue':queue_name}).json()
    print("reponse de create_queue: "+str(x))
    if x["state"] == 'OK' :
        print("requeteHTTP_create_queue ok")
        result = True
    else :
        print("requeteHTTP_create_queue pas ok")
    return result    

# POST permet d'envoyer un message dans la queue rabbitMQ
# 'http://172.17.0.3/rabbit/'
# param queue_name et message
def send_msg(queue_name, message) :   
    result = False
    x = requests.post(url_base, {'nom_queue':queue_name, 'msg':message}).json()
    print("reponse de send_msg: "+str(x))
    if x["state"] == 'OK' :
        print("requeteHTTP_send_msg ok")
        result = True
    else :
        print("requeteHTTP_send_msg pas ok")
    return result 

# GET permet de récupérer un message dans la queue rabbitMQ
# http://172.17.0.3/rabbit/queue_name?nom_queue=queue_name
# param queue_name
def get_msg(queue_name) :
    result = False
    print("URL = "+url_base+queue_name+"?nom_queue="+queue_name)
    r = requests.get(url_base+queue_name+"?nom_queue="+queue_name).json()
    print("reponse de get_msg: "+str(r))
    if r["state"] == 'OK' :
        print("requeteHTTP_get_msg ok")
        result = True
    else :
        print("requeteHTTP_get_msg pas ok")
    return result

# send chaque tache json dans la file rabbitmq
def push_task_todo(list_task) :
    for j in range(list_task):
        #o_mtask = fromJson()
        #msg = o_mtask.cmd+" "+o_mtask.phrase 
        send_msg('TODO', j)  
time.sleep(5)

create_queue('rzer')
#time.sleep(5)
send_msg('rzer', 'test')
send_msg('rzer', 'rzeezr')
send_msg('rzer', 'tejtyjtst')
send_msg('rzer', 'testyutyut')
#time.sleep(5)
#get_msg('TODO')