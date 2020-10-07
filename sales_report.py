def report_sales(file_path):
    """ Generate sales report showing total melons each salesperson sold."""

    sales = {}

    file = open(file_path) # opens text files into a reference called f

    for line in file: # goes through each line in the file
        line = line.rstrip() #strips white space from each line
        entries = line.split('|') #turns each line into a list

        salesperson = entries[0] #identifies salesperson in the list entries
        melons = int(entries[2]) # identifies melons sold by a saleperson in the list entries

        sales[salesperson] = sales.get(salesperson, 0) + melons

    for salesperson, melons in sales.items():
        print(f"{salesperson} sold {melons} melons")

report_sales("sales-report.txt")

""" List of improvements:
    - utilize dictionary methods to do lines 15-21 in one line
    - name variables more descriptively such as 'f' and 'i'
    - define whole process as a function
    - add data to a dictionary rather than 2 separate lists
"""
