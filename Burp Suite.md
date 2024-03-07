# Burp Suite Cheat Sheet

## Configuration initiale
- **Installation** : Télécharger depuis le site de PortSwigger.
- **Configuration du Proxy** : Configurer le navigateur pour utiliser le proxy de Burp (127.0.0.1:8080 par défaut).

## Composants principaux
### Proxy
- **Interception** : `Proxy > Intercept` pour capturer/modifier les requêtes/réponses.
- **Historique** : Examiner les requêtes passées sous `Proxy > HTTP history`.

### Spider
- **Lancement** : Utiliser pour automatiser l'exploration des applications web.

### Scanner
- **Scan Passif et Actif** : Identifier les vulnérabilités. Le scan actif doit être utilisé avec précaution pour éviter d'endommager le système cible.

### Intruder
- **Attaques** : Automatiser les attaques de type brute-force ou customisées.
- **Types d'attaques** : Sniper, Battering ram, Pitchfork, Cluster bomb.

### Repeater
- **Requêtes manuelles** : Envoyer des requêtes HTTP modifiées pour tester des vulnérabilités spécifiques.

### Sequencer
- **Analyse de tokens** : Évaluer la qualité des tokens de session ou autres.

### Decoder
- **Encodage/Décodage** : Convertir des données entre différents formats.

## Bonnes pratiques
- Toujours obtenir une autorisation formelle avant de tester un système.
- Utiliser Burp Suite dans un environnement de test ou avec des systèmes pour lesquels vous avez une permission explicite.

## Raccourcis utiles
- **Ctrl+I** : Activer/désactiver l'interception.
- **Ctrl+R** : Envoyer une requête du Proxy à Repeater.
- **Ctrl+S** : Envoyer une requête à Sequencer.

## Extensions
- Utiliser le BApp Store pour étendre les fonctionnalités de Burp Suite avec des plugins développés par la communauté.


