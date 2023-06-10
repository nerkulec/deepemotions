"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import narrow_dataset, drop_discordant_annotations, drop_unclear_annotations, map_emotions, group_dataset, format_dataset, make_emotions_dicts


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=narrow_dataset,
            inputs="full-raw-dataset",
            outputs="narrowed_dataset",
            name="narrow_dataset_node",
        ),
        node(
            func=group_dataset,
            inputs="narrowed_dataset",
            outputs="grouped_dataset",
            name="group_dataset_node",
        ),
        node(
            func=drop_discordant_annotations,
            inputs="grouped_dataset",
            outputs="pre_filtered_dataset",
            name="drop_discordant_annotations_node",
        ),
        node(
            func=drop_unclear_annotations,
            inputs="pre_filtered_dataset",
            outputs="filtered_dataset",
            name="drop_unclear_annotations_node",
        ),
        node(
            func=make_emotions_dicts,
            inputs="filtered_dataset",
            outputs=["id_to_emotions_dict","emotions_to_id_dict"],
            name="make_emotions_dicts_node",
        ),
        node(
            func=map_emotions,
            inputs=["filtered_dataset", "emotions_to_id_dict"],
            outputs="mapped_dataset",
            name="map_emotions_node",
        ),
        node(
            func=format_dataset,
            inputs="mapped_dataset",
            outputs="formated_datest",
            name="format_dataset_node",
        )
        ])
