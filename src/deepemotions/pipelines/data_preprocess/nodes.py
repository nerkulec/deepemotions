"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""
def narrow_dataset(dataset):
    narrowed_dateset = dataset.drop([
        "author", "subreddit", "link_id",
        "parent_id", "created_utc", "rater_id"
    ], axis = "columns")
    return narrowed_dateset

def clean_dataset(narrowed_dataset):
    clean_dataset = narrowed_dataset[~narrowed_dataset['example_very_unclear']]
    clean_dataset = clean_dataset.drop(['example_very_unclear'], axis = "columns")
    return clean_dataset

