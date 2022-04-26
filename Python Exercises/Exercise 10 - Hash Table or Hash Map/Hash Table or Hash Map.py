# Declare a dictionary
dict = {'Name': 'Ankit Gupta', 'Age': 22, 'Designation': 'Analyst'}

# Accessing the dictionary with its key
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

# update dictionary values
dict['Age'] = 24 # update existing entry
dict['College'] = "BIT Mesra" # Add new entry
print ("dict['Age']: ", dict['Age'])
print ("dict['College']: ", dict['College'])

# remove / delete dictionary values
del dict['Name'] # remove entry with key 'Name'
dict.clear()    # remove all entries in dict
del dict     # delete entire dictionary
print ("dict['Age']: ", dict['Age'])
print ("dict['College']: ", dict['College'])