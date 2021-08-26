#1
print("Hello World\n"*4)

#2
print((99*99*99)*8)

#3 skipped

#4
computer_brand = "Toshiba"
print("I have a " + computer_brand + " computer.")

#5
name = "shon"
age = 28
shoe_size = 9
info = "Hi I am " + name + ". I am " + str(age) + " years old and my shoe size is " + str(shoe_size) 
print(info)

#6
a = 3
b = 2
if a > b:
 print("Hello World")

#7
num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print(str(num) + " is Even number")  
else:  
   print(str(num) + " is Odd number") 

   #8
user_name = input("What is your name: ")
if user_name == "Shon" or user_name == "shon":
 print("Ohh wow we have tha same name!")
else:
 print("Your name " + user_name + " is like a clown its so funny.")

#9
height = int(input("Enter your height in inches: "))
if height > 145:
 print("You are tall enough to ride.")
else:
 print("You need to grow some more to ride.")