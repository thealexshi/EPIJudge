from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    """
    Need to find biggest difference between a price and then highest price after.

    If you buy stock at index i, the max possible profit from that purchase is 
    (the highest value in prices[i+1:] - price[i]). 
    If you sell stock at index i, max profit is price[i] - min(prices[:i])

    Brute force: for every single price, calculate the max possible profit, return the max of those. O(N^2)

    Keep track of the min so far, max_profit, apply formula 2 in a single pass
    """

    min_ = prices[0]
    max_profit = 0

    for price in prices:
        max_profit = max(max_profit, price - min_)
        min_ = min(min_, price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
