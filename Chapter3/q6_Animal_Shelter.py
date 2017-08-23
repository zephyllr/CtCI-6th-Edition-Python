#!/usr/bin/python3

'''
Q3.6
    Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest"(based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
'''

class AnimalShelter():
    def __init__(self):
        self.dogs = []
        self.cats = []

    class Animal():
        def __init__(self, name, animalType, timestamp):
            self.name = name 
            self.animalType = animalType #cat or dog
            self.timestamp = timestamp

        def __repr__(self):
            return self.name + '-' + self.animalType + '-' + str(self.timestamp)

    def enqueue(self, name, animalType, timestamp):
        if animalType == "cat":
            self.cats.append( self.Animal(name, animalType, timestamp))
        elif animalType == "dog":
            self.dogs.append( self.Animal(name, animalType, timestamp))
        else:
            raise Exception('Animal type not supported in this shelter')

    def dequeueAny(self):
        if self.is_empty_dog() and self.is_empty_cat():
            raise Exception('No animals in shelter')
        elif self.is_empty_dog():
            return self.dequeueCat()
        elif self.is_empty_cat():
            return self.dequeueDog()
        elif self.peekDog().timestamp < self.peekCat().timestamp:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        if self.is_empty_dog():
            raise Exception('No dogs in shelter')
        return self.dogs.pop(0)

    def dequeueCat(self):
        if self.is_empty_cat():
            raise Exception('No cats in shelter')
        return self.cats.pop(0)

    def peekDog(self):
        if self.is_empty_dog():
            raise Exception('No dogs in shelter')
        return self.dogs[-1]

    def peekCat(self):
        if self.is_empty_cat():
            raise Exception('No cats in shelter')
        return self.cats[-1]

    def is_empty_dog(self):
        return len(self.dogs) == 0

    def is_empty_cat(self):
        return len(self.cats) == 0

def animal_shelter():
    names = ['Tsuki', 'Snek', 'Tnek', 'Fishy', 'Bunny', 'Nomnom']
    shelter = AnimalShelter()
    for i in range(len(names)):
        shelter.enqueue( names[i], getAnimalType(i), i)
    test(shelter)
    for i in range(2):
        print("Adopted Dog:", shelter.dequeueDog())
        test(shelter)
    for i in range(2):
        print("Adopted Cat:", shelter.dequeueCat())
        test(shelter)
    for i in range(2):
        print("Adopted Any:", shelter.dequeueAny())
        test(shelter)

def getAnimalType(i):
    if i % 2 == 0:
        return 'cat'
    else:
        return 'dog'

def test(shelter):
    print("Dogs:", shelter.dogs)
    print("Cats:", shelter.cats)
    print("-----------------------------------")

animal_shelter()
