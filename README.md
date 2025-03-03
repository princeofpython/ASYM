# Sanctum APIs in python
Python implementation of all important APIs of sanctum. (in `utils.py`)



## Automatic Solana staking yield maximization (ASYM)
Use `utils.py` to get your captial loss by swap via sanctum router. Also the APY increase, increase per epoch, and you can calculate the breakeven epochs.
View this [article](https://74944.substack.com/p/automatic-staking-yield-maximizing).

For calculating swap loss, output amount, APY gain, APY gain per epoch by converting 10.6233339301 hubSOL to rkSOL, use this.
````
getSwapLoss('hubSOL', 'rkSOL', int(10623339301), False)
````

For calculating swap loss, input amount, APY gain, APY gain per epoch by converting  hubSOL to 10.6233339301 rkSOL, use this. (exactOut)
````
getSwapLoss('hubSOL', 'rkSOL', int(10623339301), True)
````
