#!/usr/bin/python

import argparse
# Everything inside () is just an example
def find_max_profit(prices):
  # This will be `current_min_price_so_far`
  for i in range(0, len(prices)):
    current_min_price_so_far = i
    print(f"outer {prices[current_min_price_so_far]}")
    
    for j in range(0, len(prices)):
      current  = j

      if prices[j] < prices[current_min_price_so_far]:
        # Go through find the smallest 
        current_min_price_so_far = j
        print(f"this should be smallest {prices[current_min_price_so_far]}")

        # loop through everything to the right of the current_min_price_so_far
        for k in range(prices[current_min_price_so_far] + 1, len(prices)):
          print(prices[k])
        # find max_profit_so_far
        # return difference of current_min_price_so_far from max_profit_so_far



list_1 = [10, 7, 5, 8, 11, 9]
list_2 = [100, 90, 80, 50, 20, 10]
find_max_profit(list_2)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))