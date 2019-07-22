import csv
from collections import Counter
 
with open('cleaned_survey.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    list1,list2,list3,list4,list5 = (list(),list(),list(),list(),list())
    genres = ('0 - 30 minutes','30 - 60 minutes','1 - 2 hours','2 - 4 hours','5 or more hours')
    artists_dict = {}
    blank = 0
    new_list = list()
    for row in reader:
        artists = (row["What are the top 3 artists you listen to? (Please list them in order from most to least.)"])
        artists_split = artists.split(",")
        artist = artists_split[0].lower()
        artist = artist.strip()
        
        try:
            artist1 = artists_split[1].lower()
            artist1 = artist1.strip()
            artist2 = artists_split[2].lower()
            artist2 = artist2.strip()
        except IndexError as e:
            continue

        new_list.append(artist)
        new_list.append(artist1)
        new_list.append(artist2)
        
for item in new_list:
    try:
        artists_dict[item] += 1
    except KeyError as e:
        artists_dict[item] = 1
save=(sorted(artists_dict.items(), key=lambda x: x[1], reverse=True))
print("Top 10 artists and number of people who listed them")
for i in range(0,11):
    print(save[i])


        
    

          #ignoring blank entries




        #uppercase_artists = row["What are the top 3 artists you listen to? (Please list them in order from most to least.)"]
        #artists = list(uppercase_artists.lower())
        #if artists in "abcdefghijklmnopqrstuvwxyz":
         #   print("null")
        #else:
         #   print("entry")