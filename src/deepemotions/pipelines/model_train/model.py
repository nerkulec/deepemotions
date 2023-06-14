from typing import Any
import torch
import pytorch_lightning as pl

class EmotionModel(pl.LightningModule):
    def __init__(self, pretrained_bert):
        super().__init__()
        self.bert = pretrained_bert
        self.dropout = torch.nn.Dropout(0.3)
        self.out = torch.nn.Linear(768, 28)

    def forward(self, x):
        output = self.bert(**x)
        output = self.dropout(output.pooler_output)
        output = self.out(output)
        return torch.sigmoid(output)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = torch.nn.functional.binary_cross_entropy(y_hat, y)
        self.log('train_loss', loss, on_step = True, on_epoch = True, prog_bar = True, logger = True)
        return loss
    
    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = torch.nn.functional.binary_cross_entropy(y_hat, y)
        self.log('val_loss', loss, on_step = True, on_epoch = True, prog_bar = True, logger = True)
        return loss
    
    def test_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = torch.nn.functional.binary_cross_entropy(y_hat, y)
        self.log('test_loss', loss, on_step = True, on_epoch = True, prog_bar = True, logger = True)
        return loss
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())
    
    def predict(self, text):
        self.eval()
        with torch.no_grad():
            return self(text)
        

        