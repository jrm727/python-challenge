#PyBank Main 
#Import os mmodule to create file paths across operating systems
import os
import csv
csvpath = os.path.join('/Users/jessmroczek/Documents/DA Bootcamp/Homework Files/03-Python/Instructions/Starter_Code/PyBank/Resources/budget_data.csv')

#List to Store Data
Date = []
Profit_Loses = []
Total_Month = []

# Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
        #add date 
        Date.append(row[0])
        # add Profit_Loses
        Profit_Loses.append(int(row[1]))
        
#* The total number of months included in the dataset
#Finding the sum of Months 
Total_Month = len(Date)

#* The net total amount of "Profit/Losses" over the entire period
#add all profits and losses together to get a total
Total_PL = sum(Profit_Loses)

#* The changes in "Profit/Losses" over the entire period, and then the average of those changes
# Calculate change for each row
Period_Change = []

for x in range(1, len(Profit_Loses)):
    Period_Change.append(int(Profit_Loses[x])- int(Profit_Loses[x-1]))

# Calculate the Average of Changes
# Calculate the average (sum of changes/ # of months in period)
Period_Change_Average = sum(Period_Change)/len(Period_Change)
Rounded_Period_Change_Average = round(Period_Change_Average, 2)

#* The greatest increase in profits (date and amount) over the entire period
# Find the greatest increase - reference math from VBA project
Greatest_Increase = max(Period_Change)

#* The greatest decrease in profits (date and amount) over the entire period
# The greatest decrease - reference math and logic from the VBA project
Greatest_Decrease = min(Period_Change)

#Print Prompts
print("Financial Analysis")
print("------------------------")
print("Total Month:" + str(Total_Month))
print("Total:" + str(Total_PL))
print("Average Change:" + str(Rounded_Period_Change_Average))
print("Greatest Increase in Profits:" + str(Greatest_Increase))
print("Greattest Decrease in Profits:" + str(Greatest_Decrease))

#also need to include an export of a text file with the results
# Print results to a txt file
# Reference: https://www.pythontutorial.net/python-basics/python-write-text-file/

lines = ["Financial Analysis",
"------------------------",
"Total Month:" + str(Total_Month),
"Total:" + str(Total_PL),
"Average Change:" + str(Rounded_Period_Change_Average),
"Greatest Increase in Profits:" + str(Greatest_Increase),
"Greatest Decrease in Profits:" + str(Greatest_Decrease)]
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

