import pandas as pd

#  Lines containing characters with gender set to '?':
#  read_csv
Gender_data = pd.read_csv('characters.csv', index_col ='Gender')

# retrieving rows by loc method
unkown_gender = Gender_data.loc['?']

print("\n Unknown Gender Data\n")
print(unkown_gender)