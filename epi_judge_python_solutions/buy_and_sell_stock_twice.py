from typing import List

from test_framework import generic_test


# def buy_and_sell_stock_twice(prices: List[float]) -> float:
#     min_price_so_far = prices[0]
#     max_first_profit = [0 for _ in prices]

#     # max 1st profit if sell on or before day i
#     for i in range(1, len(prices)):
#         min_price_so_far = min(prices[i], min_price_so_far)
#         max_first_profit[i] = max(max_first_profit[i-1], 
#                                   prices[i] - min_price_so_far)

#     # max second profit if buy on day i
#     max_second_profit = [0 for _ in prices]
#     for i in reversed(range(0, len(prices) - 1)):
#         next_day_diff = prices[i + 1] - prices[i]
#         max_second_profit[i] = max(next_day_diff,
#                                   next_day_diff + max_second_profit[i + 1])
    
#     return max([max_first_profit[i] + max_second_profit[i] for i in range(len(prices))])


def buy_and_sell_stock_twice(prices):
    min1 = min2 = float('inf')
    max1 = max2 = 0
    for price in prices:
         # max profit if making the first sale today
        max1 = max(max1, price - min1)  # current price - previous 1st sale min
        min1 = min(min1, price) # min price so far

        # max profit if making the second sale today
        max2 = max(max2, price - min2)  # current price - previous 2nd sale min
        min2 = min(min2, price - max1)

    return max2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
