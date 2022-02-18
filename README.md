# final-project

## Team Members: <Isabella Polena, Claire Cruse, Percy Garcia>

This project is a filtering program based on the Bechdel test (Alison Bechdel).

### Current files:

README file

Project Outline file

References folder

Data folder

BASICS
The Bechdel Test has 3 criteria:

The film must have at least two women in it

The women in the film talk to each other

The women talk to each other about something other than a man

What we have:

movie_titles_metadata.txt

contains information about each movie title
fields:
movieID,
movie title,
movie year,
IMDB rating,
no. IMDB votes,
genres in the format ['genre1','genre2',…,'genreN']
movie_characters_metadata.txt

contains information about each movie character
fields:
characterID
character name
movieID
movie title
gender ("?" for unlabeled cases)
position in credits ("?" for unlabeled cases)
movie_lines.txt

contains the actual text of each utterance
fields:
lineID
characterID (who uttered this phrase)
movieID
character name
text of the utterance
movie_conversations.txt

the structure of the conversations
fields
characterID of the first character involved in the conversation
characterID of the second character involved in the conversation
movieID of the movie in which the conversation occurred
list of the utterances that make the conversation, in chronological
order: ['lineID1','lineID2',…,'lineIDN']
has to be matched with movie_lines.txt to reconstruct the actual content
raw_script_urls.txt

the urls from which the raw sources were retrieved

1. Streamline Data

Create a single organized file out of the data

Because of the size of the files, I think the way to do it might be to individually convert them to csv format, remove unnecessary categories, then figure out a way to merge them...

the first order of business should probably be to decide what data we don't/do need.

2. Filter out films that don't meet criterion 1

Use character gender metadata

Decide how to categorize unlabeled cases in metadata

3. Filter out films that don't meet criterion 2

From Kelsey: "what counts as a conversation between 2 women? Can it just be Person A speaks once, and person B speaks once? Or does there need to be a back and forth?"

a conversation between 2 women would be that they each at least say one line to each other. One back and forth is all that is necessary.

From Kelsey: "Once you figure out which characters are female, and which are male, how are you going to programatically pull out only the lines where female characters speak to each other?"

the data identifies when a conversation is between a man (m), woman (f), and when it doesn't know (?). We can find a way in replit to delete all of the conversations that have (m). we can use regex similar to update one to complete this

4. Filter out films that don't meet criterion 3

From Kelsey:"How will you determine what counts as talking about a man? What features of a sentence/conversation will you use to filter out these elements?"

We could set up a filter based on the data in the 'men' category of the gender metadata and try to filter by men's names used in the conversations between women

5. How many films 'pass'?

Determine how many films pass each criterion and compare it to the original total.
