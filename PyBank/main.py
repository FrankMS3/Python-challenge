import os
import csv

# Setting working directory
os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join("Resources", "budget_data.csv")

# Setting variables
total = 0
row_count = 0
previous = 0
change = []
max_date = 0
min_date = 0
mydict = {}


# Reading .csv file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Getting values row by row
    for row in csvreader:
        total = int(total) + int((row[1]))
        row_count = int(row_count) + 1
        change.append((int(row[1]) - previous))
        mydict[row[0]] = (int(row[1]) - previous)
        previous = int(row[1])
        maximum = max(change)
        minimum = min(change)

    # Calculations and finding other values
    change.pop(0)
    avg = sum(change)/(len(change))
    max_date = [k for k, v in mydict.items() if v == maximum]
    min_date = [k for k, v in mydict.items() if v == minimum]

# Printing values
print("Financial Analysis")
print("-------------------------------")
print("Total Months: " + str(row_count))
print("Total: $" + str(total))
print("Average Change: $" + str(avg))
print("Greatest Increase in Profits: " + str(max_date) + " ($" + str(maximum) + ")")
print("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(minimum) + ")")

# Setting new directory
os.chdir(os.path.dirname(__file__))
new_file = os.path.join('Analysis', 'Analysis.txt')

# Creating a text file with the results
with open(new_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------\n")
    file.write("Total Months: " + str(row_count) + "\n")
    file.write("Total: $" + str(total) + "\n")
    file.write("Average Change: $" + str(avg) + "\n")
    file.write("Greatest Increase in Profits: " + str(max_date) + " ($" + str(maximum) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(min_date) + " ($" + str(minimum) + ")\n")

    