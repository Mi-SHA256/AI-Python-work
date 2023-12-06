import numpy as np
import pandas as pd

data = {
    'Name': ['Jschlatt', 'Jebadiah', 'Nick', 'Penguin'],
    'Year' : [1999, 2001, 1884, 2023],
    'City': ['NY', 'Boston', 'New Jersey', 'Toronto']
}

df = pd.DataFrame(data)

name_index = df['Name']
print("Chosen index: ")
print(name_index)

#first row
print("")
first = df.loc[0]
print("First row: ")
print(first)