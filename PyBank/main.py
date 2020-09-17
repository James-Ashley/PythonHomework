import os
import csv

budget_data = os.path.join ("Resources","budget_data.csv")

with open (budget_data, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)
    
    totalMonths = []
    
    profitsLosses = [] 
    
    previousTotal = []

    for row in csvreader:
    
        totalMonths.append(row[0])
    
        profitsLosses.append(int(row[1]))
    
        previousTotal=(int(row[1]))

numMonths = len(totalMonths)

netTotal = sum(profitsLosses)

print(numMonths, netTotal)

print(previousTotal)

avgChange = []


# for row in csvreader:
    
#  print(previousTotal)
    # currentTotal=(int(row)[1]-previousTotal)
    # print(currentTotal)
    
         

# greatIncrease =
# greatDecrease =



    