# SSLstrip

### Documentation

## Créer un fichier log de tout le traffic capturé.

```
ssl -w sniff_traffic.log
```
Cette commande permet enregistrer tout le traffic capturé dans un fichier log.

## Capture et logue uniquement les données de type "POST"
```
ssl -p -w sniff_traffic.log
```
Cette commande permet enregistrer tout le traffic capturé de type "POST" dans un fichier log.

## Capturer et loguer tout le traffic
```
sslstrip -a -w sniff_traffic.log
```
Cette commande permet de capturer tout le traffic SSL et HTTP

