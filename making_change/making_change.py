#!/usr/bin/python

import sys

def making_change(amount, denominations):
  # base case
  if amount <=0:
    return 1
  #need to create a reference for all possible ways to make change
  #done at length of amount+1 since range indexes at 0 to start
  possibilities = [0 for x in range(amount+1)]
  # base case for how many ways there are for making change for 0
  possibilities[0] = 1
  # with base cases established, we will loop through each denomination
  for i in range(0, len(denominations)):
    # for every denomination as it loops, comparison will be made between that denomination and the initial amount
      for j in range(denominations[i], amount+1):
        #with every value in possibilities, there is an increment
        # each increment is added after the value of whatever denomination is taken away
        possibilities[j] += possibilities[j-denominations[i]]
  return possibilities[amount]

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")