import pretty_errors
from executors import MyIndexer, MyTransformer
from jina import Flow, Document, DocumentArray, Executor, requests


class Capitalizer(Executor):
    """Capitalizer executor class """

    @requests
    def capitalize(self, docs, *args, **kwargs):
        for doc in docs:
            doc.text = doc.text.upper()


doc1 = Document(
    content="""
Superman, born Kal-El and legally named Clark Joseph Kent, is the last son of Krypton, sent as the dying planet's last hope to Earth, where he grew to become its protector. Though he was apparently killed shortly after the Darkseid War, his essence merged with the New Earth Superman in Rebirth, creating a new, merged timeline for Superman.
""",
    tags = {
        "secret_identity": "Clark Kent",
        "home": "Metropolis",
        "powers": ["Flight", "X-ray vision", "Strength"]
    }
)

doc2 = Document(
    content="""
Batman is the super-hero protector of Gotham City, a man dressed like a bat who fights against evil and strikes terror into the hearts of criminals everywhere. In his secret identity, he assumes the alias of Bruce Wayne, billionaire industrialist and notorious playboy; though "Bruce Wayne" is technically his real name, this Bruce Wayne is a disguise--that of the man he would have been had his parents not been murdered before his eyes when he was no more than a mere boy. 
""",
    tags = {
        "secret_identity": "Bruce Wayne",
        "home": "Gotham",
        "powers": ["Money"]
    }
)

docs = DocumentArray([doc1, doc2])

flow = Flow().add(uses=Capitalizer).add(uses=MyTransformer).add(uses=MyIndexer)

with flow:
    flow.post(on="/index", inputs=docs, on_done=print)
    flow.use_rest_gateway(45678)
    flow.block()

