import pytorch_lightning as pl
from .data import EmotionDataModule
from .model import EmotionModel

def get_datamodule(df, tokenizer):
    """Get EmotionDataModule

    Args:
        df (pandas.CSVDataSet): dataset
        tokenizer (BertTokenizer): tokenizer to be used in datamodule

    Returns:
        (EmotionDataModule): initialized Data Module
    """
    return EmotionDataModule(df, tokenizer)

def get_model(pretrained_bert):
    """Gets EmotionModel

    Args:
        pretrained_bert (BertModel): Pre-trained Bert model

    Returns:
        (EmotionModel): initalized Emotion Model
    """
    return EmotionModel(pretrained_bert)

def get_trainer():
    """Get trainer

    Returns:
        (pl.Trainer): Trainer to be used to train model
    """
    return pl.Trainer(
        # gpus = 1,
        max_epochs = 5,
        # progress_bar_refresh_rate = 30
    )

def train_model(model, trainer, datamodule):
    """Trains model

    Args:
        model (EmotionModel): model to be trained
        trainer (pl.Trainer): chosen trainer
        datamodule (EmotionDataModule): datamodule with emotion dataset

    Returns:
        EmotionModel: trained model
    """
    trainer.fit(model, datamodule = datamodule)
    return model
