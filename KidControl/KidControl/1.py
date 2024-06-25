import pandas as pd
import json

# Load the CSV file
file_path = 'C:\Users\MyPC\Downloads\iPhone-Thing-Gps (1).csv'  # Adjust the path to the uploaded file
df = pd.read_csv(file_path)

# Initialize empty lists for time, lat, and lon
time_list = []
lat_list = []
lon_list = []

# Iterate over the DataFrame and extract values
for index, row in df.iterrows():
    time_list.append(row['time'])
    
    # Parse the JSON-like string in the 'value' column
    value_dict = json.loads(row['value'].replace("'", "\""))  # Convert single quotes to double quotes for JSON parsing
    lat_list.append(value_dict['lat'])
    lon_list.append(value_dict['lon'])

# Output the arrays
print("Time Array:", time_list)
print("Latitude Array:", lat_list)
print("Longitude Array:", lon_list)
