import pytorch_lightning as pl
from .data import EmotionDataModule
from .model import EmotionModel

def get_datamodule(df, tokenizer):
    return EmotionDataModule(df, tokenizer)

def get_model(pretrained_bert):
    return EmotionModel(pretrained_bert)

def get_trainer(logger):
    return pl.Trainer(
        # gpus = 1,
        max_epochs = 5,
        logger = logger
        # progress_bar_refresh_rate = 30
    )

def train_model(model, trainer, datamodule):
    trainer.fit(model, datamodule = datamodule)
    return model

def get_logger(logger_params):
    logger = pl.loggers.WandbLogger(
        project=logger_params['project_name'],
        entity=logger_params['entity_name'],
        # config=model_params,
        log_model=True,
    )
    return logger
