from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from csv import DictReader

with open("index-egalite-fh-utf8.csv") as csvfile:
    reader = DictReader(csvfile, delimiter=";", quotechar='"')
    egapro_data = {row["SIREN"]: row for row in reader}

class EgaProService(ServiceBase):
    @rpc(Integer, _returns=Iterable(Unicode))
    def getEntreprise(ctx, siren):
        data = egapro_data.get(siren)
        if data:
            for key, value in data.items():
                yield f"{key}: {value}"
        else:
            yield f"Aucune entreprise trouvée avec le SIREN {siren}"

application = Application(
    [EgaProService],
    'spyne.examples.hello.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)
wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()
