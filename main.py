from allLSTs import allLSTs
import requests
import pandas as pd
import time

import utils


# Constants
SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'
CHECK_INTERVAL = 1  # Time (in seconds) between checks

def get_current_epoch():
    """Fetches the current epoch from Solana's RPC API."""
    try:
        response = requests.post(
            SOLANA_RPC_URL,
            json={
                "jsonrpc": "2.0",
                "id": 1,
                "method": "getEpochInfo"
            }
        )
        response.raise_for_status()
        data = response.json()
        return data['result']['epoch']
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def main():
    """Main loop to check for a new epoch."""
    current_epoch = get_current_epoch()
    if current_epoch is None:
        print("Failed to get current epoch.")
        return

    print(f"Current epoch: {current_epoch}")
    while True:
        time.sleep(CHECK_INTERVAL)
        new_epoch = get_current_epoch()
        if new_epoch is None:
            print("Failed to get current epoch.")
            continue

        if new_epoch != current_epoch:
            print(f"New epoch started! Old epoch: {current_epoch}, New epoch: {new_epoch}")
            current_epoch = new_epoch
        else:
            print(f"No new epoch. Current epoch: {current_epoch}")


if __name__ == "__main__":
    main()
