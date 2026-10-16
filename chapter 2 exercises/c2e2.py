'''2. Open the "show_version.txt" file for reading (do not use a context manager here). Use the .read() method to read the entire file contents to a variable named 'data'. Print out the first line of this "show version" output to the screen. Also print out the Python data type of this 'data' variable.

Close the file.

Open the file a second time this time using a Python context manager. Read in the file contents using the .readlines() method and 
save the content to a variable named 'data'. Once again, print out the first line of this "show version" output to the screen. 
Also print out the Python data type of this 'data' variable.
'''

with open("show_version.txt",) as data:
    data = data.readlines()

print(data[0])
print(type(data))
