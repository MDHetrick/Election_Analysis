# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    


#1. Total number of votes cast
#2. Complete list of candidates
#3. Percent of votes each candidate received
#4. Total number of votes each candidate won
#5. Winner of election based on popular vote
#create filename variable to direct or indirect path to file
