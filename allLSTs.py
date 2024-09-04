import toml
import requests

# URL of the TOML file
url = "https://raw.githubusercontent.com/igneous-labs/sanctum-lst-list/master/sanctum-lst-list.toml"

# Fetch the content from the URL
response = requests.get(url)

# Parse the TOML content
data = toml.loads(response.text)
# Extract the symbol values from the sanctum_lst_list section
allLSTs = {entry['symbol']: entry['mint'] for entry in data.get('sanctum_lst_list', [])}
