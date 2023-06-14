import pytorch_lightning as pl
import torch
from sklearn.model_selection import train_test_split

class EmotionDataset(torch.utils.data.Dataset):
    def __init__(self, df, tokenizer):
        text = df['text'].values
        # self.X = text
        self.X = tokenizer(
            text.tolist(),
            padding = True,
            truncation = True,
            max_length = 512,
            return_tensors = 'pt'
        )
        emotions = df.columns[2:]
        self.y = torch.tensor(df[emotions].values, dtype = torch.float32)
    
    def __getitem__(self, idx):
        return {
            'input_ids': self.X['input_ids'][idx],
            'attention_mask': self.X['attention_mask'][idx],
            'token_type_ids': self.X['token_type_ids'][idx],
        }, self.y[idx]
    
    def __len__(self):
        return len(self.X)
    
class EmotionDataModule(pl.LightningDataModule):
    def __init__(self, df, tokenizer, batch_size = 32):
        super().__init__()

        train_df, val_df = train_test_split(df, test_size = 0.3, random_state = 42)
        val_df, test_df = train_test_split(val_df, test_size = 0.5, random_state = 42)
        self.train_df = train_df
        self.val_df = val_df
        self.test_df = test_df
        self.batch_size = batch_size
        self.tokenizer = tokenizer
    
    def setup(self, stage = None):
        self.train_dataset = EmotionDataset(self.train_df, self.tokenizer)
        self.val_dataset = EmotionDataset(self.val_df, self.tokenizer)
        self.test_dataset = EmotionDataset(self.test_df, self.tokenizer)
    
    def train_dataloader(self):
        return torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size = self.batch_size,
            shuffle = True,
            num_workers = 4
        )
    
    def val_dataloader(self):
        return torch.utils.data.DataLoader(
            self.val_dataset,
            batch_size = self.batch_size,
            shuffle = False,
            num_workers = 4
        )
    
    def test_dataloader(self):
        return torch.utils.data.DataLoader(
            self.val_dataset,
            batch_size = self.batch_size,
            shuffle = False,
            num_workers = 4
        )

