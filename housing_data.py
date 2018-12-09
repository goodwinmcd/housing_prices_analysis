import numpy as np
import pandas as pd
import os

def unique_col_vals(dataset):
    [print(pd.value_counts(dataset[column])) for column in dataset.keys()]

def create_col_dict(data):
    col_dict = {}
    for column in data.keys():
        col_dict[column] = {}
        for value in data[column].unique():
            col_dict[column][value] = {
                'mean': 0,
                'median': 0,
            }
    return col_dict

def get_median(column_dataset):
    return column_dataset.iloc(int(column_dataset.size/2))

def get_mean(column_dataset):
    return column_dataset.mean()

def get_column_info(data):
    data = data.sort_values(['Prices'])
    col_info = create_col_dict(data)
    for column in col_info:
        for value in col_info[column]:
            current_dataset = data.loc[data[column]] == value
            col_info[column][value]['median'] = get_median(current_dataset)
            col_info[column][value]['mean'] = get_mean(current_dataset)
    return col_info


houses = pd.read_csv(os.environ['housing_data'])
#unique_col_vals(houses)
mean_medians = get_column_info(houses)
