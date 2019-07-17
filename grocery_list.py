
#Creating empty dictionary for item, list for grocery history, and setting stop to false for the while loop

grocery_item = {}
grocery_history = []
stop = False

#gathering information
while not stop:
  
  name = input("Item name:\n")
  quantity = input("Quantity purchased:\n")
  cost = input("Price per item:\n")
  grocery_item = {'name': name, 'quantity': int(quantity), 'cost': float(cost)}
  grocery_history.append(grocery_item)
  response = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

# 'q' will make stop True, exiting the loop  
  if response == 'q':
    stop = True
  else:
    stop = False
    
grand_total = 0

# # Taking the order information and updating the grocery_history dictionary. Used '%.2f' to get 2 point float
for item in grocery_history:
  
  item_total = item['quantity'] * item['cost']
  grand_total += item_total
  print("%d %s @ $%.2f ea $%.2f" %(item['quantity'], item['name'], item['cost'], item_total))
  item_total = 0
  
print("Grand Total: $%.2f" % grand_total)

