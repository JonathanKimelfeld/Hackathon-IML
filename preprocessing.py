import pandas as pd
import sklearn

# open file to read
path = 'C:\\Users\\User\\PycharmProjects\\Hackathon-IML\\train.feats.csv'
df = pd.read_csv(path, encoding='utf8', low_memory=False)
# print(df.columns.unique())
# print(df[' Form Name'].unique())
# use id column to create a new column which will state amount of visits per subject until the
# current date.

# The columns that we transform into categorical:
#   form name - to categorical 9 values that state the type of medical visit (to be binary)
#   hospital
#   username (the doctor) - maybe? to reconsider
#   Histological diagnosis
#   Histopatological degree:
#       GX - we connot set a score.
#       G1 - low score up to G4 - high score (G3 and G4 refer to a greater scale of disease)
#

# To check outliers / logical figures:
#   Age

# various formats:
#   Her2: Informative Gen for diagnosis of cancer - positive or negative

def to_binary(df): #TODO
    to_binary = ['Ivi -Lymphovascular invasion']

def drop_cols(df):
    cols_to_drop = ['KI67 protein']
    df.drop(cols_to_drop
            )
# dates: diagnosis and surgeries
def set_null(df):
    clear_nulls = ['Histopatological degree', 'Basic stage', 'Histological diagnosis',
                   "Lymphatic penetration"]
    for col in clear_nulls:
        for null in ['Null', 'NULL', 'nan']:
            df[col] = df[col].replace(null, None)

def set_dummies(df):
    to_dummies = [' Form Name', ' Hospital', 'User Name', 'Basic stage', 'Histological diagnosis']
    for dummy in to_dummies:
        df = pd.get_dummies(df, prefix=dummy, columns=[dummy])
    return df

def check_outliers(df):
    to_check = ['Age']

def prepare_data(df):
    df.columns = df.columns.str.replace('אבחנה-', '')
    set_null(df)
    df = set_dummies(df)
    return df

def split_data(X_file_name, y_file_name):
    X = pd.read_csv(X_file_name)
    y = pd.read_csv(y_file_name)
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.3)
    X_dev, X_test, y_dev, y_test = sklearn.model_selection.train_test_split(X_test, y_test, test_size=0.5)
    return X_train, y_train, X_dev, y_dev, X_test, y_test


df = prepare_data(df)
print(df.columns)

# features i didnt include:
# KI67 protein,