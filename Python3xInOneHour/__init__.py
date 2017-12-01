/* Version of Python used - Python 3.x 
The code at the end is optimized to run on Python SDK 3.x */

import sys
import random
import os

class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, weight, height, sound):
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__sound = sound


    def set_name(self, name):
        self.__name = name

    def set_weight(self, weight):
        self.__weight = weight

    def set_height(self, height):
        self.__height = height

    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} weighs {} kg and is {} cm tall and says {}".format(self.__name, self.__weight, self.__height, self.__sound)

Cat = Animal('Whiskers', 10, 33, 'Meow')
print(Cat.toString())

class Dog(Animal):
    __owner =  ""

    def __init__(self, name, weight, height, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, weight, height, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} weighs {} kg and is {} cm tall and says {}. His owner is {}".format(self.get_name(), self.get_weight(), self.get_height(), self.get_sound(), self.get_owner())

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

whoof = Dog("Whoofy", 15, 23, "Whoof", "Roger")
print(whoof.toString())
