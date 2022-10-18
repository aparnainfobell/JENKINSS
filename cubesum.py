# Simple Python program to find sum of series
# with cubes of first n natural numbers


# Returns the sum of series
class CubeSum:  # created a class
    def sumOfSeries(self, n):  # created a function a passing argument to it
        sum = 0  # creating a variable and passing value as zero
        for i in range(1, n + 1):  # iterating the argument
            sum += i * i * i  # multiplying each i

        return sum  # returning the variable


a = CubeSum()  # calling the function
c = a.sumOfSeries(5)  # giving value to the argument
print(c)  # printing the variable
