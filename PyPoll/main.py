import os
import csv

# Setting working directory
os.chdir(os.path.dirname(__file__))
election_data_csv = os.path.join("Resources", "election_data.csv")

# Setting variables
total = 0
candidates = []
votes = {}
winner_votes = 0
winner = 0
percent = []

# Reading .csv file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        total = total + 1
        # Adding unique candidates to list and votes to dictionary
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1

# Getting % of vote and the winner
for v in votes:
    cv = votes.get(v)
    percent.append((cv / total) * 100)
    if cv > winner_votes:
        winner_votes = cv
        winner = v

# Printing to terminal
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total))
print("-----------------------------")
print(str(candidates[0]) + ": " + str(percent[0]) + "% (" + str(votes[candidates[0]]) + ")")
print(str(candidates[1]) + ": " + str(percent[1]) + "% (" + str(votes[candidates[1]]) + ")")
print(str(candidates[2]) + ": " + str(percent[2]) + "% (" + str(votes[candidates[2]]) + ")")
print("-----------------------------")
print("Winner: " + str(winner))
print("-----------------------------")

# Exporting results to a text file
new_file = os.path.join("Analysis", "PyPoll Analysis.txt")
with open(new_file, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------\n")
    file.write("Total Votes: " + str(total) + "\n")
    file.write("----------------------\n")
    file.write(str(candidates[0]) + ": " + str(percent[0]) + "% (" + str(votes[candidates[0]]) + ")\n")
    file.write(str(candidates[1]) + ": " + str(percent[1]) + "% (" + str(votes[candidates[1]]) + ")\n")
    file.write(str(candidates[2]) + ": " + str(percent[2]) + "% (" + str(votes[candidates[2]]) + ")\n")
    file.write("----------------------\n")
    file.write("Winner: " + str(winner) + "\n")
    file.write("----------------------\n")
    