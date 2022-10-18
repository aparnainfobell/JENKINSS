# Python program to find the
# maximum of two numbers

class MaxOfTwo:  # created a class MaxOfTwo
    def maximum(self, a, b):  # created a function and passing arguments to it
        if a >= b:  # condition to check which argument is working
            return a  # if the above condition satisfies return that argument
        else:
            return b  # if the above condition not satisfied then return the next argument


k = MaxOfTwo()  # calling the class
c = k.maximum(4, 9)  # going in to the function and passing values for the arguments and assigning it in to a variable
print("mamimum is", c)  # printing that variable to view the output

# # Driver code
# a = 2
# b = 4
# print(maximum(a, b))
