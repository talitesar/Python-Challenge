# Python Analysis of Budget Data
# By: Tali Tesar
# Created November, 2022

# Import necessary modules; os for setting filepath across different operating systems and csv for reading csv file types
import os
import csv

# Set the filepath for opening the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

########### GENERATING VARIABLES TO STORE INFORMATION WHILE ITERATING

# Generate variable to store sum
total = 0
# Generate variable for number of months
months = 0
# Generate list to store change values and the current month
change_values = []
month_list = []

############# CONDUCTING FOR LOOP AND POPULATING VARIABLES 

# Open and read the csv file 
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header
    next(csv_reader)

    # Loop through the rows of the csv file:
    for row in csv_reader:
        # Add value of profit/loss to the total
        total = total + int(row[1])
        # Add one to the months counter
        months = months + 1
        # For rows other than first row, store change value in list
        if months > 1:
            change_values.append(int(row[1]) - int(prev_val))
            month_list.append(row[0])

        # Store previous month value
        prev_val = row[1]

# Finding the mean value of change list
sum = sum(change_values)
mean_change = round(sum/len(change_values), 2)

# Finding the maximum and minimum values for change
max_increase = max(change_values)
max_decrease = min(change_values)

# Enumerating through the change values list to find the match to the month of that value
for i, change in enumerate(change_values):
    if change==max_increase:
        max_month = month_list[i]
    if change==max_decrease:
        min_month = month_list[i]

############# PRINTING FINAL ANALYSIS TO TERMINAL AND EXPORTING AS TEXT FILE

# Print to terminal
print("Financial Analysis") 
print("----------------------------")
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: ${mean_change}')
print(f'Greatest Increase in Profits: {max_month} ({max_increase})')
print(f'Greatest Decrease in Profits: {min_month} ({max_decrease})')

# Exporting to a new text file
# Set up file path for new text file
txtpath = os.path.join("Analysis", "budget_analysis.txt")

# Export final analysis
with open(txtpath, 'w') as text:
    text.write("Financial Analysis\n") 
    text.write("----------------------------\n")
    text.write(f'Total Months: {months}\n')
    text.write(f'Total: ${total}\n')
    text.write(f'Average Change: ${mean_change}\n')
    text.write(f'Greatest Increase in Profits: {max_month} ({max_increase})\n')
    text.write(f'Greatest Decrease in Profits: {min_month} ({max_decrease})')