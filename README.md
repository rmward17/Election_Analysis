# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the follwing tasks to complete the election audit of a recent local congressional election:

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
This code was very helpful in analyzing the election results. The script is able to go through each row and pull out the data we need not only to do calculations, but also create a text file with the summary of the election analysis. 

### Walkthrough of the Script
To begin, I imported 2 dependencies, the csv and os modules. Essentially, someone else has written script that helps make our code quicker, more efficient, and easier to write! The csv module allows us to read in data from a .csv file that holds the election results. The os module allows us to access files from different operating systems and has other functions that essentially make it easier for us put the file into the folder of our choice. Below is the start of our script:

![CodeBlock1](https://github.com/rmward17/Election_Analysis/blob/main/Resources/CodeBlock1.png)

Next, I intialized variables, lists, and dictionaries to use throughout the analysis to answer all of the Board's questions. Luckily, in python it is as easy as typing the name of the variable, list, or dictionary and then assigning the corresponding value or function. For example, the code to create the list and dictionary for the county voter analysis is below:

    # Create a county list and county votes dictionary.
    county_list = [] # We created this empty list to hold our county nme data
    county_votes = {} # We created this empty dictionary to hold the names of the counties as keys and the number of votes for each county as the value.

I did the same to track the candidates and the votes by cadidate as well.

After reading in the csv file, I can get to work! I used a for loop to go through each row in the file and pull out the candidate and county from each row. Then, using if statements, I added the unique counties and candidates to the empty lists we created, tallied the votes per candidate and per county, and aadded those values to the dictionaries. Those if statments in the screenshots below:

![CodeBlock2](https://github.com/rmward17/Election_Analysis/blob/main/Resources/CodeBlock2.png)

Now, all we had to do was calculate the percentages, the winning candidate information, and county information. I also did that with for loops and if statements to check the total number of votes for each candidate and county against the "current" winning candidate and couunty so that the candidate and county with the highest number of voters and percentages of voters get assgined as the winning candidate and largest county. After running that analysis, the os module from earlier allows us to write output to a file. In this case, I chose a txt.file to hold our results. This is what that output in the txt.file looks like:

![Election Analysis](https://github.com/rmward17/Election_Analysis/blob/main/Resources/Election_analysis_screenshot.png)

### Summary
As you can see our code answered all of the Election Board questions easily, it was quite straightforward, and I made sure to comment throughout so that it was easy to follow and understand. Luckily, this code is for the Election Board to keep and reuse. The csv file only had the columns "Ballot ID","County", and "Candidate". If a new csv file is read into the code that has those 3 columns or rows are added to the current csv file, you can run this code as is and it will add the new candidates and counties to the lists and dictionaries we have created and rerun the calculations to determine the winner. You can also modify this code to do additional analysis on the current file as well! You can rewrite it to determine the winning candidates within each county or vice-versa. If we had the total population of each county, you can modify the code to determine how many people in the county voted or didn't vote. You can also use this code on different elections for the same district to see the change in how people are voting and do a comparison by adding a column the csv file to denote what year the election data is from and oragnize your results that way.

All in all, there are many uses for this code and I am glad I was able to create it for the Board of Elections.

