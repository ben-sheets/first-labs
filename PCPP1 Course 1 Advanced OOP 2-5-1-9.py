#
#    Create a class representing a luxury watch;
#    The class should allow you to
#       hold a number of watches created
#       in the watches_created class variable.
#       The number could be fetched
#       using a class method named get_number_of_watches_created;
#           the class may allow you to
#               create a watch
#               with a dedicated engraving (text).
#       As this is an extra option,
#           the watch with the engraving should be created using an alternative constructor
#               (a class method),
#               as a regular __init__ method should not allow ordering engravings;
#    the regular __init__ method should only increase the value of the appropriate class variable;
#
#The text intended to be engraved should follow some restrictions:
#
#    it should not be longer than 40 characters;
#    it should consist of alphanumerical characters,
#        so no space characters are allowed;
#    if the text does not comply with restrictions,
#       an exception should be raised
#
#before engraving the desired text,
#   the text should be validated against restrictions using a dedicated static method.
#
#    Create a watch with no engraving
#    Create a watch with correct text for engraving
#    Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
#    After each watch is created, call class method to see if the counter variable was increased
#


###############################################
import math

#define base class of "Luxury_Watch"
class Luxury_Watch():
    __watches_created = 0

    def __init__(self):
        Luxury_Watch.__watches_created += 1

  
        
# alternate construcutor for watches with engravings
    @classmethod
    def with_engraving(cls, engraving):
        Luxury_Watch.__watches_created += 1





# make a dedicated static method to validate restrictions in engraving text
    @staticmethod
    def validate(engraving):
        try:
            math.sqrt(40 - (len(engraving)))
            
        except ValueError:
            print("Engraving too long - there's a 40 character limit")
            
        else:
            for ch in engraving:
                if ord(ch) >= 48 and ord(ch) <= 57:
                    pass
                elif ord(ch) >= 65 and ord(ch) <= 90:
                    pass
                elif ord(ch) >= 97 and ord(ch) <= 122:
                    pass
                else:
                    print("Engraving contains invalid characters.  Please use only letters and umbers, no spaces!")
        finally:
            pass 


# make a class method called "get_number_of_watches_created"
    @classmethod
    def get_number_of_watches_created(cls):
        return 'Number of watches created: {} '.format(cls.__watches_created)       

# command to create a watch w/o engraving
watch_without_engraving = Luxury_Watch()
print(Luxury_Watch.get_number_of_watches_created())

# command to create a watch with engraving
Luxury_Watch.validate("Motivation")
watch_with_valid_engraving = Luxury_Watch.with_engraving("Motivation")
print(Luxury_Watch.get_number_of_watches_created())

# command to try to create a watch with illegal engraving to trigger an exception
Luxury_Watch.validate("foo@baz")
watch_with_invalid_engraving = Luxury_Watch.with_engraving("foo@baz.com")
print(Luxury_Watch.get_number_of_watches_created())

