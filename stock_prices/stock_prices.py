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

      if prices[j] > prices[i]:
        # Go through find the largest
        largest = j

        print(f"this should be largest {prices[largest]}")
  print(current_min_price_so_far)
  print(largest)

      
  # If the smallest(5) comes before the largest(11)
  if current_min_price_so_far < largest:
    # Subtract smallest(5) from largest(11) that will be max profit(6)
    max_profit = prices[largest] - prices[current_min_price_so_far]
    return max_profit
  # If the largest(100) comes before the smallest(10)
  if current_min_price_so_far > largest:
    print("this should print")
    #find the second largest(90).. that will be max you can make
    for i in range(prices[largest] + 1, len(prices)):
      print(f"trying to find second largest {prices[i]}") 
    #Subtract largest(100) from second largest(90) this will be max profit (-10)


list_1 = [10, 7, 5, 8, 11, 9]
list_2 = [100, 90, 80, 50, 20, 10]
find_max_profit(list_2)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))