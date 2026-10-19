'''
5. Create a variable named 'intf' using the following string (from 'show ip interface brief' on a Cisco router):
intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
split() this variable into fields based on white-space and save this to a variable named intf_fields.

From this new 'intf_fields' variable, create variables named intf_name, intf_ip_addr, intf_status, 
intf_protocol and match the corresponding fields from the above output (the first two fields and the last two fields, 
respectively).

Print out each of these four variables and their corresponding values.

Create booleans indicating whether both line status and line protocol are in the 'up' state. Print these booleans to the screen.
'''

intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up                    up"
intf_fields = intf.split()
print(intf_fields)

intf_name = intf_fields[0]
intf_ip = intf_fields [1]
intf_status = intf_fields [2]
intf_prot = intf_fields [3]
line_status = intf_fields [4]
line_protocol = intf_fields [5]

status = "up" in line_status
protocol = "up" in line_protocol 

print(f"Is the line status up? {status}")
print(f"\nIs the line protocol up? {protocol}")

print (f"\nInterface name:{intf_name}")
print (f"\nIP Address:{intf_ip}")
print (f"\nInterface Status:{intf_status}")
print (f"\nInterface Protocol:{intf_prot}")