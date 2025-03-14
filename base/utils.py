import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.conf import settings


def get_data_sample(dataframe):
    return dataframe.head().to_html()

def get_description(dataframe):
    return dataframe.describe().to_html()

def get_info(dataframe):
    return dataframe.info()

def get_filtered_data(dataframe, column, target_column, condition, value):
    #get the datatype
    try:
        value = eval(value)
        if type(value) == bool:
            value = str(value)
    except:
        value = value
    # try:
    if condition == '1':
        filtered_data = dataframe.loc[dataframe[column] == value]
        
    elif condition == '2':
        filtered_data = dataframe.loc[dataframe[column] > value]

    elif condition == '3':
        filtered_data = dataframe.loc[dataframe[column] < value]
        
    elif condition == '4':
        filtered_data = dataframe.loc[dataframe[column] != value]
    return filtered_data.to_html()
    # except:
    #     print("Not filterable data")

def get_categorical_and_numerical(dataframe):
    categorical_cols = []
    numerical_cols = []
    for col in dataframe.columns:
        if dataframe[col].dtype == 'object':
            categorical_cols.append(col)
        else:
            numerical_cols.append(col)
    return categorical_cols, numerical_cols

def save_figure(figure, filename):
    save_path = os.path.join(settings.MEDIA_ROOT, 'visualization', filename)
    figure.savefig(save_path)
    return filename

def visualize_all_types(dataframe, **kwargs):
    # Example: Creating a pair plot for numerical columns
    if len(kwargs.keys()) < 2:
        sns.pairplot(dataframe)
        plt.title("Pair Plot of Numerical Columns")
        save_path = save_figure(plt, 'pair_plot.png')
        plt.close()
    else:
        column1 = kwargs['visual_column1']
        column2 = kwargs['visual_column2']
        filtered_data = dataframe[[column1, column2]]
        sns.pairplot(filtered_data)
        plt.title('Bivariate Analysis for 2 cols')
        save_path = save_figure(plt, 'bivariate_analysis.png')
        plt.close()
    return save_path

def visualize_possible_bar_chart(dataframe):
    # Example: Creating a bar chart for a numerical column
    plt.figure(figsize=(10, 6))
    sns.countplot(x=dataframe.columns[0], data=dataframe)
    plt.title(f"Bar Chart of {dataframe.columns[0]}")
    plt.xticks(rotation=45)
    save_path = save_figure(plt, 'bar_chart.png')
    plt.close()
    return save_path

def visualize_possible_pie_chart(dataframe):
    # Example: Creating a pie chart for a categorical column
    plt.figure(figsize=(8, 8))
    dataframe[dataframe.columns[0]].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title(f"Pie Chart of {dataframe.columns[0]}")
    plt.axis('equal')
    save_path = save_figure(plt, 'pie_chart.png')
    plt.close()
    return save_path

def visualize_possible_count_plot(dataframe, column):
    plt.figure(figsize=(8,8))
    try:
        sns_plot = sns.countplot(dataframe[column])
        fig = sns_plot.get_figure()
        save_path = save_figure(fig, 'possible_count_plot.png')
        return save_path
    except:
        print('Count Plot Not Failed')

def visualize_hist_chart(dataframe, column):
    plt.figure(figsize=(8, 8))
    try:
        sns_plot = sns.histplot(data=dataframe, column=column)
        fig = sns_plot.get_figure()
        save_path = save_figure(fig, 'line_chart.png')
        return save_path
    except:
        print('Line Chart Not Failed')

def visualization(viz_type, dataset, **kwargs):
    df = pd.read_csv(dataset)
    if viz_type == '1':
        return visualize_all_types(df)
    elif viz_type == '2':
        numerical_cols = get_categorical_and_numerical(df)[1]
        if numerical_cols:
            return visualize_possible_bar_chart(df[[numerical_cols[0]]])
        else:
            return "No numerical columns to create a bar chart."
    elif viz_type == '3':
        categorical_cols = get_categorical_and_numerical(df)[0]
        if categorical_cols:
            return visualize_possible_pie_chart(df[[categorical_cols[0]]])
        else:
            return "No categorical columns to create a pie chart."
    elif viz_type == '4' :
        if 'visual_column1' in kwargs.keys():
            vis_col = kwargs['visual_column1']
            return visualize_possible_count_plot(df, vis_col)
        if 'visual_column1' in kwargs.keys() and 'visual_column2' in kwargs.keys():
            vis_col = visualize_all_types(df, visual_column1 = kwargs['visual_column1'], visual_column2=kwargs['visual_column2'])
    else:
        return "Invalid visualization type."

def summary(summary_type, dataset, **kwargs):
    df = pd.read_csv(dataset)
    if summary_type == '1':
        data_sample = get_data_sample(df)
        data_description = get_description(df)
        data_info = get_info(df)
        cat_cols, num_cols = get_categorical_and_numerical(df)
        return (data_sample ,data_description, data_info, cat_cols, num_cols)
    if summary_type == '2':
        data_info = get_info(df)
        return data_info
    if summary_type == '3':
        data_description = get_description(df)
        return data_description
    if summary_type == '4':
        cat_cols, num_cols = get_categorical_and_numerical(df)
        return cat_cols, num_cols
    if summary_type == '5':
        if 'column' in kwargs.keys() and 'target_column' in kwargs.keys() and 'condition' in kwargs.keys() and 'value' in kwargs.keys():
            column = kwargs['column']
            target_column = kwargs['target_column']
            condition = kwargs['condition']
            value = kwargs['value']
            filtered_data = get_filtered_data(df, column, target_column, condition, value)
            return filtered_data