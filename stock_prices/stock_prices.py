#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Go through the list and find the smallest 
  # This will be `current_min_price_so_far`
  # Go through the list and find the largest
  # If the smallest(5) comes before the largest(11)
    # Subtract smallest(5) from largest(11) that will be max profit(6)

  # If the largest(100) comes before the smallest(10)
    #find the second largest(90).. that will be max you can make 
    #Subtract largest(100) from second largest(90) this will be max profit (-10)


  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))