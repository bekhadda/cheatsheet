# WifiPhisher

### Documentation

## Créer un point d'acces

```
wifiphisher -i eth0 -e "Wifi ouvert"
```
Cette commande permet de ouvrir un point d'acces sous le nom "Wifi ouvert", il ny'a pas d'authentification requise.

## Désauthentifier les client d'un ESSID pécis
```
wifiphisher -dE "NomDuRéseauCible"
```
Cette commande permet de déconnecter tous les clients d'un point wifi.

## Désauthentifier les client des canaux
```
wifiphisher -dC X  
```
Cette commande permet de déconnecter tous les clients d'un point wifi sur les caux définis.