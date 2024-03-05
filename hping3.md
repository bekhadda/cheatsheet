# Hping3
Hping3 est un outil de test réseau en ligne de commande qui envoie divers types de paquets (TCP, UDP, ICMP, RAW-IP).

# Exemples 

## DDOS

```
hping3 -c 10000 --flood  -1 -I eth0 --rand-source
```
Cette commande enverra 10 000 paquets ICMP de type ping aussi rapidement que possible sur l'interface réseau eth0, en utilisant des adresses IP sources aléatoires pour chaque paquet.

## Scan des ports
```
hping3 --scan 0-6500 X.X.X.X
```
Cette commande utilise hping3 pour effectuer un balayage des ports de 0 à 6500 sur l'hôte dont l'adresse IP est X.X.X.X, afin de déterminer quels ports sont ouverts et quels services sont en cours d'exécution sur cet hôte.

## Découverte d'hote
```
hping3 -2 192.168.1.x --rand-dest -I eth0
```
Cette commande utilise hping3 pour envoyer des paquets de type ICMP (ping) avec des numéros de séquence aléatoires à l'adresse IP de 192.168.1.x via l'interface réseau eth0. L'option --rand-dest utilise des adresses IP de destination aléatoires pour chaque paquet ICMP envoyé.
