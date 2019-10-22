counties = ["Arapahoe","Denver","Jefferson"]
counties_tuple = ("Arapahoe","Denver","Jefferson")
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

""" if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.") """
""" if "Arapahoe" and "Denver" in counties:
    print("Arapahoe and Denver are in the list of counties.")
else:
    print("Arapahoe or Denver is not the list of counties.") """

""" if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")
 """
""" for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num) """

""" for num in range(5):
    print(num) """

for i in range(len(counties)):
    print(counties[i])
for county, voters in counties_dict.items():
    print(f'{county} county has, {voters} registered voters')

""" for county in counties_dict.keys():
    print(county) """

""" for county in counties_dict.keys():
    print(county) """

""" for county in counties_dict:
    print(counties_dict[county]) """

""" for county in counties_dict:
    print(counties_dict.get(county)) """


print('------------Concatenation method one--------------------')
for county, voters in counties_dict.items():
    print(county+' county has,', str(voters)+' registered voters')

print('------------Concatenation method using f string--------------------')
for county, voters in counties_dict.items():
    print(f'{county} county has, {voters} registered voters')

print('------------method using multi-line f string--------------------')
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)

print('------------method using multi-line f string with decimal format (##:.2f))--------------------')
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)

print('------------getting data from multiple dicts--------------------')
print('------------print using loop--------------------')
for county_dict in voting_data:
    print(county_dict)
    
print('------------print using range--------------------')
for i in range(len(voting_data)):
      print(voting_data[i])

print('------------only printing county names--------------------')
for county_dict in voting_data:
    print(county_dict['county'])

