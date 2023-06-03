"""
This is a boilerplate pipeline 'data_download'
generated using Kedro 0.18.8
"""

import pandas as pd

def download_data(*remote_datasets) -> None:
    """Download data from google API."""
    # Concatenate all the datasets
    full_dataset = pd.concat(remote_datasets)
    return full_dataset


