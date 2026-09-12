############# Code from previous task ###################
#import copy


#warehouse = list()
#warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
#warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
#warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
#warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
#warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

#proposed_warehouse = copy.deepcopy(warehouse)

#print('Source list of candies')
#for item in warehouse:
#    print(item)

#print("**********************")


#print('Price proposal')
#for item in proposed_warehouse:
#    if item['weight'] > 300:
#        item['price'] = (item['price'] * .8)
#    print(item)


############ End code from previous task ############################


#Estimated time

#15 minutes
#Level of difficulty

#Medium
#Objectives

#    improving the student's skills in creating classes representing candies;
#    improving the student's skills in operating with deepcopy() and copy.

#Scenario

#The previous task was a very easy one. Now let's rework the code a bit:

#    1. introduce the Delicacy class to represent a generic delicacy.
#        The objects of this class will replace the old school dictionaries.
#        Suggested attribute names: name, price, weight;
#    2. your class should implement the __str__() method to represent each object state;
#    3. experiment with the copy.copy() and deepcopy.copy() methods
#        to see the difference in how each method copies objects


import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name}, {self.price}, {self.weight}"

    def proposed_pricing(self):
        if self.weight > 300:
            self.proposed_price = .8 * self.price
        return self.proposed_price

LolPop = Delicacy("Lolly Pop", .4, 133)
LicRish = Delicacy("Licorice", .1, 251)
Choc = Delicacy("Chocolate", 1, 601)
Sars = Delicacy("Sours", 0.01, 513)
Hcandi = Delicacy("Hard candies", 0.3, 433)


print('Source list of candies')
print(LolPop)
print(LicRish)
print(Choc)
print(Sars)
print(Hcandi)
print('')


print("Making Shallow Copies of Delicacies")
ShallowLolPop = copy.copy(LolPop)
ShallowLicRish = copy.copy(LicRish)
ShallowChoc = copy.copy(Choc)
ShallowSars = copy.copy(Sars)
ShallowHcandi = copy.copy(Hcandi)
print('')


print("Printing Shallow Copies")
print(ShallowLolPop)
print(ShallowLicRish)
print(ShallowChoc)
print(ShallowSars)
print(ShallowHcandi)
print('')


print("Making Deep Copies of Delicacies")
DeepLolPop = copy.deepcopy(LolPop)
DeepLicRish = copy.deepcopy(LicRish)
DeepChoc = copy.deepcopy(Choc)
DeepSars = copy.deepcopy(Sars)
DeepHcandi = copy.deepcopy(Hcandi)
print('')


print('Printing Deep Copies')
print(DeepLolPop)
print(DeepLicRish)
print(DeepChoc)
print(DeepSars)
print(DeepHcandi)
print('')


print("Calulating Proposed Prices")
print(LolPop)
print("Proposed price", LolPop.proposed_pricing)























