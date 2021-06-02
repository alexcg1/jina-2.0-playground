import pretty_errors
from helper import docs, Capitalizer
from executors import MyIndexer, MyTransformer
from jina import Flow


flow = Flow.load_config('flow.yml')

with flow:
    flow.post(on="/index", inputs=docs, on_done=print)
    flow.use_rest_gateway(45678)
    flow.block()

