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

def group_dataset(narrowed_dateset):
    grouped_dataset = narrowed_dateset.groupby(["id", "text"])
    return grouped_dataset 

def drop_discordant_annotations(grouped_dataset):
    filtered_dataset = grouped_dataset.sum()
    filtered_dataset = filtered_dataset.replace(to_replace = 1, value = 0).replace(
        to_replace = [
            k for k in range(2, filtered_dataset.max(axis = None) + 1 )],
              value = 1)
    filtered_dataset = filtered_dataset.loc[~(filtered_dataset==0).all(axis=1)]
    filtered_dataset = filtered_dataset.reset_index()
    return filtered_dataset 

def clean_dataset(filtered_dataset):
    clean_dataset = filtered_dataset.drop(['example_very_unclear'], axis = "columns")
    return clean_dataset

