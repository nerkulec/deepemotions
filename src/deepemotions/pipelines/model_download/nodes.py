from transformers import BertTokenizer, BertModel

def load_tokenizer(model_name):
  """Loads Bert Tokenizer

  Args:
      model_name (string): Name of bert tokenizer to be used

  Returns:
      (BertTokenizer): tokenizer
  """
  tokenizer = BertTokenizer.from_pretrained(model_name)

  return tokenizer

def load_model(model_name, num_labels):
  """Load Bert model

  Args:
      model_name (string): Name of bert model to load
      num_labels (int): Number of classess

  Returns:
      (BertModel): loaded pretrained model
  """
  model = BertModel.from_pretrained(model_name, num_labels=num_labels)

  return model

