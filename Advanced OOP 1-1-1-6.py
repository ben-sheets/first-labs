#Scenario
#
#
#        __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
#        turn_on() should return the message 'mobile phone {number} is turned on'.
#           Curly brackets are used to mark the place to insert the object's number variable;
#        turn_off() should return the message 'mobile phone is turned off';
#        call(number) should return the message 'calling {number}'.
#           Curly brackets are used to mark the place to insert the object's number variable;
#    create two objects representing two different mobile phones;
#        assign any random phone numbers to them;
#    implement a sequence of method calls on the objects to
#        turn them on,
#        call any number.
#        Print the methods' outcomes;
#    turn off both mobiles.
#
#Example output
#mobile phone 01632-960004 is turned on
#mobile phone 01632-960012 is turned on
#calling 555-34343
#mobile phone is turned off
#mobile phone is turned off


class mobile_phone:
    def __init__ (self, number):
        self.number = number

    def turn_on():
        return print("Mobile phone {number} is turned on.")

    def call(target):
        print("Mobile phone with number ", number, " calling ", target)

    def turn_off(number):
        return print("Mobile phone with number ", number, " is powered off.")

mobile04 = mobile_phone("01632-960004")
mobile12 = mobile_phone("01632-960012")

mobile04.turn_on
mobile12.turn_on

#mobile04.call("555-34343")
#mobile12.call("555-34343")

mobile04.turn_off
mobile12.turn_off
