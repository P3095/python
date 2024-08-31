shoppinglist= []
user_choice= 0

def show_menu():
  print("Welcome")
  print("Enter 1 to add items")
  print("Enter 2 to remove items")
  print("Enter 3 to view items")
  print("Enter 4 to see number of items")
  useranswer = input()
  print ("You chose " + str(useranswer))



def add_item():
 print("Enter Item")
 newitem= input()
 shoppinglist.append(str(newitem))
 print(shoppinglist)


def remove_item():
  print("Enter Item")
removeitem= input()
shoppinglist.remove(str(removeitem))
print(shoppinglist)  


def view_item():
     print(shoppinglist)

def count_item():
          manager = len(shoppinglist)
          print(manager)

def start_list():
 show_menu()
if user_choice == 1:
  add_item()
  show_menu()

elif user_choice == 2:
  remove_item()
  show_menu()

elif user_choice == 3:
  view_item()
  show_menu()

elif user_choice == 4:
  count_item()
  show_menu()

else:
   print("Invalid reuest")
start_list()