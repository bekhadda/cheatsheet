# Yersinia Cheat Sheet

## Introduction
Yersinia est un outil puissant pour réaliser des tests d'intrusion sur les réseaux, en se concentrant sur l'attaque de protocoles spécifiques. Il supporte des protocoles tels que Spanning Tree Protocol (STP), Cisco Discovery Protocol (CDP), Dynamic Trunking Protocol (DTP), et d'autres.

## Installation
Sur la plupart des distributions Linux, Yersinia peut être installé via le gestionnaire de paquets.

## Utilisation Générale
Lancer l'interface graphique :

Lancer en mode console pour un protocole spécifique (par exemple, STP) :

## Commandes de Base
- **Attaquer un réseau spécifique** : `yersinia -G` pour ouvrir l'interface graphique, puis sélectionner le protocole et l'attaque désirée.
- **Lister tous les protocoles supportés** : `yersinia -h`
- **Mode d'écoute** : `yersinia -I`, permet de surveiller les paquets de protocoles spécifiques.

## Attaques Spécifiques
### Spanning Tree Protocol (STP)
- **Devenir la racine du pont** : Cela peut être utilisé pour rediriger le trafic à travers un appareil contrôlé par l'attaquant.

### Cisco Discovery Protocol (CDP)
- **Envoyer de fausses annonces CDP** : Pour manipuler les informations de voisinage sur les commutateurs Cisco.

### Dynamic Trunking Protocol (DTP)
- **Forcer la négociation de trunking** : Pour écouter le trafic VLAN traversant un port qui n'est normalement pas en mode trunk.

## Bonnes Pratiques
- **Toujours obtenir une autorisation** : N'utilisez jamais Yersinia sans une permission explicite du propriétaire du réseau.
- **Tester dans un environnement sécurisé** : Utilisez Yersinia dans un laboratoire ou un environnement de test pour éviter d'endommager les réseaux en production.

## Ressources Additionnelles
- Documentation officielle de Yersinia : Consultez la documentation officielle pour une liste complète des commandes et des options d'attaque.

## Disclaimer
L'utilisation de Yersinia à des fins malveillantes est illégale. Cette cheat sheet est destinée à des fins éducatives pour les professionnels de la sécurité souhaitant améliorer la sécurité de leur réseau.

