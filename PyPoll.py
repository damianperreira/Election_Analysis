# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import random
import numpy
import os

""" # Import the datetime dependency.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is,", now) """


""" with open('Resources/election_results.csv','r') as election_data:
    csv_reader = csv.reader(election_data)

    for line in csv_reader:
        print(line)

election_data.close()
 """

""" # Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources","election_results.csv")

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data) """

""" # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
outfile = open(file_to_save, "w")

# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close() """

""" # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")
 """


# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

