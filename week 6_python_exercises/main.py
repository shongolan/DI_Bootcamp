list1 = [5, 10, 15, 20, 25, 50, 20]

list1[3]=200

print(list1)


aTuple = (10, 20, 30, 40)

a,b,c,d=aTuple

print(a)
print(b)
print(c)
print(d)

fruits = ['apple', 'banana', 'kiwi', 'pear']


for kathpangit in fruits:
  print(kathpangit)

cities = ["Tel Aviv", "San Francisco", "Paris", "Barcelona"]

for city in cities:
    print("I once went to", city)

numbers = range(4, 19)

for number in numbers:
  print(number)

number=input("enter number")

for i  in range(10):
    print(number * i)

current_number = 1 
while current_number <= 10:    
    print(current_number)   
    current_number += 1

active = True

while active: 
    city = input("Please enter the name of a city you have visited (enter 'quit' when you are finished): ")
    if city == 'quit':
        active = False
    elif city == 'leave me alone':
        active = False
    elif city == 'stop':
        active = False
    else:
        print("I'd love to go to", city)

print("Goodbye !")













