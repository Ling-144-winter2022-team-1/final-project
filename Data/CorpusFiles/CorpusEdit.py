##           ---Removing Unnecessary Information---

import pandas as pd
#import re

##                        ~Titles~
#  read_csv
titles_data = pd.read_csv('rough_titles.csv',encoding='ISO-8859-1',names = ['MovieID','MovieTitle', 'Year','IMDB rating','IMDB votes','Genres'])

print("Original 'rough_titles.csv' CSV data: \n")
print(titles_data)

#  Delete columns
titles_data.drop(['MovieTitle','IMDB rating','IMDB votes'], inplace=True, axis=1)

print("\n titles data after deleting unnnecessary columns\n")
print(titles_data)
titles_data.to_csv('titles.csv')

##                      ~Characters~

#  read_csv
character_data = pd.read_csv('rough_characters.csv',encoding='ISO-8859-1',names = ['CharacterID','CharacterName','MovieID','MovieTitle','Gender','Credit'])

print("Original 'rough_characters.csv' CSV data: \n")
print(character_data)

#  Delete columns
character_data.drop(['CharacterName','MovieTitle','Credit'], inplace=True, axis=1)

print("\nCSV Data after deleting unnnecessary columns\n")
print(character_data)
#character_data.to_csv('characters.csv')

#  Remove unspecified data (Gender '?')

##                    ~Conversations~
#  read_csv
conversations_data = pd.read_csv('conversations.csv',encoding='ISO-8859-1',names = ['Ch1','Ch2', 'MovieID','LineIDs'])

print("'conversations.csv'data: \n")
print(conversations_data)
conversations_data.to_csv('conversations.csv')