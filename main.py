program_loop = True

name = input("What is your name? ")
print("Nice to meet you, " + name)
age = input("What is your age? ")
print(age + (" year old ") + name + " welcome! How can I help you!")

def display_menu():
  print("Select from the following")  
  print("1. Place Holder 1 ") 
  print("2. Place Holder 2 ")   
  print("3. Place Holder 3 ")  
  print("4. Place Holder 4 ")  
  print("5. Exit ")  



  #used to capture and process user selections
def user_selection():
    in_use =True
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:  
      choice_1()  
    elif user_choice == 2:  
      choice_2()
    elif user_choice == 3:  
      choice_3() 
    elif user_choice == 4:  
      choice_4() 
    elif user_choice == 5:  
        print( name + " ,Thank you for using the program! Please come back again!")
        in_use = False
    else:
      print("\nSorry, That is an invalid choice. Please try again!")
      return in_use


def choice_1():
  print("option 1")
  display_menu()
  program_loop =user_selection()

def choice_2():
  print("option 2")
  display_menu()
  program_loop =user_selection()
  


def choice_3():
  print("option 3")
  display_menu()
  program_loop =user_selection()

def choice_4():
  print("option 4")
  display_menu()
  program_loop =user_selection()
  
  
while program_loop:
  display_menu()
  program_loop =user_selection()  
             



