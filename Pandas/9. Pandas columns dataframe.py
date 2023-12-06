import numpy as np
import pandas as pd

data = {
    'Name': ['Jschlatt', 'Schlagg', 'Nick', 'Penguin'],
    'Year' : [1999, 2001, 1884, 2023],
    'City': ['NY', 'Twin Towers', 'New Jersey', 'Nuke Paris']
}


df = pd.DataFrame(data)

multiple_c = df[['Name', 'City']]
print("Multiple Columns: ")
print(multiple_c)

multiple_rows = df.loc[[1,3]] #WHAT LOCATIONS YOU WANT ARE LISTED INSIDE THE 2 SQUARE BRACKETS
print("Multiple rows:")
print(multiple_rows)