import os
import csv

pollsData = os.path.join('Resources' , 'election_data.csv')

votesTotal = 0
canidates = []
percVotes = []
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
print(f"Total Votes: {votesTotal}")

for i in canidatesVotes:
    percVotes = (canidatesVotes[i])/(votesTotal)*100
    print(f"{i} {percVotes:.3f}% {canidatesVotes[i]}")

for key in canidatesVotes.keys():
    if canidatesVotes[key] == max(canidatesVotes.values()):
        winner = key

print(f"Winner: {winner}")




