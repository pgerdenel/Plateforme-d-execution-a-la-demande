# création d'un serveur flask en écoute sur localhost:5000
from flask import Flask, render_template, request, send_from_directory, json, logging, Response
from flask_cors import CORS, cross_origin

import zmapp.svc.api_file

app = Flask(__name__)
# On importe l'ensemble des variables défini dans le fichier config.py3
# To get one variable, tape app.config['MY_VARIABLE']
# app.config.from_object('config') 
# app.config['CORS_HEADERS'] = 'Content-Type'
# cors = CORS(app, resources={r"/rabbit/": {"origins": "*"}})
# cors = CORS(app, resources={r'/*': {"origins": '*'}})
# app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)
# cors = CORS(app)
################# ALL ROUTES #################################################################

# ROUTE racine qui renvoie l'ensemble des services exposés et l'interface web pour les utiliser
@app.route('/')
def index():
    return render_template('index.html')

# ROUTE /rabbit/ [POST] @param nom_queue
# Créer la queue     
@app.route('/rabbit/',methods = ['POST'])
def rabbit():
    print("create called")
    result = request.form
    n = result['nom_queue']
    return json.dumps(zmapp.svc.api_file.create_queue("172.17.0.2", n))

# ROUTE /rabbit/<variable> [POST] @param nom_queue @param2 message
# on définit la route rabbit pour envoyer le message@param à la queue@param
@app.route('/rabbit/<var>', methods=['POST'])
def send_msg(var):
    print("send called")
    #result = request.form
    #n = result['nom_queue']
    #m = result['msg']
    #return zmapp.svc.api_file.send_queue("172.17.0.2", n, m)

# ROUTE /rabbit/<variable> [GET] @param nom_queue
# on définit la route rabbit pour recevoir les message de la queue@param
@app.route('/rabbit/<var>', methods=['GET'])
def receive_msg(var):
    print("receive called")
    n = request.args.get('nom_queue')
    #print("queue_name GET= "+n);
    #print("message récupéré= "+str(zmapp.svc.api_file.receive_queue("172.17.0.2", n)))
    return zmapp.svc.api_file.receive_queue("172.17.0.2", n)

# on définit une route pour les fichier javascripts
@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)  

##############################################################################################

if __name__ == "__main__":
    app.run()