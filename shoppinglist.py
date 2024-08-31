shoppinglist= []


def show_menu():
  print("Welcome")
  print("Enter 1 to add items")
  print("Enter 2 to remove items")
  print("Enter 3 to view items")
  print("Enter 4 to see number of items")
  return input()
  



def add_item():
 print("Enter Item")
 newitem= input()
 shoppinglist.append(newitem)
 print(shoppinglist)
 if newitem in shoppinglist:
     print("You have already ordered " + str(newitem))



def remove_item():
  print("Enter Item")
  removeitem= input()
  shoppinglist.remove(str(removeitem))
  if removeitem not in shoppinglist:
   print("Sorry, you have not ordered this item")
  print(shoppinglist)  
  

def view_item():
     print(shoppinglist)

def count_item():
          manager = len(shoppinglist)
          print(manager)

def start_list():
    input = show_menu()
    
    if input == "1":
      add_item()
      start_list()
      
    elif input == "2":
     remove_item()
     start_list()
     
    elif input == "3":
     view_item()
     start_list()
     
    elif input == "4":
     count_item()
     start_list()
     
    else:
     print("Invalid request")
     

start_list()