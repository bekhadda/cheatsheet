<!DOCTYPE html []>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="author" content="MarkdownViewer++" />
    <title>nouveau 6</title>
    <style type="text/css">
            
/* Avoid page breaks inside the most common attributes, especially for exports (i.e. PDF) */
td, h1, h2, h3, h4, h5, p, ul, ol, li {
    page-break-inside: avoid; 
}

        </style>
  </head>
  <body>
    <p>Burp Suite Cheat Sheet</p>
    <p>Intercepter des requêtes</p>
    <ul>
      <li>Activer l'interception : Cliquez sur l'onglet "Proxy" → "Intercept" → "Intercept is On" (le bouton doit être en rouge)</li>
      <li>Désactiver l'interception : Cliquez sur l'onglet "Proxy" → "Intercept" → "Intercept is Off" (le bouton doit être en vert)</li>
      <li>Envoyer une requête interceptée : Cliquez sur le bouton "Forward" dans l'onglet "Intercept"</li>
      <li>Annuler une requête interceptée : Cliquez sur le bouton "Drop" dans l'onglet "Intercept"</li>
    </ul>
    <p>Analyse des requêtes</p>
    <ul>
      <li>Historique des requêtes : Consultez l'onglet "Proxy" → "HTTP history" pour voir les requêtes précédentes</li>
      <li>Filtrer les requêtes : Utilisez les filtres pour afficher des requêtes spécifiques (par méthode, URL, hôte, etc.)</li>
      <li>Modifier une requête : Cliquez avec le bouton droit sur une requête dans l'historique et sélectionnez "Edit"</li>
    </ul>
    <p>Analyse des réponses</p>
    <ul>
      <li>Inspecter la réponse : Sélectionnez une requête dans l'onglet "Proxy" puis consultez l'onglet "Response" pour voir la réponse du serveur</li>
      <li>Analyser les en-têtes : Regardez les en-têtes de réponse pour des informations telles que les cookies, les codes d'état, etc.</li>
      <li>Visualiser le contenu : Utilisez les onglets "HTML", "Raw" ou "Render" pour afficher le contenu de la réponse</li>
    </ul>
    <p>Scanner des vulnérabilités</p>
    <ul>
      <li>Configurer le scanner : Allez dans l'onglet "Scanner" → "Options" pour régler les paramètres du scanner</li>
      <li>Lancer un scan : Sélectionnez une ou plusieurs requêtes dans l'onglet "Proxy" puis cliquez sur "Scanner" → "Start scan"</li>
      <li>Analyser les résultats : Consultez l'onglet "Scanner" → "Scan Queue" pour voir l'état des scans en cours et les résultats</li>
    </ul>
    <p>Exploitation des vulnérabilités</p>
    <ul>
      <li>Utiliser l'outil d'intrusion : Allez dans l'onglet "Intruder" pour exploiter les vulnérabilités identifiées</li>
      <li>Configurer l'intrusion : Chargez une requête dans l'onglet "Intruder" puis configurez les positions de l'intrusion</li>
      <li>Lancer l'intrusion : Cliquez sur "Intruder" → "Start attack" pour lancer l'attaque</li>
    </ul>
    <p>Analyse du trafic</p>
    <ul>
      <li>Monitorer le trafic : Utilisez l'onglet "Proxy" pour surveiller le trafic entre le navigateur et le serveur</li>
      <li>Exportation des données : Exportez les données capturées sous forme de fichier HAR pour une analyse ultérieure</li>
    </ul>
  </body>
</html>
