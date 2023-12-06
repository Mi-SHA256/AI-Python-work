import numpy as np
import pandas as pd

data = {
    'Name': ['Jschlatt', 'Jebadiah', 'Nick', 'Penguin'],
    'Year' : [1999, 2001, 1884, 2023],
    'City': ['NY', 'Boston', 'New Jersey', 'Toronto']
}


df = pd.DataFrame(data)

firstrows = df.head()
print(firstrows) #Displays first rows of the dataframe