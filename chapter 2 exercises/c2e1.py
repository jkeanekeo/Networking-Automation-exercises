'''1.  Create a base address variable of "192.168.254.". Prompt a user to enter a subnet prefix 
length from between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet 
(the number of total IP addresses in the subnet). Once we know the subnet size, we can calculate 
the number of hosts allowed in the subnet (subtract off the network number and broadcast address).

Also calculate and print out the network number for the first two subnets using the base address specified above.

Your program should print out the following:
The number of hosts in the subnet.
The network number of the first two subnets.
Both the first and last host address in the first subnet.

'''
baseIP = "192.168.254."

while True:
    p = input("Enter a netmask length between 25 to 30:")

    if p.isdigit():
        p = int(p)

        if 25 <= p <= 30:
            break
    print ("Invalid network mask, please enter network mask /25 to /30") 

subnetsizebin = 32 - p
subnethosts = 2**subnetsizebin
losthosts = 2 #network and broadcast IP
numberusablehosts = subnethosts - losthosts
firstusablehosts = f"{baseIP}1"
lastusablehosts = f"{baseIP}{numberusablehosts}"
networkone = f"{baseIP}0" 
networktwo = f"{baseIP}{subnethosts}" 


print (f"Number of hosts available:{numberusablehosts}\n")
print(f"Subnets:\n{networkone}\n{networktwo}\n")
print(f"Host Addresses\n{firstusablehosts}\n{lastusablehosts}")
print()

