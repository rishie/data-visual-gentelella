# data manipulations
import pandas as pd
from ast import literal_eval  # convert string to dictionary


# def get_data(path, columnNames):
def get_data(path):
    # columns = columnNames
    data_csv = pd.read_csv(path)
    data_json = data_csv.to_json()
    
    return literal_eval(data_json)
