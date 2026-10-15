'''
Create a script that prompts for a data center location.

a. Use the .upper() method to convert the data center location to all upper case. Print this variable out.

b. Add extra whitespace to the end of your data center location (during the initial prompting for a data center location). Use the .strip() 
method to remove this extra whitespace. Use print(repr(my_var)) to view any extra whitespace before and after you remove it. In other words,
 'repr(my_var)' will allow you to see any whitespace (when you print this to standard output).

Chain the .upper() method and the .strip() method together such that these two operations occur on one line of code. 
Print this to standard output. Once again use print(repr(my_var)) so that you can see any whitespace.

Your output should look similar to the following:

$ python exercise2.py 

Enter data center location: san francisco  

Upper case:
SAN FRANCISCO  

Strip off whitespace:
Before: 'san francisco  '
After: 'san francisco'

Method chaining:
'SAN FRANCISCO'
'''

location = input("Enter data center location: ")

print()
print(f"Before: {repr(location)}")
print(f"Method Chaining: {location.upper().strip()}")
print()



