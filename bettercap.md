
# Cheat Sheet Bettercap

Bettercap est un puissant framework de sécurité réseau, utilisé pour des attaques de type Man-In-The-Middle (MITM), reconnaissance de réseau, et plus. Il fonctionne sur Linux, macOS, et Windows.

## Installation

### Linux
Sur les distributions basées sur Debian (comme Ubuntu), installez Bettercap via apt-get :
```
sudo apt-get update
sudo apt-get install bettercap
```

### macOS
Utilisez Homebrew pour installer Bettercap :
```
brew install bettercap
```

### Windows
Bettercap peut être exécuté sur Windows à travers WSL (Windows Subsystem for Linux) ou en utilisant des conteneurs Docker.

## Démarrer Bettercap
Lancez Bettercap avec les privilèges super utilisateur pour avoir accès à toutes ses fonctionnalités :
```
sudo bettercap
```

## Interfaces utilisateur
- **CLI** : Bettercap propose une interface en ligne de commande interactive.
- **Web UI** : Pour une expérience utilisateur plus riche, Bettercap offre une interface web accessible à l'adresse `http://127.0.0.1:80` par défaut après avoir lancé le serveur web UI avec la commande `bettercap -caplet http-ui`.

## Commandes de base
- `help` : Affiche la liste des commandes disponibles.
- `net.probe on` : Active la reconnaissance du réseau.
- `net.show` : Affiche les hôtes détectés sur le réseau.
- `set <option> <value>` : Définit une option.
- `get <option>` : Affiche la valeur d'une option.
- `spoof.*` : Ensemble de commandes pour effectuer des attaques MITM.

## Exemples d'utilisation
- Écoute passive pour découvrir les hôtes sur le réseau :
  ```
  sudo bettercap -eval "set net.probe on; net.show"
  ```
- Attaque MITM pour intercepter le trafic entre des appareils :
  ```
  sudo bettercap -eval "set arp.spoof.targets <IP cible>; arp.spoof on; net.sniff on"
  ```

## Sécurité et éthique
- Bettercap est un outil puissant qui doit être utilisé de manière éthique et responsable.
- Assurez-vous d'avoir l'autorisation nécessaire avant d'utiliser Bettercap sur tout réseau ou appareil.

Pour plus d'informations et de guides détaillés sur les différentes fonctionnalités et capacités de Bettercap, consultez la documentation officielle sur [le site de Bettercap](https://www.bettercap.org/).
