"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""
def narrow_dataset(dataset):
    """Drops unnecesary columns from dataset. 
    Remaining columns are: 'text', 'id', 'example_very_unclear' and columns representing emotion categories.

    Args:
        dataset (pandas.CSVDataSet): Dataset to be processed

    Returns:
        (pandas.CSVDataSet): narrowed dataset
    """
    unnecesary_columns=["author", "subreddit", "link_id",
                        "parent_id", "created_utc", "rater_id"]
    narrowed_dataset = dataset.drop(unnecesary_columns,
                                    axis = "columns")
    return narrowed_dataset

def group_dataset(narrowed_dateset):
    """Groups data in dataset by comment id.

    Args:
        narrowed_dateset (pandas.CSVDataSet): dataset with only relevant columns

    Returns:
        (CSVDataSet): grouped dataset
    """
    grouped_dataset = narrowed_dateset.groupby(["id", "text"])
    return grouped_dataset 

def drop_discordant_annotations(grouped_dataset):
    """Drops annotations given by just one rater.

    Args:
        grouped_dataset (pandas.CSVDataSet): dataset grouped by comment id and text

    Returns:
        (pandas.CSVDataSet): filtered dataset
    """
    filtered_dataset = grouped_dataset.sum()
    filtered_dataset = filtered_dataset.replace(to_replace = 1, value = 0).replace(
        to_replace = [
            k for k in range(2, filtered_dataset.max(axis = None) + 1 )],
              value = 1)
    filtered_dataset = filtered_dataset.loc[~(filtered_dataset==0).all(axis=1)]
    filtered_dataset = filtered_dataset.reset_index()
    return filtered_dataset 

def clean_dataset(filtered_dataset):
    """Clean 

    Args:
        filtered_dataset (pandas.CSVDataSet): 

    Returns:
        (CSVDataSet): cleaned dataset
    """
    clean_dataset = filtered_dataset.drop(['example_very_unclear'], axis = "columns")
    return clean_dataset

