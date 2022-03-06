import pandas as pd

female_characters_data = pd.read_csv("female_characters.csv")
female_movies = female_characters_data['MovieID'].tolist()
#print(female_movies)

# defining output list
multi_f_movies = [] 

# condition for reviewing every element
for females in female_movies:

	# checking the occurrence of elements
	n = female_movies.count(females)
	
	# if the occurrence is more than
	# one we add it to the output list
	if n > 1:		

		if multi_f_movies.count(females) == 0: # condition to check

			multi_f_movies.append(females)

print(multi_f_movies)

textfile = open("multi_female_movies.txt", "w")
for element in multi_f_movies:
    textfile.write(element + "\n")
textfile.close()