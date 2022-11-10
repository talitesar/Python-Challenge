# Python Analysis of Polling Data
# By: Tali Tesar
# Created November, 2022

# Import necessary modules; os for setting filepath across different operating systems and csv for reading csv file types
import os
import csv

# Set the filepath for opening the csv file
votes_csv = os.path.join("Resources", "election_data.csv")

########### GENERATING VARIABLES TO STORE INFORMATION WHILE ITERATING

# Generate variable for total number of votes
total_votes=0
# Generate dictionary of candidates and vote totals to be filled while iterating
candidate_votes = {}

########### ITERATING THROUGH CSV FILE AND TALLYING VOTES

# Open and read csv file
with open(votes_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the header
    next(csv_reader)

    # Start iterating
    for row in csv_reader:

        # Add one to total votes
        total_votes += 1

        # Check if dictionary already has candidate name in it
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 0
            
        if row[2] in candidate_votes:
            candidate_votes[row[2]] += 1
            

########### CALCULATING PERCENTAGES BASED ON VOTE TALLYS AND STORING THEM IN NEW DICTIONARIES

# Generating lists to store the info from the dictionary candidate votes
candidate_name = []
candidate_percent_list = []
candidate_votes_list = []

# Iterating through the dictionary candidate_info and storing the information separately
for key in candidate_votes.keys():
    candidate_name.append(key)

for value in candidate_votes.values():
    candidate_votes_list.append(value)
    candidate_percent_list.append(round((value/total_votes)*100, 2))


########### PRINTING FINAL ANALYSIS TO TERMINAL AND EXPORTING TO TEXT FILE

# Print to terminal
print("Election Results") 
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")
print(f'{candidate_name[0]}: {candidate_percent_list[0]}% ({candidate_votes_list[0]})')
print(f'{candidate_name[1]}: {candidate_percent_list[1]}% ({candidate_votes_list[1]})')
print(f'{candidate_name[2]}: {candidate_percent_list[2]}% ({candidate_votes_list[2]})')
print("----------------------------")
print(max(candidate_votes, key=candidate_votes.get))
print("----------------------------")

# Set up file path for new text file
txtpath = os.path.join("Analysis", "election_results.txt")

# 
with open(txtpath, 'w') as text:
    text.write("Election Results\n") 
    text.write("----------------------------\n")
    text.write(f'Total Votes: {total_votes}\n')
    text.write("----------------------------\n")
    text.write(f'{candidate_name[0]}: {candidate_percent_list[0]}% ({candidate_votes_list[0]})\n')
    text.write(f'{candidate_name[1]}: {candidate_percent_list[1]}% ({candidate_votes_list[1]})\n')
    text.write(f'{candidate_name[2]}: {candidate_percent_list[2]}% ({candidate_votes_list[2]})\n')
    text.write("----------------------------\n")
    text.write(f'max(candidate_votes, key=candidate_votes.get)\n')
    text.write("----------------------------")
