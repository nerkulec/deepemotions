# deepemotions
**Team: Magdalena Buszka, Bartosz Brzoza**  

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


## Overview

The aim of this project is to classify emotions associated with comments.
For training we used google's [goemotions](https://github.com/google-research/google-research/tree/master/goemotions) dataset. 