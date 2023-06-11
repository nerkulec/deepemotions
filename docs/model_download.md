To download model use model_downloading pipeline by running
```
kedro run --pipeline=model_download
```
## Overview

This pipeline downloads pre train bert model.

## Pipeline inputs

model_name(string) defined in `conf.base.parameters.model_download.yml`
## Nodes:

::: src.deepemotions.pipelines.model_download.nodes