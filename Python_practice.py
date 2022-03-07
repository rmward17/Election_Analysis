#starting code
print("Hello World")

# practing if statments in python with counties list
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# creates an index error
#if counties[3] != 'Jefferson':
    #print(counties[2])

# practicing if-else statments in python

temperature = int(input("What is the remperature ouside?"))

if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows.")

# Nested If-Else

score = int(input("What is your test score?"))

if score >= 90:
   print("Your grade is an A.")
else:
    if score >= 80:
       print("Your grade is a B.")
    else: 
        if score >= 70:
            print("Your score is a C.")
        else:
            if score >= 60:
                print("Your grade is a D.")
            else:
                print("Your grade is an F")

# using if-elif-else
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# Membership operators
counties = ["Arapahoe","Denver","Jefferson"]

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# combo of memebership and logic operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#combo continued
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# Loops

# condition-controlled loop aka a while loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

# count-controlled loop aka a for loop
for county in counties:
    print(county)

numbers = [0,1,2,3,4]

for num in numbers:
    print(num)

for num in range(5):
    print(num)

# using range() funciton
for i in range(len(counties)):
    print(counties[i])

#iterating through a dictionary

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

#produces same output as above but 
for county in counties_dict.keys():
    print(county) 

#get values
for voters in counties_dict.values():
    print(voters)

#both also prodcues values
for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# get key-value pairs we use the .items() fucntion
# when iterating over a dictionary, the first variable is assigned to the keys and the second is assigned to the values

for county, voters in counties_dict.items():
    print(str(county) + " couny has " + str(voters) + " registered voters.")

# getting each dictionary in a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])
    print(voting_data[i]['county'])
    print(voting_data[i]['registered_voters'])

# getting values froma  list of dictionaries - nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county_dict in voting_data:
    print(county_dict['registered_voters'])


# formatting prints
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

# multiple f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes:,} number of votes. "
f"The total number of votes in the election was {total_votes:,}. "
f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

for i in range(len(voting_data)):
    #print(voting_data[i])
    #print(voting_data[i]['county'])
    #print(voting_data[i]['registered_voters'])
    print(f"{voting_data[i]['county']} county has {voting_data[i]['registered_voters']:,} registered voters")