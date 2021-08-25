"""def oldest(self,name,age):
    ansourted=age#value:14,15,12
    age.sort()#12,14,15
    for i in range(len(ansourted)):
        if age[-1]==ansourted[i]:
            x=i
    print(name[x]+" "+age[-1])
class Cat:
    def __init__(self, name=["kath","cath","kats"], age=[14,15,12]):
        self.name = name
        self.age = age
        oldest(self.name,self.age)

self.Cat__init__()"""

"""class dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def bark(self,dog_name):
        print(dog_name+" goes woof!")
    
    def jump(self,dog_name,dog_height):
        dog_height=dog_height*2
        print(dog_name+" jumps "+ str(dog_height)+" cm high!")
    
davids_dog=dog("rex",50)
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark("rex")
davids_dog.jump("rex",50)

sarahs_dog=dog("taecup", 20)
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark("teacup")
sarahs_dog.jump("teacup",20)

if davids_dog.height>sarahs_dog.height:
    print(davids_dog.name)
else:
    print(sarahs_dog.name)"""

"""class song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self,lyrics):
        for i in range(len(lyrics)):
            print(lyrics[i])
stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song(stairway.lyrics)"""

class zoo:
    def __init__(self,zoo_name):
       self.zoo_name=zoo_name
       self.animal=[]
       self.name=[]
       self.list2=[]
    def add_animal(self,new_animal):
        if new_animal not in self.animal:
            self.animal.append(new_animal)
    def get_animals(self):
        for i in range(len(self.animal)):
            print(self.animal[i])
    def sell_animal(self,animal_sold):
        if animal_sold in self.animal:
            for i in range(len(self.animal)):
                if animal_sold==self.animal[i]:
                    x=i
            self.animal.pop(x)
    def sort_animals(self):
        d={}
        for word in self.animal:
            d.setdefault(word[0],[]).append(word)
        self.list2=list(d.values())
        print(self.list2)
    def get_groups(self):
        for i in range(len(self.list2)):
            print(self.list2[i])
    
ramat_gan_safari=zoo("kaths")
ramat_gan_safari.add_animal("birds")
ramat_gan_safari.add_animal("barney")
ramat_gan_safari.add_animal("kath")
ramat_gan_safari.add_animal("dog")
ramat_gan_safari.add_animal("horse")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("kath")
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()





    








        

