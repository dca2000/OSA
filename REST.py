from csv import DictReader

from flask import Flask, jsonify

# Chargement initial des données (une seule fois)
with open("index-egalite-fh-utf8.csv") as csvfile:
    reader = DictReader(csvfile, delimiter=";", quotechar='"')
    egapro_data = {row["SIREN"]: row for row in reader}

app = Flask(__name__)

@app.route("/entreprises")
def entreprises():
    """
    Retourne toutes les données EgaPro pour toutes les entreprises.
    """
    return jsonify(list(egapro_data.values()))

@app.route("/entreprises/<siren>")
def entreprise(siren):
    """
    Retourne les données EgaPro pour une entreprise spécifique (SIREN).
    
    :param siren: Le numéro SIREN de l'entreprise.
    :return: Les données de l'entreprise au format JSON, ou une erreur 404 si non trouvée.
    """
    data = egapro_data.get(siren)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": f"Aucune entreprise trouvée avec le SIREN {siren}"}), 404

if __name__ == "__main__":
    app.run(debug=True)
