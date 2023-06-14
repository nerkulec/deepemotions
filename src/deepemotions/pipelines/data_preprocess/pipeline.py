"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import narrow_dataset, clean_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=narrow_dataset,
            inputs="full-raw-dataset",
            outputs="narrowed-dataset",
            name="narrow_dataset_node",
        ),
        node(
            func=clean_dataset,
            inputs="narrowed-dataset",
            outputs="clean-dataset",
            name="clean_dataset_node",
        ),
    ])
