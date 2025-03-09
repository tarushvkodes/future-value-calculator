import os
import pandas as pd
import numpy as np

def process_data_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            
            # Keep only location, year, and value columns
            df = df[['location', 'year', 'value']]
            
            # Calculate the mean for multiple data points per year
            df = df.groupby(['location', 'year']).mean().reset_index()
            
            # Extrapolate missing data points for years 2000-2023
            all_years = pd.DataFrame({'year': range(2000, 2024)})
            df = df.set_index('year').groupby('location').apply(lambda x: x.reindex(all_years['year']).interpolate(method='linear').ffill().bfill()).reset_index()
            
            # Save the processed data to new files
            output_filepath = os.path.join(directory, f"processed_{filename}")
            df.to_csv(output_filepath, index=False)

if __name__ == "__main__":
    directory = "data_files"  # Specify the directory containing the data files
    process_data_files(directory)
