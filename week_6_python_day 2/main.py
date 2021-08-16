string=input("enter a word: ")
if len(string)<10:
    print("string not long enough")
if len(string)>10:
    print("string too long")
print(string[0])
print(string[-1])
word=[]
for i in range(len(string)):
    word.append(string[i])
print(word)
e=""
for i in range(len(word)):
    e+=word[i]
    print(e)
