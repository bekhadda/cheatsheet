# Notice d'Utilisation du Script de Scan et Test de Sécurité

## Présentation

Ce script en Python est conçu pour automatiser le scan de sécurité d'une adresse IP cible. Il utilise une combinaison d'outils bien connus dans le domaine de la cybersécurité, tels que Nmap pour le scan de ports et la détection de services, Hydra pour le bruteforce de services SSH ouverts, et hping3 pour tester la robustesse du port 80 (HTTP). Les résultats sont ensuite formatés et enregistrés dans un fichier Markdown, permettant une lecture facile et une intégration aisée dans des rapports de sécurité ou des documentations de projet.

## Fonctionnalités

- **Scan Rapide Nmap :** Effectue un scan rapide des ports ouverts sur l'adresse IP cible et détecte les services en cours d'exécution.
- **Bruteforce SSH avec Hydra :** Si le port 22 (SSH) est ouvert, lance une attaque par bruteforce utilisant une liste d'utilisateurs et de mots de passe prédéfinis.
- **Détection de Version du Serveur :** Si le port 80 (HTTP) est ouvert, identifie la version du serveur web (par exemple, Apache) en cours d'exécution.
- **Test du Port 80 avec hping3 :** Utilise hping3 pour envoyer des paquets SYN au port 80, testant la réactivité et la robustesse du serveur face à des demandes de connexion.

## Prérequis

- Python 3.x installé sur votre système.
- Les outils Nmap, Hydra, et hping3 doivent être installés et accessibles depuis votre PATH système.
- Permissions nécessaires pour exécuter des scans de réseau et des attaques par bruteforce. **Utilisez ce script uniquement sur des systèmes pour lesquels vous avez une autorisation explicite.**

## Installation des Outils

### Sur Debian/Ubuntu

```bash
sudo apt-get update
sudo apt-get install nmap hydra hping3
```

## Utilisation

1. **Préparation :** Assurez-vous que les chemins vers vos fichiers de liste d'utilisateurs et de mots de passe sont correctement définis dans le script (`USER_LIST_PATH` et `PASS_LIST_PATH`).

2. **Exécution du Script :**

```bash
python3 nom_du_script.py
```

3. **Entrée de l'Adresse IP Cible :** Lorsque le script est lancé, il vous demandera d'entrer l'adresse IP de la cible à scanner.

4. **Consultation des Résultats :** Après l'exécution, les résultats seront disponibles dans un fichier Markdown nommé `rapport_{ip}.md`, où `{ip}` est l'adresse IP que vous avez scannée.

## Sécurité et Légalité

- **Permission :** Ne jamais utiliser ce script sur des réseaux ou des systèmes pour lesquels vous n'avez pas obtenu une permission explicite. L'utilisation non autorisée peut être illégale et contraire à l'éthique.
- **Sécurité :** Soyez conscient que l'exécution de scans et de tests peut affecter les performances du réseau et des systèmes cibles. Utilisez ce script de manière responsable.
