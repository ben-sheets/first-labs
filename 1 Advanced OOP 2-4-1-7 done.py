#
#
#    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
#    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
#    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
#
#
#To print the current time, you could use the following code:
# import module responsible for time processing
#from datetime import datetime

# get current time using now() method
#timestamp = datetime.now()

# convert timestamp to human-readable string, following passed pattern:
#string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')

#print(string_timestamp)








###############################


from datetime import datetime


def timestamplogger(decorated_function):
    def internal_wrapper(*func_args):
        timestamp = datetime.now()
        string_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print(string_timestamp)
        return decorated_function(*func_args)
    return internal_wrapper


@timestamplogger
def addTheseNumbers(*args):
    print("This list of numbers", args, "adds up to: ", sum(args))


addTheseNumbers (1,3,5,7,11)
