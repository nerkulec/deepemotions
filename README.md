# deepemotions
**Team: Magdalena Buszka, Bartosz Brzoza, Martyna Firgolska**  

## Install
  
```bash 
git clone https://github.com/nerkulec/deepemotions.git
# git clone git@github.com:nerkulec/deepemotions.git
cd deepemotions
conda env create --file conda.yml
conda activate deepemotions
pip install -r requirements.txt
# Adding new package
pip install <package>
# pip install pipreqs
pipreqs .
```

## Run project
```
kedro run
```

### Download data

```
kedro run --pipeline=data_download
```

### Preprocess data

Assuming the data is already downloded
```
kedro run --pipeline=data_preprocess
```

### Download pre-trained model

```
kedro run --pipeline=model_download
```

### Train model

Assuming the pre-trained model is already downloded and data is already downloaded and preprocessed 
```
kedro run --pipeline=model_train
```

### Logging to wandb

If not already logged before running the training log in to Wandb to save logs.
You will need to input your key.

```
wandb login
```

## Overview

The aim of this project is to classify emotions associated with comments.
For training we used google's [goemotions](https://github.com/google-research/google-research/tree/master/goemotions) dataset. 