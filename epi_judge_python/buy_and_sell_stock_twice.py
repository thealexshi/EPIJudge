from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """
    Second buy must be after the first sale.

    max_profit = buy sell stock once 

    If you sell at i, the max profit you can get is (price[i] - min(prices[:i])) + (max_profit(prices[i+1:]))

    Can we calculate second half of equation and store in an array? 


    We can store results for max profit of selling at i once in an array in O(N)

    - First, calculate max_profit(prices[i+1:]) and store results in array. 
    - Then iterate through prices going forward and track the min and max

    [3, 4, 1, 5] -> 5

    """
    # profits[i] = max profit of buy sell once with prices from i (inclusive) to the end of the array
    # profits = [4,4,4,0]
    # highest = 5
    profits = [0] * (len(prices) + 1)
    highest = prices[-1]

    for i in reversed(range(len(prices) - 1)):
        profits[i] = max(profits[i + 1], highest - prices[i])
        highest = max(highest, prices[i])


    max_total_profit = profits[0]
    smallest = prices[0]
    for i in range(1, len(prices)):
        max_total_profit = max(max_total_profit, (prices[i] - smallest) + profits[i+1])
        smallest = min(smallest, prices[i])

    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
