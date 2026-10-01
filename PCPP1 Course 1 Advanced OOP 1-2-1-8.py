#Estimated time
#
#20 minutes
#Level of difficulty


#Easy
#Objectives

#    creating classes, class and instance variables;
#    accessing class and instance variables;

#Scenario

#Imagine that you receive a task description of an application
#   that monitors the process of apple packaging before the apples are sent to a shop.

#A shop owner has asked for 1000 apples, but the total weight limitation cannot exceed 300 units.

#Write a code that creates objects representing apples as long as both limitations are met.
    #When any limitation is exceeded, than the packaging process is stopped,
    #and your application should print the number of apple class objects created, and the total weight.

#Your application should keep track of two parameters:

 #   the number of apples processed, stored as a class variable;
 #   the total weight of the apples processed; stored as a class variable.
     #Assume that each apple's weight is random, and can vary between 0.2 and 0.5 of an imaginary weight unit;

#Hint: Use a random.uniform(lower, upper) function to create a random number between the lower and upper float values.
import random


class appleOrder():

    
    def __init__(self, count, weight):
        applecount = 0
        appleweight = 0
        self.maxCount = count
        self.maxWeight = weight
        while (appleweight + .5) <= self.maxWeight:
            applecount += 1
            appleweight += random.uniform(.2, .5)
        print("Order complete! ", applecount, "apples weighing ", appleweight)



Order = appleOrder (1000, 300)

            
