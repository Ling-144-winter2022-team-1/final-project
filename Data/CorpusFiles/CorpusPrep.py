##           ---Removing Unnecessary Information---

import pandas as pd


##                        ~Titles~
print("\n TITLES \n")

#  read_csv
titles_data = pd.read_csv('rough_titles.csv',encoding='ISO-8859-1',names = ['MovieID','MovieTitle', 'Year','IMDB rating','IMDB votes','Genres'])

print("Original 'rough_titles.csv' data: \n")
print(titles_data)

#  Delete columns
titles_data.drop(['MovieTitle','IMDB rating','IMDB votes'], inplace=True, axis=1)

print("\n titles data after deleting unnnecessary columns\n")
print(titles_data)
titles_data.to_csv('titles.csv')


##                      ~Characters~
print("\n CHARACTERS \n")
#  Remvoving columns:
#  read_csv
character_data = pd.read_csv('rough_characters.csv',encoding='ISO-8859-1',names = ['CharacterID','CharacterName','MovieID','MovieTitle','Gender','Credit'])

print("Original 'rough_characters.csv' CSV data: \n")
print(character_data)

#  Delete columns
character_data.drop(['CharacterName','MovieTitle','Credit'], inplace=True, axis=1)

print("\n Character data after deleting unnnecessary columns\n")
print(character_data)
character_data.to_csv('characters.csv')


#  Characters with Gender set to '?':
#  read_csv
Gender_data = pd.read_csv('characters.csv', index_col ='Gender')

# retrieving rows by loc method
unkown_gender = Gender_data.loc['?']

print("\n Unknown Gender Data\n")
print(unkown_gender)

##                    ~Conversations~
print("\n CONVERSATIONS \n")
#  read_csv
conversations_data = pd.read_csv('conversations.csv',encoding='ISO-8859-1',names = ['Ch1','Ch2', 'MovieID','LineIDs'])

print("'conversations.csv'data: \n")
print(conversations_data)
conversations_data.to_csv('conversations.csv')


#                        ~Lines~
print("\n TITLES \n")

#  read_csv
lines_data = pd.read_csv('rough_lines.csv',encoding='ISO-8859-1',names = ['LineID','CharacterID', 'MovieID','CharacterName','line'])

print("Original 'rough_lines.csv' data: \n")
print(lines_data)

#  Delete columns
lines_data.drop('CharacterName', inplace=True, axis=1)

print("\n lines data after deleting unnnecessary columns\n")
print(lines_data)
lines_data.to_csv('lines.csv')