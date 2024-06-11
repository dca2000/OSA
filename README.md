API EgaPro : Comparaison REST, SOAP et RPC
Ce projet présente trois implémentations différentes d'une API permettant d'accéder aux données d'égalité professionnelle des entreprises françaises (EgaPro) :

API REST (Representational State Transfer)
Principe: Suit les principes REST, utilisant les verbes HTTP (GET, POST, PUT, DELETE) pour manipuler les ressources (entreprises) identifiées par des URI (Uniform Resource Identifiers).
Format de données: Utilise principalement JSON pour la représentation des données.
Avantages: Simplicité, évolutivité, large adoption, facilité d'utilisation avec des outils web.
Inconvénients: Peut être moins performante que SOAP ou RPC pour certaines opérations complexes.
API SOAP (Simple Object Access Protocol)
Principe: Basée sur le protocole SOAP, qui utilise XML pour structurer les messages et définit un ensemble de règles pour les interactions entre les applications.
Format de données: Utilise exclusivement XML.
Avantages: Standardisée, adaptée aux environnements d'entreprise, permet des opérations complexes et transactionnelles.
Inconvénients: Plus complexe à mettre en œuvre et à utiliser que REST, plus verbeuse.
API RPC (Remote Procedure Call)
Principe: Permet d'appeler des fonctions sur un serveur distant comme si elles étaient exécutées localement.
Format de données: Utilise généralement un format de sérialisation comme XML-RPC ou JSON-RPC.
Avantages: Simple à implémenter et à utiliser pour des opérations spécifiques, peut être plus performante que SOAP pour certaines applications.
Inconvénients: Moins flexible que REST, peut entraîner un couplage fort entre le client et le serveur.
Structure du projet
rest_api.py: Implémentation de l'API REST.
soap_api.py: Implémentation de l'API SOAP (nécessite l'installation de Spyne).
rpc_api.py: Implémentation de l'API RPC (utilise le module xmlrpc de Python).
index-egalite-fh-utf8.csv: Fichier de données EgaPro (à placer dans le même répertoire).
Utilisation
API REST
bash
Copier le code
python rest_api.py
API SOAP
bash
Copier le code
python soap_api.py
API RPC
bash
Copier le code
python rpc_api.py
Ce README fournit une vue d'ensemble des différentes approches d'implémentation d'API, leurs avantages et inconvénients, et la structure du projet. Pour utiliser chaque API, exécutez le script Python correspondant après avoir placé le fichier de données index-egalite-fh-utf8.csv dans le même répertoire.