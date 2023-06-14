import pytorch_lightning as pl
from .data import EmotionDataModule
from .model import EmotionClassifier

def get_datamodule(df):
    return EmotionDataModule(df)

def get_model(pretrained_bert):
    return EmotionClassifier(pretrained_bert)

def get_trainer():
    return pl.Trainer(
        gpus = 1,
        max_epochs = 5,
        progress_bar_refresh_rate = 30
    )

def train_model(model, trainer, datamodule):
    trainer.fit(model, datamodule = datamodule)
    return model
