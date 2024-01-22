from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_ending_here = [0 for _ in prices]
    for day in range(1, len(prices)):
        max_ending_here[day] = max(max_ending_here[day - 1] + prices[day] - prices[day - 1],
                                   prices[day] - prices[day - 1])
    
    return max(max_ending_here)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
