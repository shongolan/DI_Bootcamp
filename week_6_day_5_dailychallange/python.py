def encypt_func(txt, s):  
    result = ""  
    for i in range(len(txt)):  
        char = txt[i]   
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)    
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result

def decypt_func(txt, s):  
    result = ""  
    for i in txt: 
        if i.isupper():
            c_unicode=ord(i)
            c_index=ord(i)-ord("A")
            newindex=(c_index-s)%26
            new_unicode=newindex+ord("A")
            new_charcter=chr(new_unicode)
            result=result+new_charcter
        else:
            result+=i
    return result  

print("choice action\na. encrypt\nb. decrypt")
choice=input("--> ")
if choice=="a":
    print("encrypt")
    message=input("enter the message: ")
    shift=int(input("enter the shift number: "))
    print("result\nPlain txt : " + message)  
    print("Shift pattern : " + str(shift))  
    print("Cipher: " + encypt_func(message, shift))  
elif choice=="b":
    print("decrypt")
    message=input("enter the message: ")
    shift=int(input("enter the shift number: "))
    print("result\nPlain txt : " + message)  
    print("Shift pattern : " + str(shift))  
    print("Cipher: " + decypt_func(message, shift))