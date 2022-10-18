# Python program to convert a list to string

class LtoS:#created a class
    def listToString(self,s):#created a function and passing an argument
        # initialize an empty string
        str1 = ""

        # traverse in the string
        for i in s:
            str1 += i

        # return string
        return str1

a = LtoS() #calling the class
c = a.listToString(['python', 'program', 'practise'])#passing values to the argument in the function
print(c)#printing the variable to see the output


