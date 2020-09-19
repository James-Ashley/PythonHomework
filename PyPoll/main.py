# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

import os
import csv

pollsData = os.path.join('Resources' , 'election_data.csv')

#   * The total number of votes cast

votesTotal = 0
canidates = []
percVotes = []
candVotesstring = ""
canidatesVotes = {}

with open (pollsData, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        canidates = row[2]
        if canidates not in canidatesVotes.keys():
            canidatesVotes[canidates] = 1
        else:
            canidatesVotes[canidates] = canidatesVotes[canidates]+1

votesTotal = sum(canidatesVotes.values())

# print(f"Total Votes: {votesTotal}")

#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won

for i in canidatesVotes:
    percVotes = (canidatesVotes[i])/(votesTotal)*100
    candVotesstring += (f"{i} {percVotes:.3f}% ({canidatesVotes[i]})\n")

#   * The winner of the election based on popular vote.

for key in canidatesVotes.keys():
    if canidatesVotes[key] == max(canidatesVotes.values()):
        winner = key

# print(candVotesstring)
# print(f"Winner: {winner}")

analysisText = (f"""
Election Results
------------------------
Total Votes: {votesTotal}
------------------------
{candVotesstring}------------------------
Winner: {winner}
------------------------""")

print(analysisText)

#final text output

file = os.path.join("analysis", "PyPoll_Results.txt")
 
with open (file, 'w') as text:
    text.write(analysisText)
    text.close