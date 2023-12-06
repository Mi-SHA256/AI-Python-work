import numpy as np
import pandas as pd

data = {
    'Name': ['Jschlatt', 'Jebadiah', 'Nick', 'Penguin'],
    'Year' : [1999, 2001, 1884, 2023],
    'City': ['NY', 'Boston', 'New Jersey', 'Toronto']
}

df = pd.DataFrame(data)

#access first row and 'Name' column

rez = df.iloc[0]['Name'] #iloc means ITEM LOCATE, INDEX AND THEN COLUMN NAME
print(rez)

#SUBSET FIRST 2 ROWS AND ALL COLUMNS - LEAVE SPACE EMPTY TO MEAN ALL

subset = df.iloc[:2, :]
print(subset)