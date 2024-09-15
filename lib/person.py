#!/usr/bin/env python3

class Person:
    # Class body goes here

    #Instance method definition
    def talk(self):
        return("Hello World!")
        
    def walk(self):
       return("The person is walking.")
    
    pass
Job = Person()


print(Job.walk())
print(Job.talk())