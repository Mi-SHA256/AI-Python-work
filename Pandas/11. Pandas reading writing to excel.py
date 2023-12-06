import numpy as np
import pandas as pd

data = {
    'Name': ['Jschlatt', 'Jebadiah', 'Nick', 'Penguin'],
    'Year' : [1999, 2001, 1884, 2023],
    'City': ['NY', 'Boston', 'New Jersey', 'Toronto']
}

df = pd.DataFrame(data)

df.to_csv("watch_list.csv", index = False)

read = pd.read_csv("watch_list.csv")
print(read)