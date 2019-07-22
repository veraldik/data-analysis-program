import csv
from collections import Counter

def reader():
    
    plz = open('finalnotfixed.csv')
    fp = csv.DictReader(plz, delimiter=',')
    return(fp)


def ugh(reader):
    ages = []
    for row in reader:
        age = (row["What is your age? "])
        if age not in ages:
            ages.append(age)
    return(ages)
    
def artists(reader, ages):
    md = {}
    end = (len(ages))
    for row in reader:
        age = (row["What is your age? "])
        artists = (row["How many artists do you listen to?"])
        artists = list(artists)
        print(artists)
        for i in range(0,end):
            if age == ages[i]:
                try:
                    md[age] += artists
                except KeyError as e:
                    md[age] = artists
    return(md)
    

    


fp = reader()
hi = (ugh(fp))
fp = reader()
md = artists(fp,hi)
print("Most common number of artists listened to by age group")
print(md)