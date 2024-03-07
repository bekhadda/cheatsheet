# DNSChef Cheat Sheet

DNSChef est un outil de spoofing DNS flexible, utile pour rediriger le trafic d'un domaine vers une adresse IP spécifique lors des tests de pénétration ou des exercices de red teaming.

## Installation

DNSChef peut être installé directement depuis les dépôts de votre système d'exploitation ou cloné depuis son dépôt GitHub.

### Via Git

```bash
git clone https://github.com/iphelix/dnschef.git
cd dnschef
python dnschef.py
Utilisation de base
Pour lancer DNSChef et écouter sur toutes les interfaces réseau, utilisez :

bash
Copy code
python dnschef.py --fakeip 192.168.1.100
Cela redirigera toutes les requêtes DNS vers l'adresse IP 192.168.1.100.

Options avancées
Spécifier un domaine
Pour rediriger les requêtes d'un domaine spécifique, utilisez :

bash
Copy code
python dnschef.py --fakedomains example.com --fakeip 192.168.1.100
Exclure un domaine
Pour répondre normalement à certains domaines tout en redirigeant les autres :

bash
Copy code
python dnschef.py --nameserver 8.8.8.8 --passthrough example.com
Fichier de configuration
Vous pouvez également utiliser un fichier INI pour définir des réponses DNS spécifiques :

ini
Copy code
[example.com]
A = 192.168.1.100
AAAA = ::1
MX = mail.example.com
Et lancez DNSChef avec ce fichier :

bash
Copy code
python dnschef.py --file /chemin/vers/le/fichier.ini
Interface et port
Spécifiez l'interface réseau et le port d'écoute :

bash
Copy code
python dnschef.py --interface 192.168.1.1 --port 53
Bonnes pratiques
Utilisez DNSChef dans un environnement contrôlé : Assurez-vous d'avoir l'autorisation appropriée pour utiliser DNSChef dans votre réseau.
Tests de sécurité : Utilisez DNSChef pour simuler des attaques DNS et tester la résilience de votre réseau.
