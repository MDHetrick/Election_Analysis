# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize total votes counter
total_votes = 0
#Get the candidate from each list
candidate_options = []
#declare empty candidate votes dictionary
candidate_votes = {}
#winner trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    #read the file object with reader function
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    #print each row in csv file
    for row in file_reader:
        #Add the total vote count
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]
        #if the candidate does not match existing candidate
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
            #add to vote total
        candidate_votes[candidate_name] += 1
with open(file_to_save, "w") as txt_file:
    election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"TotalVotes: {total_votes:,}\n"
            f"---------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) *100
        #print(f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #set winning count = votes and winning percent = percent
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    print(f"{winning_candidate} won with {winning_count} votes, representing {winning_percentage:.1f}% of the votes.")
    winning_candidate_summary = (
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning vote count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
    #print(winning_candidate_summary)


    


#1. Total number of votes cast
#2. Complete list of candidates
#3. Percent of votes each candidate received
#4. Total number of votes each candidate won
#5. Winner of election based on popular vote
#create filename variable to direct or indirect path to file
