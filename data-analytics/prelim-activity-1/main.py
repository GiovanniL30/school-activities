import pandas as pd

class_csv = pd.read_csv('data/CLASS.csv')
resto_csv = pd.read_csv('data/resto1.csv')
sample_csv = pd.read_csv('data/SAMPLE.csv')

print(resto_csv.describe())
print(class_csv.describe())
print(sample_csv.describe())