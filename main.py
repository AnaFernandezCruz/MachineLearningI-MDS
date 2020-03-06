import utils as utl
import dtree as dtr
from sklearn.model_selection import train_test_split
import pandas as pd

# Carga el fichero previamente modificado con el scrip build_data.py
df = pd.read_csv("./export_dataframe.csv", delimiter=",")

# Limpiamos, imputamos valores ,transformamos columnas ... etc
tl = utl.Utils(df)
df = tl.tf_to_classes('precio', 'clase_precio', ['MUYBARATA', 'BARATA', 'NORMAL', 'CARA', 'MUYCARA'])

X, y = tl.split_to_model('clase_precio')


# Separamos el dataframe en los bloques que decidamos para luego entrenar nuestros modelos.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Modelos:
# 1. Decision tree

dtr = dtr.DTree(X_train, X_test, y_train, y_test)
dtr.train()




