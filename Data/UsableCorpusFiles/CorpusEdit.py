##           ---Removing Unnecessary Information---

import pandas as pd
#import re

##                      ~Titles~
#  read_csv
titles_data = pd.read_csv('titles_v4.csv',encoding='ISO-8859-1',names = ['MovieID','MovieTitle', 'Year','IMDB rating','IMDB votes','Genres'])

print("Original 'titles_v4.csv' CSV data: \n")
print(titles_data)

#  Delete rows or columns from the CSV files
titles_data.drop(['MovieTitle','IMDB votes'], inplace=True, axis=1)

print("\n titles data after deleting unnnecessary columns\n")
print(titles_data)
titles_data.to_csv('titles.csv')

##                      ~Characters~

#  read_csv
character_data = pd.read_csv('characters_v4.csv',encoding='ISO-8859-1',names = ['CharacterID','CharacterName','MovieID','MovieTitle','Gender','Credit'])

print("Original 'character_data_v4.csv' CSV data: \n")
print(character_data)

#  Delete rows or columns from the CSV files
character_data.drop(['CharacterName','MovieTitle','Credit'], inplace=True, axis=1)

print("\nCSV Data after deleting unnnecessary columns\n")
print(character_data)
character_data.to_csv('characters.csv')



