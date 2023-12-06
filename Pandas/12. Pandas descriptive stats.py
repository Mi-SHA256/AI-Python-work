import pandas as pd
import numpy as np

#data = {
#    'Name': ['Jschlatt', 'Schlagg', 'Nick', 'Penguin'],
#    'Year' : [1999, 2001, 1884, 2023],
#    'City': ['NY', 'Twin Towers', 'New Jersey', 'Nuke Paris']
#}

#df = pd.DataFrame(data)

#Commented data to test if .csv file works the same

read = pd.read_csv("gangstas_watch_list.csv")  #read from file

df = pd.DataFrame(read)

stats = df.describe() #shows descriptive stats on the dataframe
print(stats)


