#!/bin/sh
echo "salut";
echo "on vérifie si le serveur rabbitmq est joignable"
ping -c 1 172.17.0.2;
echo "on vérifie si le serveur flask est joignable"
ping -c 1 172.17.0.3;
sleep 20;
