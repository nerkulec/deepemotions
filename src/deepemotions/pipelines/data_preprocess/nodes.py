"""
This is a boilerplate pipeline 'data_preprocess'
generated using Kedro 0.18.5
"""
def make_emotions_dicts(filtered_dataset):
    emotions = filtered_dataset["emotion"].unique()
    id_to_emotions_dict = {key: value for key, value in enumerate(emotions)}
    emotions_to_id_dict = {key: value for value, key in enumerate(emotions)}
    return id_to_emotions_dict, emotions_to_id_dict

def narrow_dataset(dataset):
    narrowed_dateset = dataset.drop(["author", "subreddit", "link_id",
                                          "parent_id", "created_utc", "rater_id"],
                                          axis = "columns")
    return narrowed_dateset

def group_dataset(narrowed_dateset):
    grouped_dataset = narrowed_dateset.groupby(["id"])
    return grouped_dataset 

def drop_discordant_annotations(grouped_dataset):
    pre_filtered_dataset = grouped_dataset.sum().replace(0, None).melt(
        id_vars="text", var_name="emotion", value_name="num_rated",
        ignore_index=False).dropna()
    pre_filtered_dataset = pre_filtered_dataset[
        pre_filtered_dataset["num_rated"] > 1]
    return pre_filtered_dataset 

def drop_unclear_annotations(pre_filtered_dataset):
    filtered_dataset = pre_filtered_dataset[
        ~pre_filtered_dataset["emotion"].isin(["example_very_unclear"])]
    return filtered_dataset


def map_emotions(filtered_dataset, emotion_mapping):
    mapped_filterd_dataset = filtered_dataset.replace({"emotion" : emotion_mapping})
    return mapped_filterd_dataset

def format_dataset(mapped_filterd_dataset):
    formated_dataset = mapped_filterd_dataset.drop("num_rated", axis = "columns")
    formated_dataset = formated_dataset.reset_index()
    formated_dataset["emotion"] = formated_dataset["emotion"].astype(str)
    formated_dataset = formated_dataset.groupby(["id", "text"]).agg({'emotion': ';'.join})
    formated_dataset = formated_dataset.reset_index()
    formated_dataset = formated_dataset[["text", "emotion", "id"]]
    return formated_dataset



