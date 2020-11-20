import os
import csv

os.getcwd()
csvpath = os.path.join("PyPoll", "Resources", "ElectionData.csv")
txtpath = os.path.join("PyPoll", "Analysis", "Analysis.txt")

counter = 0
candidates = set()
votes = {}
maxvotes = 0
winner = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        counter = counter + 1
        candidates.add(row[2])
        if row[2] in votes:
            votes[row[2]] = votes[row[2]] + 1
        else:
            votes[row[2]] = 1
    results = {"Total Votes": counter}
    for i in votes:
        results[i] = ["{:.2%}".format(votes[i]/counter), votes[i]]
        if votes[i] > maxvotes:
            maxvotes = votes[i]
            winner = i
    results["Winner"] = winner
    print(results)

opentxt = open(txtpath, "w")
opentxt.write(str(results))