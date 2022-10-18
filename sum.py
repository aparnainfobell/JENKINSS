# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum

class SumOfDict:  # created a class and named it to SumOfDict
    def returnSum(mydict):  # created a function and pass an argument

        lst = []  # an empty list is created to add the values
        for i in mydict:  # iterating the argument with for loop
            lst.append(mydict[i])  # appending the iterated values of that argument in to the empty list
        final = sum(
            lst)  # using the inbuilt function sum for finding the sum of values of that list and passing it in to a variable
        return final  # returning that variable

a = SumOfDict #calling the class
c = a.returnSum({'a': 100, 'b': 200, 'c': 300})#passing values to the arguments in the function and assigning it in to a variable
print(c) #printing the variable to view the output


