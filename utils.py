import pandas as pd


class Utils:
    df = None

    def __init__(self, df):
        self.df = df

    def tf_to_classes(self, col, newCol, list):
        self.df[newCol] = pd.cut(self.df[col], len(list), labels=list)
        return self.df

    def split_to_model(self, col_y):
        df_y = self.df[col_y]
        df_x = self.df.loc[:, self.df.columns != col_y]
        return df_x, df_y
