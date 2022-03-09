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
# Must initialize variables, lists, and dictionaries outside of opening the file 
total_votes = 0

# candidate options
candidate_options = []

# candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
           # dictionary_name[key] = value 
           candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1

# Determine percentage of votes for each candidate by looping thorugh the counts
# Iterate through the candidate options list to get each name
# for each key in the dictionary
for candidate_name in candidate_votes:
# use the for loop variable ot retrieve the votes of the candidate from the votes dictionary
# assign a variable to the dictionary values
  votes = candidate_votes[candidate_name]
# Calculate the percentage of the vote count for each candidate
  vote_percentage = float(votes) / float(total_votes) * 100
  print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  if (votes > winning_count) and (vote_percentage > winning_percentage):
    # If true then set winning_count = votes and winning_percent =
    # vote_percentage.
    winning_count = votes
    winning_percentage = vote_percentage
    # And, set the winning_candidate equal to the candidate's name.
    winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# print the percentages for each of the candidates
# print ( "key: recieved {calculated value}% of the vote.")
# print(f"{candidate_name}: recieved {vote_percentage:.1f}% of the vote.")
# Print the total votes
# print(total_votes)

# Print the candidate list
# print(candidate_options)

# print the candiate votes dictionary
# print(candidate_votes)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file
    txt_file.write("Counties in the Election\n---------------------------\nArapahoe\nDenver\nJefferson")
