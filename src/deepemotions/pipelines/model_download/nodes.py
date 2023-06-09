from transformers import BertTokenizer, BertModel

def load_tokenizer(model_name):
  tokenizer = BertTokenizer.from_pretrained(model_name)

  return tokenizer

def load_model(model_name, num_labels):
  model = BertModel.from_pretrained(model_name, num_labels=num_labels)

  return model

