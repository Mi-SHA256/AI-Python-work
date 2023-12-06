import pandas as pd
import numpy as np

#dataframe sorting

read = pd.read_csv("gangstas_watch_list.csv")
df = pd.DataFrame(read)

sorted_index = df.sort_index()
print(sorted_index) #sorting by index

print("")
sort_year = df.sort_values(by='Year')
print(sort_year) #sorting by a given value, can be any
