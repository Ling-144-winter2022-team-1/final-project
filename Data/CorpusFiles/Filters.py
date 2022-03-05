import pandas as pd

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
unkown_gender = Gender_data.loc[['f','F']]

print("\n Unknown Gender Data\n")
print(unkown_gender)
unkown_gender.to_csv('female_characters.csv')

for genders in female_characters.csv:
  