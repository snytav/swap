import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

tab = pd.read_html('https://www.cbr.ru/hd_base/bliquidity/?UniDbQuery.Posted=True&UniDbQuery.From=09.01.2017&UniDbQuery.To=07.10.2021')

print(len(tab))

df = tab[0]

print(df.head)

cols = df.columns
print(df.shape)
print(cols)
N,ncolumns = df.shape

print(df[cols[1]][0])

for k in range(1,ncolumns):
    print(k)
    df[cols[k]] = df[cols[k]].str.replace(' ', '')

print(df[cols[1]][0])

for k in range(1,ncolumns):
    df[cols[k]] = df[cols[k]].str.replace(',','.',regex=True)

print(df[cols[1]][0])


qq  =0

