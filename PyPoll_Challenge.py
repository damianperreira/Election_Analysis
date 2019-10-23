

import csv
import random
import numpy
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Create Candidate list
candidate_options = []
# Create County list
county_options = []

# Declare the empty dictionary
candidate_votes = {}
# County Dict
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Winning county Tracker
winning_county = ""
winning_cnty_count = 0
winning_cnty_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row. 
    headers = next(file_reader)

# Candidate ------------------------------------------   
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1 
       
        # Print the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
           # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# County ------------------------------------------
        # Print the county name from each row (select position 1)
        county_name = row[1]

        if county_name not in county_options:
           # Add the county name to the county list
            county_options.append(county_name)

            # Begin tracking that county's vote count
            county_votes[county_name] = 0

        # Add a vote to that county's count
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:
    election_results = ("\n"
        "Election results:\n"
        "\n"
        "-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        "-------------------------\n"
        "\n"
        "Candidate Summary\n"
        "-------------------------\n")

    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through the candidate list
    for candidate in candidate_votes:
        # get vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes
        vote_percentage = int(votes) / int(total_votes) * 100

        # Print each candidate, their voter count, and percentage to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.2f}% ({votes:,})")

        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
    print("\nCounty Summary")
    print("-------------------------")
# Determine the percentage of votes for each county by looping through the counts
# Iterate through the county list
    for county in county_votes:
        # Retrieve vote count of a county
        cvotes = county_votes[county]
        # Calculate the percentage of votes
        county_vote_percentage = int(cvotes) / int(total_votes) * 100

        # Print each county, their voter count, and percentage to the terminal
        county_results = (f"{county} county: {county_vote_percentage:.2f}% ({cvotes:,})")

        # Print each county, their voter count, and percentage to the terminal
        print(county_results)
        # Save the county results to our text file
        txt_file.write(county_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate

        # Determine winning vote count and county
        if (cvotes > winning_cnty_count) and (county_vote_percentage > winning_cnty_percentage):
            # If true then set winning_cnty_count = cvotes and winning_cnty_percent = county_vote_percentage
            winning_cnty_count = cvotes
            winning_cnty_percentage = county_vote_percentage
            # And, set the winning_county equal to the county's name
            winning_county = county

    winning_candidate_summary = ("\n"
        f"Winning Candidate\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        "\n"
        f"Winning County\n"
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_cnty_count:,}\n"
        f"Winning Percentage: {winning_cnty_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)