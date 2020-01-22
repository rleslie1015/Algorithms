# I'm probably way overthinking this but I am stuck trying to loop through the prices and find the second largest sum.
# I've already looped through and found the smallest and largest prices
# BUT in the case the largest comes before the smallest I want to find the second largest in order to subtract that from the largest and find max profit

# Everything inside () is just an example price
def find_max_profit(prices):
  # This will be `current_min_price_so_far`
  for i in range(0, len(prices)):
    current_min_price_so_far = i
   
    for j in range(0, len(prices)):
      current  = j

      if prices[j] < prices[current_min_price_so_far]:
        # Go through find the smallest 
        current_min_price_so_far = j

      if prices[j] > prices[i]:
        # Go through find the largest
        largest = j
  # If the smallest(5) comes before the largest(11)
  if current_min_price_so_far < largest:
    # Subtract smallest(5) from largest(11) that will be max profit(6)
    max_profit = prices[largest] - prices[current_min_price_so_far]
    return max_profit
  # If the largest(100) comes before the smallest(10)

  if current_min_price_so_far > largest:
    #find the second largest(90).. that will be max you can make 
    for i in range(prices[largest] + 1, len(prices)):
      print(f"trying to find second largest {prices[i]}") 
    #Subtract largest(100) from second largest(90) this will be max profit (-10)

