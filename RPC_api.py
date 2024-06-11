from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
from csv import DictReader

# Chargement initial des données
with open("index-egalite-fh-utf8.csv") as csvfile:
    reader = DictReader(csvfile, delimiter=";", quotechar='"')
    egapro_data = {row["SIREN"]: row for row in reader}

class EgaProRPCServer:
    def get_entreprise(self, siren):
        """
        Retourne les données EgaPro pour une entreprise spécifique (SIREN).
        
        :param siren: Le numéro SIREN de l'entreprise (int).
        :return: Les données de l'entreprise au format dictionnaire, ou un message d'erreur si non trouvée.
        """
        data = egapro_data.get(siren)
        if data:
            return data
        else:
            return {"error": f"Aucune entreprise trouvée avec le SIREN {siren}"}

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_instance(EgaProRPCServer())

print("Serveur RPC démarré sur http://localhost:8000")
server.serve_forever()
