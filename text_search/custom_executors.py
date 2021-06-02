from typing import Optional, Dict, Tuple

from jina import Executor, DocumentArray, requests, Document



class Printer(Executor):
    """Print input"""

    @requests
    def printer(self, docs, *args, **kwargs):
        print(f"------ DocumentArray: {docs}")
        for doc in docs:
            print(f"Doc: {doc}")
