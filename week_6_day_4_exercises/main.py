my_fav_numbers=set()
my_fav_numbers.add(4)
my_fav_numbers.add(6)
my_fav_numbers.remove(6)
print(my_fav_numbers)
friend_fav_numbers=set()
friend_fav_numbers.add(20)
friend_fav_numbers.add(30)
our_fav_numbers=set.union(my_fav_numbers,friend_fav_numbers)
print(our_fav_numbers)

#2

# my_tuple = (5,6,7)
# new_tuple=list(my_tuple)
# new_tuple.append(8)
# my_tuple=tuple(new_tuple)
# print(my_tuple)

# #3
# for i in range(20):
#     print(i+1)

# #4
# number=1.5
# list1=[]
# for i in range(8):
#     list1.append(number)
#     number+=.5
# print(list1)

# #5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(2)
# basket.append("kiwi")
# basket.insert(0, "Apples")
# count=0
# for i in range(len(basket)):
#     if basket[i]=="Apples":
#         count+=1
# basket=[]
# print(basket)

# #6
# name="kath"
# while True:
#     ussername=input("enter your name: ")
#     if ussername==name:
#         break
# #7
# items=[1,2,3,4,5,6]
# for i in range(len(items)):
#     if (i %2)==0:
#         print(items[i])
# #8
# nl=[]
# for x in range(1500, 2501):
#     if (x%5==0) and (x%7==0):
#         nl.append(str(x))
# print (','.join(nl))

# #9
# fav=input("enter your favorit fruits separated by space: ")
# fruits=[]
# fruits=list(fav.split(" "))
# nameOfFruits=input("enter any fruit: ")
# if nameOfFruits in fruits:
#     print("you choice one of your favorit fruits! enjoy")
# else:
#     print("you choice a new fruit i hope you enjoys")

# #10

# toppings=[]
# price=10
# while True:
#     customerTopping=input("enter toopings that you want type quit to stop: ")
#     if customerTopping=="quit":
#         break
#     else:
#         price+=2.5
#         toppings.append(customerTopping)
#         print("adding the topping to your pizza")
# for i in toppings:
#     print(i)
# print("your total price is: "+str(price))

#11

# totalprice=0
# for i in range(4):
#     age=int(input("enter your age: "))
#     if age<3:
#         print("ticket is free")
#     elif age>=3 and age<=12:
#         print("ticket is 10$")
#         totalprice+=10
#     elif age>12:
#         print("ticket is 15$")
#         totalprice+=15
# print("the total cost of your tickets is $"+str(totalprice))
# allowed=[]
# notallowed=[]
# for i in range(4):
#     ussername=input("enter your name: ")
#     usserage=int(input("enter your age: "))
#     if usserage>=16 and usserage <=21:
#         notallowed.append(ussername)
#     else:
#         allowed.append(ussername)
# for i in range(len(allowed)):
#     print(allowed[i])


#12
# names = ['Mark', 'Ben', 'simon']
# namesdel = []
# for i in range(len(names)):
#  print("What is your age " + names[i])
#  age = int(input("age: "))
#  if age > 16:
#   namesdel.append(names[i])

# print(namesdel)

#13 and 14
# print("deli has out of pastrami sandwich")
# sandwich_orders=["tuna sandwhich","avocado sandwhich","egg sandwich","kath sandwhich","pastrami sandwhich","pastrami sandwhich","pastrami sandwhich"]
# while True:
#  if "pastrami sandwhich" in sandwich_orders:
#   sandwich_orders.remove("pastrami sandwhich")
#  else:
#   break
# finished_sandwiches=[]
# finished_sandwiches=sandwich_orders
# for i in range(len(finished_sandwiches)):
#     print("i made your "+ finished_sandwiches[i])















