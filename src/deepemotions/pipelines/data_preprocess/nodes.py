def make_emotions_dicts(filtered_dataset):
    """Create mapping between emotions(categories) names and their numerical ids.

    Args:
        filtered_dataset (pandas.CSVDataSet): filtered dataset

    Returns:
        tuple(dict(int: string), dict(string: int)): mapping from id to emotion name, and from emotion name to id
    """
    emotions = filtered_dataset["emotion"].unique()
    id_to_emotions_dict = {key: value for key, value in enumerate(emotions)}
    emotions_to_id_dict = {key: value for value, key in enumerate(emotions)}
    return id_to_emotions_dict, emotions_to_id_dict

def narrow_dataset(dataset):
    """Drops unnecesary columns from dataset. 
    Remaining columns are: 'text', 'id', 'example_very_unclear' and columns representing emotion categories.

    Args:
        dataset (pandas.CSVDataSet): Dataset to be processed

    Returns:
        pandas.CSVDataSet: narrowed dataset
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
        CSVDataSet: grouped dataset
    """
    grouped_dataset = narrowed_dateset.groupby(["id"])
    return grouped_dataset 

def drop_discordant_annotations(grouped_dataset):
    """Drops annotations given by just one rater.

    Args:
        grouped_dataset (pandas.CSVDataSet): dataset grouped by comment id

    Returns:
        pandas.CSVDataSet: pre filtered dataset
    """
    pre_filtered_dataset = grouped_dataset.sum().replace(0, None).melt(
        id_vars="text", var_name="emotion", value_name="num_rated",
        ignore_index=False).dropna()
    pre_filtered_dataset = pre_filtered_dataset[
        pre_filtered_dataset["num_rated"] > 1]
    return pre_filtered_dataset 

def drop_unclear_annotations(pre_filtered_dataset):
    """Removes unclear examples from dataset.

    Args:
        pre_filtered_dataset (pandas.CSVDataSet): pre filtered dataset

    Returns:
        pandas.CSVDataSet: filtered dataset
    """
    filtered_dataset = pre_filtered_dataset[
        ~pre_filtered_dataset["emotion"].isin(["example_very_unclear"])]
    return filtered_dataset


def map_emotions(filtered_dataset, emotion_mapping):
    """Replaces string names of emotions with their ids

    Args:
        filtered_dataset (pandas.CSVDataSet): filtered dataset to process
        emotion_mapping (dict): mapping between emotion names and their ids.

    Returns:
        CSVDataSet: mapped filtered dataset
    """
    mapped_filtered_dataset = filtered_dataset.replace({"emotion" : emotion_mapping})
    return mapped_filtered_dataset

def format_dataset(mapped_filterd_dataset):
    """Format dataset.
    Formated dataset has columns:
        - text : text of the comment
        - emotion : numerical values of emotions annotated to comment
        - id : unique record identifier

    Args:
        mapped_filterd_dataset (pandas.CSVDataSet): mapped and filtered dataset to format

    Returns:
        pandas.CSVDataSet: formated dataset
    """
    formated_dataset = mapped_filterd_dataset.drop("num_rated", axis = "columns")
    formated_dataset = formated_dataset.reset_index()
    formated_dataset["emotion"] = formated_dataset["emotion"].astype(str)
    formated_dataset = formated_dataset.groupby(["id", "text"]).agg({'emotion': ';'.join})
    formated_dataset = formated_dataset.reset_index()
    formated_dataset = formated_dataset[["text", "emotion", "id"]]
    return formated_dataset



