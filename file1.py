import pandas as pd
import os

folder = 'transactions-ser'

# Get a list of all the CSV files in the folder
csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
# Read the first CSV file
df = pd.read_csv(os.path.join(folder, csv_files[0]))

# Iterate through the remaining CSV files and merge them into the dataframe
for file in csv_files[1:]:
    df_temp = pd.read_csv(os.path.join(folder, file))
    df = df.append(df_temp, ignore_index=True)