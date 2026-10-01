#Create a class representing a time interval;
#the class should implement its own method for
    #addition, subtraction on time interval class objects;
#the class should implement
    # its own method for multiplication of time interval class objects by an integer-type value;
#the __init__ method
    #should be based on keywords to allow accurate and convenient object initialization
    #, but limit it to hours, minutes, and seconds parameters;
#the __str__ method
    #should return an HH:MM:SS string,
    #where HH represents hours,
    #MM represents minutes and
    #SS represents the seconds attributes of the time interval object;
#check the argument type,
    #and in case of a mismatch,
        #raise a TypeError exception.

#Hint 1
    #just before doing the math, convert each time interval to a corresponding number of seconds to simplify the algorithm;
    #for addition and subtraction, you can use one internal method, as subtraction is just ... negative addition.

#Test data:

#    the first time interval (fti) is hours=21, minutes=58, seconds=50
#    the second time interval (sti) is hours=1, minutes=45, seconds=22
#    the expected result of addition (fti + sti) is 23:44:12
#    the expected result of subtraction (fti - sti) is 20:13:28
#    the expected result of multiplication (fti * 2) is 43:57:40

#Hint 2:
    #you can use the assert statement to validate
        #if the output of the __str__ method applied to a time interval object equals the expected value.


# add on

#    Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
#    to add an integer to a time interval object means to add seconds;
#    to subtract an integer from a time interval object means to remove seconds.


#    in the case when a special method receives an integer type argument, instead of a time interval object, create a new time interval object based on the integer value.

#Test data:

#    the time interval (tti) is hours=21, minutes=58, seconds=50
#    the expected result of addition (tti + 62) is 21:59:52
#    the expected result of subtraction (tti - 62) is 21:57:48



import time
from datetime import timedelta

class timeIntervalsMath:

    def __init__(self, interval1, interval2):
        self.int1 = interval1
        self.int2 = interval2

    def addition = 
        

#    def addition(int1, int2)
        


fti = timedelta(hours = 21, minutes = 58, seconds = 50)
sti = timedelta(hours = 1, minutes = 45, seconds = 22)
print(fti)
print(sti)

