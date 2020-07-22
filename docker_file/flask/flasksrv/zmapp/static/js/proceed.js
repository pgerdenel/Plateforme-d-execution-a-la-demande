// const url_base = "http://localhost:5000/rabbit/";
const url_base = "http://192.168.3.101:2524/rabbit/";

const requeteHTTP_create = new XMLHttpRequest();
const requeteHTTP_send = new XMLHttpRequest();
const requeteHTTP_receive = new XMLHttpRequest();

requeteHTTP_create.onloadend = handler_create;
requeteHTTP_send.onloadend = handler_send;
requeteHTTP_receive.onloadend = handler_receive;

/* CREER QUEUE
 * Fonction pour gérer l'envoie de la requête requête "create_c" */
function create(nom_queue) {
	console.log("create called with nom_queue= "+nom_queue);
    requeteHTTP_create.open("POST", url_base, true);
    requeteHTTP_create.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    requeteHTTP_create.send("nom_queue="+nom_queue);
}
/* SEND QUEUE
 * Fonction pour gérer l'envoie de la requête "send_c" */
function send(nom_queue, message) {
    const url = url_base+nom_queue;
	console.log("send called with nom_queue= "+nom_queue+" et message= "+message);
    requeteHTTP_send.open("POST", url, true);
    requeteHTTP_send.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    requeteHTTP_send.send("nom_queue="+nom_queue+"&msg="+message);
}
/* RECEIVE QUEUE
 * Fonction pour gérer l'envoie de la requête "receive_c" */
function receive(_nom_queue) {
    const url = url_base+_nom_queue+"?nom_queue="+_nom_queue;
	console.log("receive called with nom_queue= "+_nom_queue);
    requeteHTTP_receive.open("GET", url, true);
    requeteHTTP_receive.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    requeteHTTP_receive.send(null);
}

/* HANDLER SEND QUEUE
 * Fonction pour gérer la reception du résultat de la requête "send_c" */
function handler_send() {
    if((requeteHTTP_send.readyState === 4) && (requeteHTTP_send.status === 200)) {
        console.log("doc json= "+JSON.stringify(requeteHTTP_send.responseText).replace(/\\/g, ""));
        let docJSON = JSON.parse(requeteHTTP_send.responseText);
        if(docJSON['state'] === 'OK') {
            console.log("requeteHTTP_send ok");
            $("#result_s").text("Le message a bien été posté dans la file");
		}
		else {
            console.log("requeteHTTP_send pas ok");
            $("#result_s").text("Le message n'as pas été posté dans la file");
		}
    }
    else {
        console.log("requeteHTTP_send pas ok du tout");
        $("#result_s").text("Erreur pour effecter la requête send message");
    }
}
/* HANDLER CREER QUEUE
 * Fonction pour gérer la reception du résultat de la requête requête "create_c" */
function handler_create() {
    if((requeteHTTP_create.readyState === 4) && (requeteHTTP_create.status === 200)) {
        console.log("doc json= "+JSON.stringify(requeteHTTP_create.responseText).replace(/\\/g, ""));
        let docJSON = JSON.parse(requeteHTTP_create.responseText);
        if(docJSON['state'] === 'OK') {
            console.log("requeteHTTP_create ok");
            $("#result_c").text("La file a bien été créée");
		}
		else {
            console.log("requeteHTTP_create pas ok");
            $("#result_c").text("La file n'a pas été créée");
		}
    }
    else {
        console.log("requeteHTTP_create pas ok du tout");
        $("#result_c").text("Erreur pour crée la file");
    }
}
/* HANDLER RECEIVE QUEUE
 * Fonction pour gérer la reception du résultat de la requête "receive_c" */
function handler_receive() {
    if((requeteHTTP_receive.readyState === 4) && (requeteHTTP_receive.status === 200)) {
        console.log("doc json= "+JSON.stringify(requeteHTTP_receive.responseText).replace(/\\/g, ""));
        let docJSON = JSON.parse(requeteHTTP_receive.responseText);
        if(docJSON['state'] === 'OK') {
            console.log("requeteHTTP_receive ok");
            $("#result_r").text("Le message reçu est \""+docJSON['msg']+"\"");
		}
		else {
            console.log("requeteHTTP_receive pas ok");
            $("#result_r").text("Aucun message reçu");
		}
    }
    else {
        console.log("requeteHTTP_receive pas ok du tout");
        $("#result_r").text("Erreur pour recevoir des messages");
    }
}

jQuery(function ($) {
    "use strict";

    $(document).ready(function () {

        // Action sur le bouton "créer la queue"
        $("#btn_c").on('click', function() {
            // on récupère le nom de la queue
            var nom = $("#nom_queue_c").val()
            console.log("name= "+nom);
            create(nom);
        });

        // Action sur le bouton "envoyer le message"
        $("#btn_s").on('click', function() {
            // on récupère le nom de la queue et  du message
            var nom = $("#nom_queue_s").val()
            var msg = $("#msg_queue_s").val()
            console.log("name= "+nom);
            console.log("msg= "+msg);
            send(nom, msg);
        });

        // Action sur le bouton "recevoir les messages"
        $("#btn_r").on('click', function() {
            // on récupère le nom de la queue
            var nom = $("#nom_queue_r").val()
            console.log("name= "+nom);
            receive(nom);
        });

    });

})