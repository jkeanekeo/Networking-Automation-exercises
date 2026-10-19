'''
4. Using a context manager, open the file named "show_arp.txt". Read the contents of this file in 
(using the f.readlines() method) and save the file contents to a variable named 'show_arp'.
Print out the Python data type of 'show_arp' variable.
Print out the length of the 'show_arp' variable.
Print out the header line from the 'show_arp' variable.
Print out both the first and the last line of the tabular data from the 'show_arp' variable.
Split the header line into fields using the .split() method. Save this into a variable named fields. 
Print out this 'fields' variable.
Print out the Python data type of this 'fields' variable.
Print out the current number of entries in the 'fields' variable.
Print out the first field and the last field.

If you print out the fields variable you will observe that some fields are unneeded or incorrect 
(due to the splitting on whitespace).

For example, there are fields containing 'Age' and '(min)', but that is only one column in the tabular output. 
Similarly, 'Hardware' and 'Addr' were split into two fields, but there is only one corresponding column in the table output.

Consequently, you should delete the field containing '(min)' from the list. Similarly, you 
should combine the 'Hardware' and 'Addr' entries into a single field named 'Hardware_Addr'. 
At the end of your modifications, you should only see the following six fields in the 'fields' variable.
['Protocol', 'Address', 'Age', 'Hardware_Addr', 'Type', 'Interface']
Finally, print out the fields variable after you have made the above corrections.'''

#reading the txt file
with open ("show_arp.txt",) as show_arp:
    show_arp = show_arp.readlines()

#print first and second line of txt file
print("file type:",type(show_arp))
print("length of file: ",len(show_arp))
print(show_arp[0].strip())
print(show_arp[1].strip())
print(f"{show_arp[-1] }\n")

#split the header into fields variable
fields = (show_arp[0].split())
print(f"Fields: {fields}")
print(f"file type: ",type(fields))
print(fields[0])
print (fields[-1])

fields.remove("(min)")
hardware_index = fields.index("Hardware")
fields[hardware_index] = "Hardware_Addr"
del fields[hardware_index + 1]

print(fields)