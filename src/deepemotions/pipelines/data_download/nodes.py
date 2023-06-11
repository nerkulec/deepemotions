"""
This is a boilerplate pipeline 'data_download'
generated using Kedro 0.18.8
"""

import pandas as pd

def download_data(*remote_datasets) -> None:
    """
    Concatenates all remote datasets into one csv.

    Args:
        remote_datasets (list(pandas.CSVDataSet)) : csv datasets defined in conf/base/catalog.yml
    Returns: 
        full_dataset(pandasCSVDataSet):  concatenated dataset
    """
    # Concatenate all the datasets
    full_dataset = pd.concat(remote_datasets)
    print("Downloaded full datset of lenght:", len(full_dataset))

    return full_dataset


