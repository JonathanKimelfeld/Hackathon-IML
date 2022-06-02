import pandas as pd
import sklearn
import numpy as np
import ast

# open file to read
path = 'C:\\Users\\User\\PycharmProjects\\Hackathon-IML\\train.labels.0.csv'
df = pd.read_csv(path, encoding='utf8', low_memory=False)


def create_responses(df):
    responses = ['BON - Bones', 'LYM - Lymph nodes', 'HEP - Hepatic', 'PUL - Pulmonary', 'PLE - Pleura', 'SKI - Skin',
                 'OTH - Other', 'BRA - Brain', 'MAR - Bone Marrow', 'PER - Peritoneum', 'ADR - Adrenals']
    for response in responses:
        df[response] = np.zeros(df.shape[0], )
    return df


def prepare_labels(df):
    df.columns = df.columns.str.replace('אבחנה-', '')
    df = create_responses(df)
    all_lists = df['Location of distal metastases']
    for index, label_list in enumerate(all_lists):
        sublist = ast.literal_eval(label_list)
        for sub in sublist:
            df.loc[index, sub] += 1

labels = prepare_labels(df)
# features i didnt include:
# KI67 protein,