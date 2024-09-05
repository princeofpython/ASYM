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


"""
['fpSOL', 'wifSOL', 'pathSOL', 'JupSOL', 'juicingJupSOL', 'phaseSOL', 'banxSOL', 'iceSOL', 'fmSOL', 'BurnSOL', 'mallowSOL', 
'pineSOL', 'uwuSOL', 'uptSOL', 'pwrSOL', 'superSOL', 'jucySOL', 'bonkSOL', 'dSOL', 'compassSOL', 'picoSOL', 'clockSOL', 'hubSOL', 
'strongSOL', 'lanternSOL', 'stakeSOL', 'pumpkinSOL', 'hSOL', 'lifSOL', 'cgntSOL', 'laineSOL', 'vSOL', 'bSOL', 'daoSOL', 'JitoSOL', 
'JSOL', 'LST', 'zippySOL', 'edgeSOL', 'elSOL', 'aeroSOL', 'thugSOL', 'wenSOL', 'camaoSOL', 'dainSOL', 'digitSOL', 'digitalSOL', 
'dlgtSOL', 'dualSOL', 'haSOL', 'hausSOL', 'kumaSOL', 'nordSOL', 'polarSOL', 'rkSOL', 'rSOL', 'spikySOL', 'stakrSOL', 'xSOL', 
'fuseSOL', 'mangoSOL', 'apySOL', 'stepSOL', 'uSOL', 'lotusSOL', 'eonSOL', 'gS', 'bbSOL', 'SOL', 'INF', 'stSOL', 'mSOL']
"""
