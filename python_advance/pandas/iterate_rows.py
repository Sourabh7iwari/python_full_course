import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']}

df = pd. DataFrame(data)

# Iterating over rows using iterrows()
for index, row in df. iterrows( ):
    print(f" Index: {index}, Data: {row.to_dict()} ",  )