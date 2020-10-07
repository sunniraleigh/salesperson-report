"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #generates an empty list
melons_sold = [] #generates an empty list

f = open('sales-report.txt') # opens text files into a reference called f
for line in f: # goes through each line in the file
    line = line.rstrip() #strips white space from each line
    entries = line.split('|') #turns each line into a list

    salesperson = entries[0] #identifies salesperson in the list entries
    melons = int(entries[2]) # identifies melons sold by a saleperson in the list entries

    if salesperson in salespeople:
        position = salespeople.index(salesperson) #if the saleperson is already in a list, get the index of that salesperson

        melons_sold[position] += melons #add to the number of melons that salesperson has sold
    else:
        salespeople.append(salesperson) #if the salesperson was not in the list, add them
        melons_sold.append(melons) # add the number of melons they sold


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #for each salesperson, print their name and how many melons they sold

""" List of improvements:
    - utilize dictionary methods to do lines 15-21 in one line
    - name variables more descriptively such as 'f'

"""
