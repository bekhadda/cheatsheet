# Cheat Sheet Gophish

Gophish est un framework open-source utilisé pour tester la sensibilisation à la sécurité par le biais de simulations d'attaques de phishing. Il permet de créer des campagnes de phishing simulées pour tester et éduquer les utilisateurs.

## Installation
Gophish est disponible sur GitHub. Vous pouvez le télécharger et l'installer à partir de là.

### Linux/macOS
```
wget https://github.com/gophish/gophish/releases/download/<VERSION>/gophish-v<VERSION>-linux-64bit.zip
unzip gophish-v<VERSION>-linux-64bit.zip
cd gophish
```

### Windows
Téléchargez le fichier .zip depuis la page de releases de Gophish, extrayez-le et exécutez `gophish.exe`.

## Configuration
Avant de démarrer Gophish, vous devriez configurer le fichier `config.json` pour répondre à vos besoins. Cela inclut la configuration des ports, de la base de données, et d'autres paramètres.

### Exemple de `config.json`
```json
{
    "admin_server": {
        "listen_url": "127.0.0.1:3333",
        "use_tls": true,
        "cert_path": "gophish_admin.crt",
        "key_path": "gophish_admin.key"
    },
    "phish_server": {
        "listen_url": "0.0.0.0:80",
        "use_tls": false,
        "cert_path": "example.crt",
        "key_path": "example.key"
    },
    "db_name": "sqlite3",
    "db_path": "gophish.db",
    "migrations_prefix": "db/db_"
}
```

## Démarrer Gophish
Pour démarrer Gophish, exécutez l'exécutable dans le répertoire Gophish.
- Sur Linux/macOS : `./gophish`
- Sur Windows : Double-cliquez sur `gophish.exe` ou exécutez-le depuis l'invite de commande.

## Utilisation
Une fois Gophish démarré, connectez-vous à l'interface d'administration en utilisant le navigateur web et accédez à l'URL indiquée par la console (par défaut `https://127.0.0.1:3333`).

### Créer une campagne
1. **Utilisateurs & Groupes** : Créez des utilisateurs et groupes à cibler.
2. **Modèles d'email** : Créez des modèles d'email qui seront envoyés.
3. **Pages d'atterrissage** : Créez des pages d'atterrissage que les utilisateurs verront après avoir cliqué sur les liens.
4. **URL de redirection** : Configurez où les utilisateurs seront redirigés après avoir interagi avec l'email.
5. **Rapports** : Analysez les résultats de la campagne.

## Conseils de sécurité
- Utilisez Gophish dans un environnement contrôlé.
- Assurez-vous d'avoir l'autorisation avant de lancer une campagne de phishing.
- Sensibilisez vos utilisateurs à l'objectif éducatif de ces campagnes.

Pour plus de détails et des guides d'utilisation, consultez la documentation officielle et la communauté Gophish sur GitHub.
