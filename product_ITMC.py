print("\033[31m","Hello ITMC, my name is Tuan Hai, I'm looking forward to meet you soon")
print("\033[34m","This is a product which was made from python, everyone could enjoy it^^")
print("""Wellcome to my foodstall
This is my menu:
+Cheese_sausage: 50$
+Instant_noodle: 20$
+Spaghetti: 100$
+Caviar_shushi: 70$""")
Cheese_sausage = 50
Instant_noodle = 20
Spaghetti = 100
Caviar_shushi = 70
food = input("What do you like in the menu:")

if food == "Cheese_sausage":
  print("Is there anything else?")
  Answer = input("yes or no?: ")
  if Answer == "yes":
    print("Please choose one more dish: ")
    Food = input()
    if Food == "Instant_noodle":
      print("Your total bill is: ", Cheese_sausage*Instant_noodle,"$")
    elif Food == "Spaghetti":
      print("your total bill is:", Cheese_sausage*Spaghetti, "$")
    elif Food == "Caviar_shushi":
      print("your total bill is:", Cheese_sausage*Caviar_shushi, "$")
    else:
      print("I don't understand, can you order again please?")
  else:
    print("your bill is:", Cheese_sausage,"$")

    
elif food == "Instant_noodle":
  print("Is there anything else?")
  Answer = input("yes or no?: ")
  if Answer == "yes":
    print("Please choose one more dish: ")
    Food = input()
    if Food == "Cheese_sausage":
      print("Your total bill is: ", Cheese_sausage*Instant_noodle,"$")
    elif Food == "Spaghetti":
      print("your total bill is:", Instant_noodle*Spaghetti, "$")
    elif Food == "Caviar_shushi":
      print("your total bill is:", Instant_noodle*Caviar_shushi, "$")
    else:
      print("I don't understand, can you order again please?")
  else:
    print("your bill is:", Instant_noodle,"$")


elif food == "Spaghetti":
  print("Is there anything else?")
  Answer = input("yes or no?: ")
  if Answer == "yes":
    print("Please choose one more dish: ")
    Food = input()
    if Food == "Instant_noodle":
      print("Your total bill is: ", Spaghetti*Instant_noodle,"$")
    elif Food == "Cheese_sausage":
      print("your total bill is:", Cheese_sausage*Spaghetti, "$")
    elif Food == "Caviar_shushi":
      print("your total bill is:", Spaghetti*Caviar_shushi, "$")
    else:
      print("I don't understand, can you order again please?")
  else:
    print("your bill is:", Spaghetti,"$")


elif food == "Caviar_shushi":
  print("Is there anything else?")
  Answer = input("yes or no?: ")
  if Answer == "yes":
    print("Please choose one more dish: ")
    Food = input()
    if Food == "Instant_noodle":
      print("Your total bill is: ", Caviar_shushi*Instant_noodle,"$")
    elif Food == "Spaghetti":
      print("your total bill is:", Caviar_shushi*Spaghetti, "$")
    elif Food == "Cheese_sausage":
      print("your total bill is:", Cheese_sausage*Caviar_shushi, "$")
    else:
      print("I don't understand, can you order again please?")
  else:
    print("your bill is:", Caviar_shushi,"$")
else:
  print("My foodstall don't have that food, please order again!")
