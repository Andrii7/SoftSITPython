profitDict = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}

def profit(dataDict):
    return int(dataDict["sell_price"] * dataDict["inventory"] - dataDict["cost_price"] * dataDict["inventory"])



print(profit(profitDict))