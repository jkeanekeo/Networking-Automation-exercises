'''
3.   Use the split() method to extract the serial number from the following string. This output line is
 based upon the "show version" output from a Cisco IOS-XE device.

line = "Processor board ID FAL127990LA"
Note, the split() method will divide the string base upon consecutive whitespace. Consequently, executing .split() on 
the above 'line' variable will return four strings. For example,

# Use Python unpacking to immediately assign .split() output to four-different variables.
var1, var2, var3, var4 = line.split()
Alternatively, you can assign line.split() to a single variable. In this case a list will be returned.

# Return a list
words = line.split()
serial_number would be the fourth element in the returned list so it would be words[3]. We will cover lists in lesson2.
'''

line = "Processor board ID FAL127990LA"
var1, var2, var3, var4 = line.split()

print()
print (f"{var1, var2, var3, var4}")
print()