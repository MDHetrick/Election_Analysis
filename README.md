# Colorado Election Analysis

## Project Overview
The goal of this project is to perform an audit on a recent local Colorado election. This audit will look at the following deliverables:

1. Calculate total number of votes cast.
2. Get a complete list of candidates who received votes
3. Calculate total number of votes each candidate received.
4. Calculate percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.3, Visual Studio Code 1.63.2

## Summary
### The analysis of the election show that:
- There were 369,711 votes cast in the election
- Three counties were represented in this election:
  - Jefferson
  - Denver
  - Arapahoe
- The county results were:
  - Jefferson: 38,855 votes (10.5%)
  - Denver: 306,055 votes (82.8%)
  - Arapahoe: 24,801 votes (6.7%)
- The largest county turnout was Denver county with 306,055 votes
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote with 85,213 votes.
  - Diana DeGette received 73.8% of the vote with 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote with 11,606 votes.
- The winner of the election was:
  - Diana DeGette who received 73.8% of the vote with 272,892 votes.
### Future Elections:
The script could be used in future elections with some minor changes.

The script can be modified to give us the county with the lowest turnout. We can access the county_votes dictionary and pull out the lowest turnout. The winner could also be determined this way, if we change min to max in both places in the middle line.

```
    losing_county_summary = (
        f"\n-------------------------\n"
        f"Smallest County Turnout:\n {min(county_votes, key=county_votes.get)} ({county_votes[min(county_votes, key=county_votes.get)]:,} votes)\n"
        f"---------------------------\n")
    print(losing_county_summary)

```

The script can also be modified to look at how many votes were given to each candidate in each county. First, dictionaries can be added for each candidate that list each county.

```
Diana_Dict = {
    "Denver": 0,
    "Arapahoe": 0,
    "Jefferson": 0
}
Ray_Dict = {
    "Denver": 0,
    "Arapahoe": 0,
    "Jefferson": 0
}
Charles_dict = {
    "Denver": 0,
    "Arapahoe": 0,
    "Jefferson": 0
}
```
Then, we can iterate through the rows and count the votes each candidate got in each county. This can be placed within the current code.

```
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        if candidate_name == "Diana DeGette":
            Diana_Dict[county_name] += 1
        elif candidate_name == "Raymon Anthony Doane":
            Ray_Dict[county_name] += 1
        elif candidate_name == "Charles Casper Stockham":
            Charles_dict[county_name] += 1

```

Then the results can be formatted and printed.

```
Diana_votes_county = (
    f'\n-----------------------------\n'
    f'Diana DeGette\n' 
    f'Arapahoe County: {Diana_Dict["Arapahoe"]:,} votes\n'
    f'Jefferson County: {Diana_Dict["Jefferson"]:,} votes\n'
    f'Denver County: {Diana_Dict["Denver"]:,} votes'
    f'\n-----------------------------\n'
)

Charles_votes_county = (
    f'\n-----------------------------\n' 
    f'Charles Casper Stockham\n' 
    f'Arapahoe County: {Charles_dict["Arapahoe"]:,} votes\n'
    f'Jefferson County: {Charles_dict["Jefferson"]:,} votes\n'
    f'Denver County: {Charles_dict["Denver"]:,} votes'
    f'\n-----------------------------\n'
)

Ray_votes_county = (
    f'\n-----------------------------\n'
    f'Raymon Anthony Doane \n' 
    f'Arapahoe County: {Ray_Dict["Arapahoe"]:,} votes\n'
    f'Jefferson County: {Ray_Dict["Jefferson"]:,} votes\n'
    f'Denver County: {Ray_Dict["Denver"]:,} votes'
    f'\n-----------------------------\n'
)

print(Diana_votes_county)
print(Ray_votes_county)
print(Charles_votes_county)
```

For this to be relevant to future elections, it would require some editing to incorporate all the relevant information such as candidate names and county names. If this breakdown is desired, the initial code can be run to obtain this information, and then the extended code can be modified and run to provide the more granular information.


