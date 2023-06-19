import os
import csv

# defining variables
total_month = 0
total_amount = 0
changes = [] 
previous = 0
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

        # Calculate total month by counting the rows as each rows have unique month
        total_month += 1
        #Calculate total amount by summing them all
        total_amount += int(row[1])
        # Calculate changes
        current_change = int(row[1])
        if total_month > 1:
            
            change = current_change - previous
            changes.append(change)
    
        previous = current_change  
        
    #Calculating average change
    avg_change = sum(changes)/len(changes)
    avg_change = round(avg_change, 2)
    
    #Calculating greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)
    
    
    
print(f"Total Months : {total_month}")
print(f"Total : {total_amount}")
print(f"Average Change : $ {avg_change}")
print(f"Greatest increase in profits : {greatest_increase}")
print(f"Greatest decrease in profits : {greatest_decrease}")

output_path = os.path.join('python-challenge','Pybank','analysis','financial_analysis.txt') 

with open(output_path,'w') as result:
    result.write(f"Total Months : {total_month}\n")
    result.write(f"Total : {total_amount}\n")
    result.write(f"Average Change : $ {avg_change}\n")
    result.write(f"Greatest increase in profits : {greatest_increase}\n")
    result.write(f"Greatest decrease in profits : {greatest_decrease}\n")