from transformers import BertTokenizer, BertModel

def load_tokenizer():
  tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

  return tokenizer

def load_model():
  model = BertModel.from_pretrained("bert-base-uncased")

  return model

