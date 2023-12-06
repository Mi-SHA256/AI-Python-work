import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data
df = pd.read_csv("KDDTrain+_20Percent.csv")

#convert column to numeric, handling non-numbers errors
df['src_bytes'] = pd.to_numeric(df['src_bytes'], errors="coerce")

#convert duration to numeric, errors

df['duration'] = pd.to_numeric(df['duration'], errors = 'coerce')

print("Exploring Dataset first rows: ")
print(df.head())

print("")

print("Getting info about dataset: ")
print(df.info())

print("")

print("Basic Data Analysis (Numerical columns): ")
print(df.describe())

print("")

print("Count of unique values in 'class' column: ")
print(df['class'].value_counts())

print("")
print("Data Visualization")
print("")

#Bar Chart
prot_count = df['protocol_type'].value_counts()
plt.figure(figsize=(10,6))
plt.bar(prot_count.index, prot_count.values)
plt.title('Distribution of Protocol Types')
plt.xlabel('Protocol Type')
plt.ylabel('Count')
plt.show()

#Histogram of Duration column
plt.figure(figsize=(10,6))
plt.hist(df['duration'], bins=50, edgecolor = 'k')
plt.title("Distribution of Connection Durations")
plt.xlabel("Duration")
plt.ylabel("Count")
plt.show()