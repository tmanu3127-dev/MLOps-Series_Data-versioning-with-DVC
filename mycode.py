import pandas as pd
import os

# Create a sample dataframe with column names:

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
        }

df = pd.DataFrame(data)


# Adding new row to df for v2  ;these we will perform after some time to prove
#  that what we changed will store in the dvc 
new_row_loc2 = {'Name': 'V2', 'Age': 20, 'City': 'Miami'}

df.loc[len(df.index)] = new_row_loc2

# Adding new row to df for v3
new_row_loc3 = {'Name': 'V3', 'Age': 30, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc3

# Ensure the data directory exsits at the root level of the project, if not create it:

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)


# Define the file path for the CSV file:
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the Dataframe to CSV file , including column names:

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")