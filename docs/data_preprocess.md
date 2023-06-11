## Data downloading
Do preprocess data use data_preprocess pipeline by running
```
kedro run --pipeline=data_preprocess
```
## Overview

This pipeline preproceses downloaded dataset `data/01_raw/goemotions-full-raw.csv` and saves it in `data/02_intermediate/formated_full.csv`


## Pipeline inputs  
`full-raw-dataset` : pandas.CSVDataSet stored in `data/01_raw/goemotions-full-raw.csv`

## Nodes:
::: src.deepemotions.pipelines.data_preprocess.nodes