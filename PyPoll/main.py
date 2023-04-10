# Import 
import os, csv
from pathlib import Path
# file location
input_file = Path("python-challenge", "PyPoll", "Resources" "election_data.csv")
# Create empty lists to iterate through specific rows for the following variables
total_votes = 0
candidatename = []
candidates=[]
votespercandidate = {}
csvpath = "./Resources/election_data.csv"
# Winner math
wincount = 0
winpercent = 0

# Open csv 
with open(csvpath, "r") as csvfile:
     # Store the contents in variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip header labels
    header = next(csvreader)
    for row in csvreader:
        #count total votes
        total_votes += 1
    #get candidate names
        candidatename=row[2]
        if candidatename not in candidates:
             candidates.append(candidatename)
             votespercandidate[candidatename]=0
        # Obtain the total votes for each candidate
        votespercandidate[candidatename]+=1
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------") 
# Determine the percentage of votes for each candidate by looping through the counts. 
for candidatename in votespercandidate:
    votes = votespercandidate[candidatename]
    vote_percentage = float(votes)/float(total_votes) * 100
    print(f"{candidatename}: {vote_percentage:.1f}% ({votes:,})\n")
    print("----------------------------")
    # Determine winning vote count and candidate
    if (votes > wincount) and (vote_percentage > winpercent):
# 2. If true then set winning_count = votes and winning_percent = # vote_percentage.
        wincount = votes
        winpercent = vote_percentage
        winning_candidate = candidatename
print (f"Winner: {winning_candidate}\n")


# Output files
output_file = "./Analysis/election_analysis.csv"
with open(output_file,"w") as file:
# Write methods to print to Election_Analysis_Summary
    file.write("Election Results")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"{candidatename}: {vote_percentage:.1f}% ({votes:,})\n")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {winning_candidate}\n")

