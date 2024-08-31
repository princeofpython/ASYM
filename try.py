import requests
import pandas as pd

# Step 1: Make the request
url = "https://sanctum-extra-api.ngrok.dev/v1/infinity/allocation/current"
headers = {
    "accept": "application/json"
}

response = requests.get(url, headers=headers)
data = response.json()  # Assuming the response is JSON
# print(data) prints data in json format

# Step 2: Convert JSON to DataFrame
# If the JSON is a dictionary with nested lists, you might need to access specific keys
# and flatten the structure. For example:
# df = pd.DataFrame(data['key'])  # Replace 'key' with the appropriate key

df = pd.DataFrame(data)

pd.set_option('display.max_colwidth', None)  # Don't truncate column content
pd.set_option('display.max_columns', None)   # Display all columns

# Step 3: Display the DataFrame
#print(df.iloc[0])
print(df)