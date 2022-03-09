# Election_Analysis

## Project Overview
A Colrado Board of Elections employee has given me the follwing tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of he election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: 3.6.7, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham: recieved 23.0% of the vote.
  - Diana DeGette: recieved 73.8% of the vote.
  - Raymon Anthony Doane: recieved 3.1% of the vote.
- The winner of the election was:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%
 
## Challenge Overview
A Colrado Board of Elections employee has given me the follwing tasks to complete the election audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of he election based on popular vote.
6. Determine the voter turnout for each county
7. Calculate the percentage of votes from each county
8. Determine the county with the highest voter turnout

## Challenge Results
The analysis of the election results show that:
- There were 369,711 votes cast in the election. 
- The county results are:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- Denver had the largest voter turnout
- The candidate results are:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election is:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%

## Challenge Summary
Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This code was very helpful in analyzing the election results. The script is able to go through each row and pull out the data we need not only to do calculations, but also create a text file with the summary of the results. 

### Walkthrough of the Script
To begin, I imported 2 dependencies, the csv and os mods. Essentialls, someone else has written script that helps make our code quicker, more efficient, and easier to write! The csv module allows us to read in data from a .csv file that holds the election results. The os module allows us to access files from different operating systems and has other functions that essentially make it easier for us put the file into the folder of our choice. Below is the start of our script:

![CodeBlock1](https://github.com/rmward17/Election_Analysis/blob/main/Resources/CodeBlock1.png)

Next, I intialized variables, lists, and dictionaries that I planned to use throughout the analysis to answer all of the Election Board questions. Luckily, in python it is as easy as typing the name of the variable, list, or dictionary and then assigning the corresponding value or function. For example, the code to create the list and dictionary for the county voter analysis is below:

    # Create a county list and county votes dictionary.
    county_list = [] # We created this empty list to hold our county nme data
    county_votes = {} # We created this empty dictionary to hold the names of the counties as keys and the number of votes for each county as the value.
    
After reading in teh csv file, we can get to work! I used a for loop to go through each
  
What is nice about this code is that you can modify the variable names and csv file but use the same structure to get this information for a larger data set that contains many more counties and candidates. 

