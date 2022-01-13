# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from itertools import count
import os
from platform import java_ver

# Add a variable to load a file from a path.
#---------------------------------------
# I had to delete ".." ---> what is this? why did I have to delete it?
#---------------------------------------
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
#create county list -> uses []
county_list = []
#create county votes dictionary -> {}
county_votes = {}

#create a dictionary for number of votes per cand/county
Cand_votes_by_county = {}

JeffersonVotes = 0
Jefferson_by_candidate = {}
# ArapahoeVotes = 0
# Arapahoe_by_candidate = {}
# DenverVotes = 0
# denver_by_candidate = {}
# Diana_Jefferson = 0
# Diana_Arapahoe = 0
# Diana_Denver = 0
# Charles_Jefferson = 0
# Charles_Arapahoe = 0
# Charles_Denver = 0
# Ray_Jefferson = 0
# Ray_Arapahoe = 0
# Ray_Denver = 0

# Read the csv and convert it into a list of dictionaries

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        # total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

         # 5: Add a vote to that county's vote count.
        # county_votes[county_name] += 1

        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

# JeffersonVotes = [] is a list with the number of votes - maybe I don't need this
# Jefferson_by_candidate = {} - a dictionary that will store the number of votes 
    for candidate_name in candidate_options:
        if county_name == "Jefferson":
            Jefferson_by_candidate[candidate_name] = JeffersonVotes
            JeffersonVotes =+ 1
            


    # for candidate_name in candidate_options:
    #     for county_name in county_list:
    #         Cand_votes_by_county[candidate_name][county_name]

            # Arapahoe_by_candidate[candidate_name] = ArapahoeVotes
            # denver_by_candidate[candidate_name] = DenverVotes




#What I want my end result to be:
# Jefferson_by_candidate {
#       "Charles Casper Stockham": # votes in Jefferson, 
#       "Diana DeGette" : # votes in Jefferson,
#       "Raymon Anthony Doane" : # votes in Jefferson,} 
# Arapahoe_ by_candidate
# Denver_by_candidate








        #     # elif county_name == "Arapahoe":
            #     Arapahoe_by_candidate[candidate_name] += 1
            # elif county_name == "Denver":
            #     denver_by_candidate[candidate_name] += 1


        # if candidate_name == "Diana DeGette" and county_name == "Jefferson":
        #     JeffDiana += 1

# print(Arapahoe_by_candidate)
# print(candidate_options[0])
# print(Jefferson_by_candidate)


# print(candidate_options)

#         if candidate_name == "Diana DeGette": 
#             if county_name == "Jefferson":
#                 Diana_Jefferson += 1
#             elif county_name == "Arapahoe":
#                 Diana_Arapahoe += 1
#             elif county_name == "Denver":
#                 Diana_Denver += 1
# #         if candidate_name == "Charles Casper Stockham": 
# #             if county_name == "Jefferson":
# #                 Charles_Jefferson += 1
# #             elif county_name == "Arapahoe":
# #                 Charles_Arapahoe += 1
# #             elif county_name == "Denver":
# #                 Charles_Denver += 1
# # Ray_Jefferson = 0
# # Ray_Arapahoe = 0
# # Ray_Denver = 0


# Diana_results = (
#     f"Diana DeGette:\n"
#     f"\tJefferson County: {Diana_Jefferson:,} votes \n"
#     f"\tArapahoe County: {Diana_Arapahoe:,} votes \n "
#     f"\tDenver County: {Diana_Denver:,} votes\n")
# # Charles_results = (
# #     f"Charles Casper Stockham:\n"
# #     f"\tJefferson County: {Charles_Jefferson:,} votes \n"
# #     f"\tArapahoe County: {Charles_Arapahoe:,} votes \n "
# #     f"\tDenver County: {Charles_Denver:,} votes\n")

# print(Diana_results)
# # print(Charles_results)

