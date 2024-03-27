def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    maxi = 0
    for i in range(len(prices)-1):
        m = max(prices[i+1:]) - prices[i]
        maxi = max(maxi, m)
    return maxi
    pass
