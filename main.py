import pandas as pd

path = 'C:\\Users\\User\\PycharmProjects\\Hackathon-IML\\train.feats.csv'
df = pd.read_csv(path, encoding='utf8')


if __name__ == '__main__':
    for col in df.columns:
        print(col)