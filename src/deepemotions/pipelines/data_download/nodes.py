"""
This is a boilerplate pipeline 'data_download'
generated using Kedro 0.18.8
"""

import pandas as pd

def download_data(*remote_datasets) -> None:
    """Download data from google API."""
    # Concatenate all the datasets
    full_dataset = pd.concat(remote_datasets)
    print("Downloaded full datset of lenght:", len(full_dataset))

    return full_dataset


