#Algo for file updates in Python
#Scenario

# Review the following scenario. Then complete the step-by-step instructions.
# You are a security professional working at a health care company. 
# As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content. 
# The contents of the file are based on who is working with personal patient records. 
# Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. 
# There's also a remove list that identifies which employees you must remove from this allow list.
# Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. 
# If so, you should remove those IP addresses from the file containing the allow list.

#======================================================================================#

import_file = "allow_list.txt"
remove_list = "remove_list.txt"

def remove_func (remove_list):
	with open(remove_list,"r") as file: #opens text file containing known bad addresses
		bad_addresses = file.read()
	bad_addresses = bad_addresses.split() #string to list
	
	print("Bad address list:",bad_addresses) #display the list of bad addresses


def revise_file (import_file, bad_addresses):
	with open(import_file, "r") as file:
		ip_addresses = file.read()
	ip_addresses = ip_addresses.split() #converts the string contained into a list

	print("Known IP addresses:",ip_addresses) #Display list of known IPs
	
	for element in ip_addresses: #iterates through the new list, naming a variable 'element'
		if element in bad_addresses:
				ip_addresses.remove(element) #if the 'element" is found, remove it from new list'

	ip_addresses = " ".join(ip_addresses) # back to a string. Bring out of for loop

	with open (import_file, "w") as file: #open it with write permissions
		file.write(ip_addresses) #put that data from the new list-to-string back into 'allow_list.txt'


remove_func(remove_list)
revise_file(import_file,bad_addresses)

print("Newly created allow list:",ip_addresses) #show us the end result