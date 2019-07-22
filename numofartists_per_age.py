import csv
from collections import Counter
 
with open('finalnotfixed.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    list1,list2,list3,list4,list5 = (list(),list(),list(),list(),list())
    genres = ('0 - 30 minutes','30 - 60 minutes','1 - 2 hours','2 - 4 hours','5 or more hours')
    for row in reader:
        frequency = (row["How often do you use a music streaming service?(Hours a day)"])
        num_of_artists = (row["How many artists do you listen to?"])
        if frequency == '0 - 30 minutes':
            list1.append(int(num_of_artists))
        if frequency == '30 - 60 minutes':
            list2.append(int(num_of_artists))
        if frequency == '1 - 2 hours':
            list3.append(int(num_of_artists))
        if frequency == '2 - 4 hours':
            try:
                list4.append(int(num_of_artists))
            except ValueError as e:
                list4.append(int(0))
        if frequency == '5 or more hours':
            list5.append(int(num_of_artists))
    print(list1)
    print()
    print(list2)
    print()
    print(list3)
    print()
    print(list4)
    a = Counter(list1).most_common(1)
    b = Counter(list2).most_common(1)
    c = Counter(list3).most_common(1)
    d = Counter(list4).most_common(1)
    e = Counter(list5).most_common(1)
   
    maybe = (a,b,c,d,e)
  
    for i in range (0,5):
        genre_tuple = list(maybe[i])
        genre_list = (genre_tuple[0])
        print("Most common number of genres for those who use streaming services", genres[i], "a day")
        print(genre_list[0])
        
        

