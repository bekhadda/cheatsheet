# Cheat Sheet Hydra

## Installation
Pour installer Hydra, utilisez pip :
```
pip install hydra-core
```

## Structure de base
- **`main.py`** : Le point d'entrée de votre application où vous initialisez Hydra.
- **`config`** : Un dossier contenant tous vos fichiers de configuration (.yaml ou .yml).

### Exemple de structure de dossier
```
.
├── main.py
└── config
    ├── config.yaml
    └── db
        └── mysql.yaml
```

## Initialiser Hydra dans votre application
Dans `main.py`, importez et initialisez Hydra :
```python
import hydra
from omegaconf import DictConfig

@hydra.main(config_path='config', config_name='config')
def main(cfg: DictConfig) -> None:
    print(cfg.pretty())

if __name__ == "__main__":
    main()
```

## Création de fichiers de configuration
Les fichiers de configuration sont en YAML. Vous pouvez créer différents fichiers pour différentes parties de votre application.

### Exemple `config.yaml`
```yaml
default:
  db: mysql

server:
  port: 8080
```

### Exemple `db/mysql.yaml`
```yaml
host: localhost
username: user
password: secret
database: testdb
```

## Surcharge des configurations par la ligne de commande
Hydra permet de surcharger facilement les configurations directement depuis la ligne de commande.

Exemple, changer le port du serveur :
```
python main.py server.port=1234
```

## Utilisation des groupes de configuration
Les groupes de configuration permettent de changer facilement entre différentes configurations.

Dans l'exemple ci-dessus, `default.db: mysql` spécifie que le groupe de configuration par défaut pour `db` est `mysql`. Vous pouvez facilement changer cela via la ligne de commande :
```
python main.py db=postgresql
```
Assurez-vous d'avoir un fichier de configuration correspondant pour `postgresql` sous `config/db`.

## Conseils supplémentaires
- **Composition**: Hydra est basé sur la composition de configurations, vous permettant de combiner plusieurs fichiers pour construire votre configuration finale.
- **Interpolation**: Hydra supporte l'interpolation entre les valeurs de configuration, vous permettant de réutiliser des valeurs définies ailleurs dans votre configuration.
- **Environnement et Overrides**: Vous pouvez également surcharger les configurations en utilisant des variables d'environnement ou en passant des paramètres supplémentaires lors de l'exécution.

Hydra est un outil puissant et flexible pour gérer les configurations, adapté à une large gamme d'applications, des scripts simples aux systèmes complexes. Pour plus de détails et des cas d'utilisation avancés, consultez la documentation officielle de Hydra.
