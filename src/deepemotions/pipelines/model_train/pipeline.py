"""
This is a boilerplate pipeline 'model_train'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import get_datamodule, get_model, get_trainer, train_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=get_datamodule,
            inputs="clean-dataset",
            outputs="datamodule",
            name="get_datamodule_node",
        ),
        node(
            func=get_model,
            inputs="bert-model",
            outputs="model",
            name="get_model_node",
        ),
        node(
            func=get_trainer,
            inputs=None,
            outputs="trainer",
            name="get_trainer_node",
        ),
        node(
            func=train_model,
            inputs=["model", "trainer", "datamodule"],
            outputs="trained-model",
            name="train_model_node",
        ),
    ])
