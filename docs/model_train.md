To download model use model_downloading pipeline by running
```
kedro run --pipeline=model_train
```
## Overview

This pipeline creates and trains model.

## Pipeline inputs
clean-dataset, bert-tokenizer, bert-model defined in `conf.base.parameters.catalog.yml`

## Nodes:

::: src.deepemotions.pipelines.model_train.nodes

## Dataset and datamodule

::: src.deepemotions.pipelines.model_train.data

## Model
::: src.deepemotions.pipelines.model_train.model

