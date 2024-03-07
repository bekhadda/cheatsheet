import subprocess

# Chemins statiques vers les fichiers de liste d'utilisateurs et de mots de passe
USER_LIST_PATH = "/root/script/listutilisateur.txt"
PASS_LIST_PATH = "/root/script/listmotdepasse.txt"

def scan_rapide(ip):
    rapport = f"# Rapport de Scan pour {ip}\n\n"
    print("Lancement d'un scan rapide...")
    result = subprocess.run(["nmap", "-T4", "-F", ip], capture_output=True, text=True)
    print(result.stdout)
    rapport += "## Scan Rapide Nmap\n```\n" + result.stdout + "\n```\n"

    if "22/tcp open" in result.stdout:
        rapport += "### Port 22 (SSH) est ouvert\nTentative de bruteforce avec Hydra.\n\n"
        bruteforce_output = bruteforce_ssh(ip)
        rapport += "#### Résultats Bruteforce Hydra\n```\n" + bruteforce_output + "\n```\n"
    
    if "80/tcp open" in result.stdout:
        rapport += "### Port 80 (HTTP) est ouvert\nTentative d'identification de la version du serveur...\n\n"
        version_output = detecter_version_serveur(ip)
        rapport += "#### Version du Serveur\n```\n" + version_output + "\n```\n"
        hping_output = tester_port_80_avec_hping3(ip)
        rapport += "#### Test hping3 sur le port 80\n```\n" + hping_output + "\n```\n"
    
    # Enregistrement du rapport dans un fichier Markdown
    with open(f"rapport_{ip}.md", "w") as fichier_rapport:
        fichier_rapport.write(rapport)

    print(f"Rapport généré dans le fichier : rapport_{ip}.md")

def bruteforce_ssh(ip):
    print("Démarrage de Hydra pour bruteforce SSH...")
    result = subprocess.run(["hydra", "-L", USER_LIST_PATH, "-P", PASS_LIST_PATH, "ssh://" + ip], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout if result.stdout else "Aucun résultat ou erreur."

def detecter_version_serveur(ip):
    result = subprocess.run(["nmap", "-sV", "-p 80", ip], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout if result.stdout else "Aucun résultat ou erreur."

def tester_port_80_avec_hping3(ip):
    print("Test du port 80 avec hping3...")
    result = subprocess.run(["hping3", "-S", "-p", "80", "-c", "4", ip], capture_output=True, text=True)
    print(result.stdout)
    return result.stdout if result.stdout else "Aucun résultat ou erreur."

def main():
    ip = input("Entrez l'adresse IP cible : ")
    scan_rapide(ip)

if __name__ == "__main__":
    main()
