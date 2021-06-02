from jina import Flow, Document, DocumentArray, Executor, requests


class Capitalizer(Executor):
    """Capitalizer executor class """

    @requests
    def capitalize(self, docs, *args, **kwargs):
        for doc in docs:
            doc.text = doc.text.upper()
