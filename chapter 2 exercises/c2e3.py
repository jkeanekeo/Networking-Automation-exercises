'''
3. Create a list of five IP addresses. Print the initial list of addresses.
Use the .append() method to add an IP address onto the end of the list
Use the .extend() method to add two more IP addresses to the end of the list.
Use list concatenation to add two more IP addresses to the end of the list.
Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in 
the list.
Using the .pop() method to remove the first IP address in the list and the last IP address in the list.
Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

ip_list = ['1.1.1.1', '2.2.2.2', '3.3.3.3', '4.4.4.4', '5.5.5.5']
ip_list.append('192.168.1.1')
ip_list.extend(['192.168.1.2', '192.168.1.3'])

print (f"IP list:\n{ip_list}")
print (f"first IP add:\n{ip_list[0]}")
print (f"last IP add:\n{ip_list[-1]}")

ip_list.pop(0)
print (f"New first IP add:\n{ip_list[0]}")