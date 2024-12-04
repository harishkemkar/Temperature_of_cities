## https://api.weatherapi.com/v1/current.json?q=Pune&key=5a377f26b5bd43d298980919243011
## https://api.weatherapi.com/v1/current.json?q=London&key=5a377f26b5bd43d298980919243011

import requests
import pandas as pd
import openpyxl
import csv
import datetime

Path_input_file = 'D:\\Harish kemkar\\SRE\\Python  files\\File_Project'
input_file_name = 'Capital.txt'
input_file_full_path = Path_input_file + '\\' + input_file_name
print(input_file_full_path)

# Get the current timestamp
timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
# Define the file name with the timestamp
file_name = f"file_{timestamp}.csv"
print(file_name)

## To read the .txt file having city names
## file read and saved in list data type

with open(input_file_full_path,'r') as file:
    lines=file.readlines()


## run the api call for All city  names in list
api_key = '5a377f26b5bd43d298980919243011' # Replace with your actual API key
base_url = 'https://api.weatherapi.com/v1/current.json'
# city_name = input("Enter city Name for getting weather details ")

## Dataframe to hold output
Capital_temp_data = { 'Name': [],
                      'Region': [],
                      'lat': [],
                      'lon':[],
                      'tz_id':[],
                      'temp_c':[]
                      }

print(type(Capital_temp_data))
Capital_temp_data_df = pd.DataFrame(Capital_temp_data)
print(Capital_temp_data_df)

## working code
for capital in lines:
    api_url = f"{base_url}?q={capital}&key={api_key}"
    # print(api_url)
    # if city_name is None or city_name == "":
    #     print("city name is either None or empty")
    # else:
    #     print("city name is neither None or empty")
    ## Get weather data for given city name

    response = requests.get(api_url)
    data = response.json()

    # print(data)
    #
    # print(type(data))
    data1 = dict(data)

    # print(data1.keys())
    # print(data1.values())

    ## Below code gets Location details
    Current_location = dict(data1['location'])

    # print(Current_location)
    # print(type(Current_location))
    # print(Current_location.keys())
    # print(Current_location.values())

    ## Values to be captured
    # print(Current_location['name'])
    # print(Current_location['region'])
    # print(Current_location['country'])
    # print(Current_location['lat'])
    # print(Current_location['lon'])
    # print(Current_location['tz_id'])

    ## Below codes gets Temperature
    # print(data1['current'])

    current_temp = dict(data1['current'])

    # print(current_temp.keys())
    #
    # print(current_temp.values())

    # print(current_temp['temp_c'])
    record = [Current_location['name'],Current_location['region'],Current_location['country'],Current_location['lat'],Current_location['lon'],Current_location['tz_id'],current_temp['temp_c']]
    print(record)

    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the list as a row
        writer.writerow(record)
