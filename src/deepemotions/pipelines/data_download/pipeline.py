"""
This is a boilerplate pipeline 'data_download'
generated using Kedro 0.18.8
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import download_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=download_data,
            inputs=["remote-full-dataset-1", "remote-full-dataset-2", "remote-full-dataset-3"],
            outputs="full-dataset",
            name="download_data_node",
        )
    ])
