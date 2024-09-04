import requests
import pandas as pd
from allLSTs import allLSTs
import json

"""
    APYs for the specified tokens since their respective inceptions. Takes a list of LSTs (strings) as input, Returns a pandas dataframe.
"""
def getInceptionAPY(LSTs):
    url = "https://sanctum-extra-api.ngrok.dev/v1/apy/inception?" 
    
    for lst in LSTs:
        url += "lst=" + lst + '&'

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON


    df = pd.DataFrame(data)

    return df

"""
    Latest known APYs for the specified LSTs. Calculation method:
        Calculate per-epoch APY of 6 epochs ago up till last completed epoch (5 epochs total)
        Remove smallest and largest outliers
        Return average of the remaining 3 per-epoch APYs

    If data for LST is incomplete, this falls back to APY since inception.
    Takes a list of LSTs (strings) as input, Returns a pandas dataframe.
"""
def getLatestAPY(LSTs):
    url = "https://sanctum-extra-api.ngrok.dev/v1/apy/latest?" 
    
    for lst in LSTs:
        url += "lst=" + lst + '&'

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON


    df = pd.DataFrame(data)

    return df

"""
    APYs for the specified tokens counting from {epochs + 1} epochs ago till last epoch.
    Takes a list of LSTs (strings), epochs (int) as input, Returns a pandas dataframe.
"""
def getPastEpochsAPY(LSTs, epochs):
    url = "https://sanctum-extra-api.ngrok.dev/v1/apy/past-epochs/" + str(epochs) + "?" 
    
    for lst in LSTs:
        url += "lst=" + lst + '&'

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON


    df = pd.DataFrame(data)

    return df

"""
    The current LST allocations for the Infinity pool.
    This endpoint is only updated every 5 minutes
"""
def getInfinityAllocation():
    url = "https://sanctum-extra-api.ngrok.dev/v1/infinity/allocation/current"

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON

    df = pd.DataFrame(data)

    return df

"""
    Current SOL value for the specified tokens in lamport terms for 1.0 of the token.
    If the stake pool has not been updated for this epoch, returns last epoch's value
"""
def getSolValue(LSTs):
    url = "https://sanctum-extra-api.ngrok.dev/v1/sol-value/current?" 
    
    for lst in LSTs:
        url += "lst=" + lst + '&'

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON


    df = pd.DataFrame(data)

    return df

"""
    Current TVLs for the specified tokens in lamport terms.
"""
def getTVL(LSTs):
    url = "https://sanctum-extra-api.ngrok.dev/v1/tvl/current?" 
    
    for lst in LSTs:
        url += "lst=" + lst + '&'

    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON


    df = pd.DataFrame(data)

    return df

"""
Get a SOL value for LSTs
"""

def getLSTPrice(LSTs):
    url = "https://sanctum-s-api.fly.dev/v1/price?"
    for lst in LSTs:
        url += "input=" + allLSTs[lst] + '&'
    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON

    df = pd.DataFrame(data['prices']).drop('mint', axis = 1)
    df.index = LSTs
    return df


def getSwapQuote(inLST, outLST, amount, bExactOut):
    url = "https://sanctum-s-api.fly.dev/v1/swap/quote?"
    url += "input=" + allLSTs[inLST]
    url += "&outputLstMint=" + allLSTs[outLST]
    url += "&amount=" + str(amount)
    url += "&mode=" + ("ExactOut" if bExactOut else "ExactIn")
    headers = {
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    data = response.json()  # Assuming the response is JSON

    return data
