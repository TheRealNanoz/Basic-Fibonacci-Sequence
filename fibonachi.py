from time import sleep

class sequence: #create sequence
    def __init__(self, max): #initialise class with the attribute: max
        self.max = max
    def sleepTrue(self, max): #define function for returning fibonacci sequence with a delay of 0.1s between results
        max = self.max # retrieve the value stored in max
        current = 0 # set the current to 0
        print(current) # print 0 as first value of sequence
        previous = current # set the previous value
        current = current + 1 # set the next value as the current + 1
        while current < max: # makes sure we do not go over the maximum value
            sleep(0.1)
            print(current) #prints the value in current
            current = current + previous # updates current value to the sum of current + previous
            previous = current # takes current value as previous
        return current # returns the current value once the loop is exited

    def sleepFalse(self, max):
        max = self.max # retrieve the value stored in max
        current = 0 # set the current to 0
        print(current) # print 0 as first value of sequence
        previous = current # set the previous value
        current = current + 1 # set the next value as the current + 1
        while current < max: # makes sure we do not go over the maximum value
            print(current) #prints the value in current
            current = current + previous # updates current value to the sum of current + previous
            previous = current # takes current value as previous
        return current # returns the current value once the loop is exited


start = 0
previous = start #initiate previous value as 0
max = 0
while True:
    max = int(input("What is the maximum value of the sequence (0 is infinite until terminated): "))
    if max > 0:
        break
    elif max == 0:
        max = float('inf')
        break
    else:
        print("Cannot have a negative number as maximum. must be 0+")
while True:
    slowed = bool(input("Do you wish for the program to be slowed (1 = True, 0 = False): "))
    if (slowed == True) or (slowed == False):
        break
    else:
        print("You must only input a 0 or 1!")
print(max)
fibonacci = sequence(max)
if slowed == True:
    max = max
    final_value = fibonacci.sleepTrue(max)
    print(f"The final value after max in the sequence is: {final_value}")
if slowed == False:
    max = max
    final_value = fibonacci.sleepFalse(max)
    print(f"The final value after max in the sequence is: {final_value}")
