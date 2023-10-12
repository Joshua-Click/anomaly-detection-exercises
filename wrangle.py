# imports
import pandas as pd
import numpy as np
import os

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from sklearn import metrics
from random import randint
from matplotlib import style
import env as e
import warnings
warnings.filterwarnings("ignore")


def check_columns(df, reports=False, graphs=False):
    """
    This function takes a pandas dataframe as input and returns
    a dataframe with information about each column in the dataframe. For
    each column, it returns the column name, the number of
    unique values in the column, the unique values themselves,
    the number of null values in the column, the proportion of null values,
    the data type of the column, and the range of the column if it is float or int. The resulting dataframe is sorted by the
    'Number of Unique Values' column in ascending order.

    Args:
    - df: pandas dataframe

    Returns:
    - pandas dataframe
    """
    print(f"Total rows: {df.shape[0]}")
    print(f"Total columns: {df.shape[1]}")
    if reports == True:
        describe = df.describe().round(2)
        pd.DataFrame(describe)
        print(describe)
    if graphs == True:
        df.hist(bins=20, figsize=(10, 10))
        plt.show()
    data = []
    # Loop through each column in the dataframe
    for column in df.columns:
        # Append the column name, number of unique values, unique values, number of null values, proportion of null values, and data type to the data list
        if df[column].dtype in ["float64", "int64"]:
            data.append(
                [
                    column,
                    df[column].dtype,
                    df[column].nunique(),
                    df[column].isna().sum(),
                    df[column].isna().mean().round(5),
                    df[column].unique(),
                    df[column].describe()[["min", "max", "mean"]].values,
                ]
            )
        else:
            data.append(
                [
                    column,
                    df[column].dtype,
                    df[column].nunique(),
                    df[column].isna().sum(),
                    df[column].isna().mean().round(5),
                    df[column].unique(),
                    None,
                ]
            )
    # Create a pandas dataframe from the data list, with column names 'Column Name', 'Number of Unique Values', 'Unique Values', 'Number of Null Values', 'Proportion of Null Values', 'dtype', and 'Range' (if column is float or int)
    # Sort the resulting dataframe by the 'Number of Unique Values' column in ascending order
    return pd.DataFrame(
        data,
        columns=[
            "col_name",
            "dtype",
            "num_unique",
            "num_null",
            "pct_null",
            "unique_values",
            "range (min, max, mean)",
        ],
    )


def get_curlogs():
    '''This function imports codeup curriculum access logs data 
    from MySql codeup server and creates a csv
    
    argument: None
    
    returns: df'''
    filename = "anonymized_curriculum.csv"
    # if file exists, it opens it as df, if not, it pulls it from mysql
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT * FROM logs;
        """
        connection = e.get_db_url("curriculum_logs")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df

def get_cohorts():
    '''This function imports codeup cohort name data 
    from MySql codeup server and creates a csv
    
    argument: None
    
    returns: df'''
    filename = "cohort_id.csv"
    # if file exists, it opens it as df, if not, it pulls it from mysql
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT * FROM cohorts;
        """
        connection = e.get_db_url("curriculum_logs")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df

def prep_logs(df, df2):
    '''combines cohort data to the curriculum logs
    
    argument: df, df2
    
    returns: prepped df'''
    # fills na values
    df = df.fillna(value= -1)
    # merges 2 dataframes on a left join
    df = df.merge(df2, how='left', left_on= 'cohort_id', right_on='id')
    # creates extra columns
    df['endpoint'] = df['path'].str.split('/').str[-1]
    df['startpoint'] = df['path'].str.split('/', n=1).str[0]
    # converts cohort id to int
    df['cohort_id'] = df['cohort_id'].astype(int)
    # sets date to date time and index
    df.date = pd.to_datetime(df.date)
    df = df.set_index(df.date, drop=True)
    # drops unused columns
    df = df.drop(columns=['time', 'slack', 'deleted_at', 'created_at', 'updated_at'])

    return df

def split_by_program(df):
    '''Takes the df and splits into 4 smaller ones by program_id'''
    pgm1 = df[df['program_id'] == 1]
    pgm2 = df[df['program_id'] == 2]
    pgm3 = df[df['program_id'] == 3]
    pgm4 = df[df['program_id'] == 4]

    return pgm1, pgm2, pgm3, pgm4