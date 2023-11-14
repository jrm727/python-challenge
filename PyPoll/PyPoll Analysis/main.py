#main.py for PyPoll 
#Import os mmodule to create file paths across operating systems
import os
import csv
csvpath = os.path.join('/Users/jessmroczek/Documents/DA Bootcamp/Homework Files/03-Python/Instructions/Starter_Code/PyPoll/Resources/election_data.csv')

#List to Store Data
Ballot_ID = []
County = []
Canidate = []

# Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    for row in csvreader:
        #add Ballot ID 
        Ballot_ID.append(row[0])
        # add County
        County.append(row[1])
        # add Canidate
        Canidate.append(row[2])

#* The total number of votes cast
Total_Votes = len(Ballot_ID)

#* A complete list of candidates who received votes
Canidate_List = []
Raymon_Anthony_Doane = []
Raymon_Anthony_Doane_Votes = 0
Diana_DeGette = []
Diana_DeGette_Votes = 0
Charles_Casper_Stockham = []
Charles_Casper_Stockham_Votes = 0

# Count Votes of each canidate and Store Names of Each Canidate with append Canidate List
for x in Canidate: 
    # Checks if one value is equal to another
    if x == "Raymon Anthony Doane":
        Raymon_Anthony_Doane.append(Canidate_List)
        Raymon_Anthony_Doane_Votes += 1
    elif x == "Diana DeGette":
        Diana_DeGette.append(Canidate_List)
        Diana_DeGette_Votes += 1
    else: 
        Charles_Casper_Stockham.append(Canidate_List)
        Charles_Casper_Stockham_Votes += 1

#* The percentage of votes each candidate won
Percent_Vote_For_RAD = round(((Raymon_Anthony_Doane_Votes/Total_Votes) * 100), 3)
Percent_Vote_For_DD = round(((Diana_DeGette_Votes/Total_Votes) * 100), 3)
Percent_Vote_For_CCS = round(((Charles_Casper_Stockham_Votes/Total_Votes) * 100), 3)

#* The winner of the election based on popular vote
if Percent_Vote_For_RAD > (Percent_Vote_For_DD and Percent_Vote_For_CCS):
    Winner = "Raymon Anthony Doane"
elif Percent_Vote_For_DD > (Percent_Vote_For_RAD and Percent_Vote_For_CCS):
    Winner = "Diana DeGette"
else:
    Winner = "Charles Casper Stockham"

#print results
print("Election Results")
print("-------------------------")
print('Total Votes:' + str(Total_Votes))
print("-------------------------")
print(f'Charles Casper Stockham: {Percent_Vote_For_CCS}% ({Charles_Casper_Stockham_Votes})')
print(f'Diana_DeGette: {Percent_Vote_For_DD}% ({Diana_DeGette_Votes})')
print(f'Raymon Anthony Doane: {Percent_Vote_For_RAD}% ({Raymon_Anthony_Doane_Votes})')
print("-------------------------")
print(f'Winner: {Winner}')
print("-------------------------")

lines = ["Election Results",
"------------------------",
'Total Votes:' + str(Total_Votes),
"------------------------",
(f'Charles Casper Stockham: {Percent_Vote_For_CCS}% ({Charles_Casper_Stockham_Votes})'),
(f'Diana_DeGette: {Percent_Vote_For_DD}% ({Diana_DeGette_Votes})'),
(f'Raymon Anthony Doane: {Percent_Vote_For_RAD}% ({Raymon_Anthony_Doane_Votes})'),
"------------------------",
(f'Winner: {Winner}'),
'------------------------']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')