# Python code to demonstrate string length
# using for loop

# Returns length of string
class LengthOfStr:  # created a class
    def findLen(self, str):  # created a function and passed arugument to it
        counter = 0  # created a variable and give value 0
        for i in str:  # iterating the argument
            counter += 1  # adding the iterated values to the created variable
        return counter  # returning that variable


a = LengthOfStr()  # calling the class
c = a.findLen("python")  # created a variable and giving values to the argument in the function
print("length", c)  # printing the variable to see the output
