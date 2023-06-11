## Data downloading
To download data use data_downloading pipeline by running
```
kedro run --pipeline=data_downloading
```
Alternatively you can download data manually by following instructions at [goemotions](https://github.com/google-research/google-research/tree/master/goemotions) to get datasets `goemotions_1.csv`, `goemotions_2.csv` and `goemotions_3.csv`. To get final dataset concatenate them into one `data/01_raw/goemotions-full-raw.csv` file.
## Overview

This pipeline downloads raw data from [google storage](https://storage.googleapis.com/gresearch/goemotions/data/full_dataset/goemotions_1.csv), concatenates it into one csv and saves it at `data/01_raw/goemotions-full-raw.csv`.

## Pipeline inputs

List of *remote* datasets defined in [`conf/base/catalog.yml`](./../conf/base/catalog.yml).  
In our case : `["remote-full-dataset-1", "remote-full-dataset-2", "remote-full-dataset-3"]`

## Nodes:

::: src.deepemotions.pipelines.data_download.nodes