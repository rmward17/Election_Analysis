# the data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of the candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candiate won
# 5. The winner of the election based on popular vote

import os
import csv
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources",'election_results.csv')

# Initialize a total vote counter
total_votes = 0

# candidate options
candidate_options = []

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: read and analyze data here
     # Read the file object with the reader function
     file_reader = csv.reader(election_data)
     # print the header rows
     headers = next(file_reader)
     
     # print each row in the CSV file
     for row in file_reader:
          # Add to the total vote vount
         total_votes += 1
          # Pull the candidate name from each row
         candidate_name = row[2]
         # If the candidate does not match any existing candidate...
         if candidate_name not in candidate_options:
           # Add it to the list of candidates
           candidate_options.append(candidate_name)

        
# Print the total votes
print(total_votes)

# Print the candidate list
print(candidate_options)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
