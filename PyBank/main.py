# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The net total amount of "Profit/Losses" over the entire period      
#   * The average of the changes in "Profit/Losses" over the entire period
#   * The greatest increase in profits (date and amount) over the entire period
#   * The greatest decrease in losses (date and amount) over the entire period
# * As an example, your analysis should look similar to the one below:
#   * The total number of months included in the dataset
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import os
import csv

budget_data = os.path.join("Resources" , "budget_data.csv")

with open (budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    delta = []
    prevMonth = 0
    totalMonths = []
    monthsList = []
    greatestIncrease = 0
    greatestDecrease = 0
    increaseIndex = 0
    decreaseIndex = 0

    for row in csvreader:
        totalMonths.append(int(row[1]))
        monthsList.append(row[0])
        months = len(totalMonths)
        profitsTotal = sum(totalMonths)
        
        if prevMonth == 0:
            prevMonth = int(row[1])
        else:
            delta.append(int(row[1])-prevMonth)
            prevMonth = int(row[1])

avgDelta = sum(delta) / len(delta)

greatestIncrease = max(delta)
greatestDecrease = min(delta)

increaseIndex = delta.index(greatestIncrease)
decreaseIndex = delta.index(greatestDecrease)

#final script

analysisText = (f"""
    Financial Analysis
    ---------------------------------
    Total Months: {months}
    Total: $ {profitsTotal}
    Average Change: ${round(avgDelta, 2)}
    Greatest Increase in Profits:  {monthsList[increaseIndex+1]} (${greatestIncrease})
    Greatest Decrease in Profits:  {monthsList[decreaseIndex+1]} (${greatestDecrease})
    """)
    

print(analysisText)

#final text output

file = os.path.join("analysis", "PyBank_Results.txt")
 
with open (file, 'w') as text:
    text.write(analysisText)
    


   


            
        











    