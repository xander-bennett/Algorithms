#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # create base case
  profit = float('-inf')
  for i in range(len(prices) - 1):  #the range is all but the last one because you can't buy and sell on the same day
    # establish any of the elements to act as the buy. The remaining elements are compared as sells
    buy_order = prices[i]
    for j in prices[i+1:]:
      sell_order = j
      net = (sell_order - buy_order)
      if net > profit:
        profit = net
  return profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))