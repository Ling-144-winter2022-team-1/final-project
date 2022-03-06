import pandas as pd
import csv

#       Removing lines containing characters with gender set to                                             '?'
#  read_csv
Gender_data = pd.read_csv("characters.csv", index_col ="Gender")

# retrieving rows by loc method
unkown_gender = Gender_data.loc[['m','M','f','F']]

print("\n Unknown Gender Data\n")
print(unkown_gender)
unkown_gender.to_csv('all_characters.csv')

#       Removing lines containing characters with gender set to                                         'M' and 'm'
#  read_csv
Gender_data = pd.read_csv("characters.csv", index_col ="Gender")

# retrieving rows by loc method
female_gender = Gender_data.loc[['f','F']]

print("\n Female Gender Data\n")
print(female_gender)
female_gender.to_csv('female_characters.csv')

#         Isolating female character IDs

# reading CSV file
female_characters_data = pd.read_csv("female_characters.csv")

print("\n Female characters data \n")
print(female_characters_data)

# converting column data to list
ChID = female_characters_data['CharacterID'].tolist()

#print("\n Female Character IDs\n")
#print('CharacterID:', ChID)

textfile = open("femaleID_list.txt", "w")
for element in ChID:
    textfile.write(element + "\n")
textfile.close()

#print("\n femaleID_list. txt file\n")

#          Using character IDs to filter