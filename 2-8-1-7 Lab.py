#Estimated time
#45 minutes
#Level of difficulty Medium
#Objectives    improving the student's skills in operating with inheritance and composition
#Scenario
#
#Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.
#
#Your task is to :
#
#    define classes representing:
#        tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
#        engine; methods available: start(), stop(), get_state(); attribute available: fuel type
#        vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
#    based on the classes defined above, create the following objects:
#        two sets of tires: city tires (size: 15), off-road tires (size: 18)
#        two engines: electric engine, petrol engine
#    instantiate two objects representing cars:
#        the first one is a city car, built of an electric engine and city tires
#        the second one is an all-terrain car build of a petrol engine and off-road tires
#    play with the cars by calling methods responsible for interaction with components.


#######################################################################################################
        
      
class Tires:
    def __init__(self, size):
        self.pressure = 0
        self.size = size

    def get_pressure(self):
        print("Tire pressure is:", self.pressure, "psi.")

    def pump(self, psi):
        self.pressure = psi
        print("Pumping tire to", self.pressure, "psi.")


class City_Tires(Tires):
    def __init__(self):
        super().__init__("15")


class Off_Road_Tires(Tires):
    def __init__(self):
        super().__init__("18")
    

class Engine:
    def __init__(self, fuel_type):
        self.state = "off"
        self.type = fuel_type

    def start(self):
        self.state = "running"
        
    def stop(self):
        self.state = "off"
        
    def get_state(self):
        print("Engine is: ", self.state)


class Electric_Engine(Engine):
    def __init__(self):
        super().__init__("electric")


class Petrol_Engine(Engine):
    def __init__(self):
        super().__init__("petrol")


class Vehicle():
    def __init__(self, VIN, Engine, Tires):
        self.VIN = VIN
        self.engine = Engine
        self.tires = Tires

  
       

city_car = Vehicle(987, Electric_Engine(), City_Tires())
all_terrain_car = Vehicle(345, Petrol_Engine(), Off_Road_Tires())

print("City car tests...")
city_car.tires.get_pressure()
city_car.tires.pump(35)
city_car.tires.get_pressure()
city_car.engine.get_state()
city_car.engine.start()
city_car.engine.get_state()
city_car.engine.stop()
city_car.engine.get_state()

print("All terrain car tests...")
all_terrain_car.tires.get_pressure()
all_terrain_car.tires.pump(35)
all_terrain_car.tires.get_pressure()
all_terrain_car.engine.get_state()
all_terrain_car.engine.start()
all_terrain_car.engine.get_state()
all_terrain_car.engine.stop()
all_terrain_car.engine.get_state()
print("~fin~")
