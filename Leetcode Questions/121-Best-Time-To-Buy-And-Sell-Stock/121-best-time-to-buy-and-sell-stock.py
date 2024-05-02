'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for x in prices:
        min_price = min(x, min_price)
        max_profit = max(x - min_price, max_profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))