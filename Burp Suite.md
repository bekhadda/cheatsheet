Burp Suite Cheat Sheet

Intercepter des requêtes

- Activer l'interception : Cliquez sur l'onglet "Proxy" → "Intercept" → "Intercept is On" (le bouton doit être en rouge)
- Désactiver l'interception : Cliquez sur l'onglet "Proxy" → "Intercept" → "Intercept is Off" (le bouton doit être en vert)
- Envoyer une requête interceptée : Cliquez sur le bouton "Forward" dans l'onglet "Intercept"
- Annuler une requête interceptée : Cliquez sur le bouton "Drop" dans l'onglet "Intercept"

Analyse des requêtes

- Historique des requêtes : Consultez l'onglet "Proxy" → "HTTP history" pour voir les requêtes précédentes
- Filtrer les requêtes : Utilisez les filtres pour afficher des requêtes spécifiques (par méthode, URL, hôte, etc.)
- Modifier une requête : Cliquez avec le bouton droit sur une requête dans l'historique et sélectionnez "Edit"

Analyse des réponses

- Inspecter la réponse : Sélectionnez une requête dans l'onglet "Proxy" puis consultez l'onglet "Response" pour voir la réponse du serveur
- Analyser les en-têtes : Regardez les en-têtes de réponse pour des informations telles que les cookies, les codes d'état, etc.
- Visualiser le contenu : Utilisez les onglets "HTML", "Raw" ou "Render" pour afficher le contenu de la réponse

Scanner des vulnérabilités

- Configurer le scanner : Allez dans l'onglet "Scanner" → "Options" pour régler les paramètres du scanner
- Lancer un scan : Sélectionnez une ou plusieurs requêtes dans l'onglet "Proxy" puis cliquez sur "Scanner" → "Start scan"
- Analyser les résultats : Consultez l'onglet "Scanner" → "Scan Queue" pour voir l'état des scans en cours et les résultats

Exploitation des vulnérabilités

- Utiliser l'outil d'intrusion : Allez dans l'onglet "Intruder" pour exploiter les vulnérabilités identifiées
- Configurer l'intrusion : Chargez une requête dans l'onglet "Intruder" puis configurez les positions de l'intrusion
- Lancer l'intrusion : Cliquez sur "Intruder" → "Start attack" pour lancer l'attaque

Analyse du trafic

- Monitorer le trafic : Utilisez l'onglet "Proxy" pour surveiller le trafic entre le navigateur et le serveur
- Exportation des données : Exportez les données capturées sous forme de fichier HAR pour une analyse ultérieure
