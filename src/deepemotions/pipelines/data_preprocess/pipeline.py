"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import narrow_dataset, drop_discordant_annotations, clean_dataset, group_dataset

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=narrow_dataset,
            inputs="full-raw-dataset",
            outputs="narrowed-dataset",
            name="narrow_dataset_node",
        ),
        node(
            func=group_dataset,
            inputs="narrowed-dataset",
            outputs="grouped-dataset",
            name="group_dataset_node",
        ),
        node(
            func=drop_discordant_annotations,
            inputs="grouped-dataset",
            outputs="filtered-dataset",
            name="drop_discordant_annotations_node",
        ),
        node(
            func=clean_dataset,
            inputs="filtered-dataset",
            outputs="clean-dataset",
            name="clean_dataset_node",
        )
    ])
