"""
This is a boilerplate pipeline 'model_download'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_tokenizer, load_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_tokenizer,
            inputs="params:model_name",
            outputs="bert-tokenizer",
            name="load_tokenizer_node",
        ),
        node(
            func=load_model,
            inputs=["params:model_name", "params:num_labels"],
            outputs="bert-model",
            name="load_model_node",
        ),
    ])
