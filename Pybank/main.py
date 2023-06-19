import os
import csv

# defining variables
total_month = 0
total_amount = 0
changes = 0
avg_change = 0
greatest_increase = 0
greatest_decrease = 0

#defining path to csv file in resources
path = os.path.join('python-challenge','Pybank','Resources','budget_data.csv')
    
# Reading the csv file 
with open(path) as budget:
    budget_reader = csv.reader(budget, delimiter = ',')
    
    #read the header row first
    header= next(budget_reader)
    
    for row in budget_reader:

        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        total_month += 1
        total_amount += int(row[1])

print(f"Total Months : {total_month}")
print(f"Total : {total_amount}")