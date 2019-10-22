# Election Analysis

## Project Overview
A Colorado Board of Elections employee has provided the following tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the elction based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election shows that:
 - There were 369,711 votes cast in the election.
 - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
 - The candidate results were:
    - Charles Casper Stockham received 23.05% of the vote and 85,213 number of votes
    - Diana DeGette received 73.81% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.14% of the vote and 11,606 number of votes.
 - The winner opf the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
 
 ## Overview
 There was only one source of data provided (election_results.csv) each row in the file represented a single vote and icluded attributes identofying the candidate.
 
 Python was used to read and write to the file and create a separate file with a summary of the analysis (election_analysis.csv).
 
 ## Summary
In summary we were able to show the distribution of votes accross three candidates as both a count of votes and a percent of total. The winner was identified by popular vote as having the highest count and percent of total votes.
