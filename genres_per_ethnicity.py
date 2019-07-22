import csv
from collections import Counter

def reader():
    
    plz = open('finalnotfixed.csv')
    fp = csv.DictReader(plz, delimiter=',')
    return(fp)


def ugh(reader):
    ethnicities = []
    for row in reader:
        ethnicity = (row["What is your ethnicity?"])
        if ethnicity not in ethnicities:
            ethnicities.append(ethnicity)
    return(ethnicities)
    
def genres(reader, ethnicities):
    md = {}
    end = (len(ethnicities))
    for row in reader:
        ethnicity = (row["What is your ethnicity?"])
        genres = list(row["How many genres do you listen to?"])
        for i in range(0,end):
            if ethnicity == ethnicities[i]:
                try:
                    md[ethnicity] += genres
                except KeyError as e:
                    md[ethnicity] = genres
    return(md)
    
def make_list(dictionary):
    value = list(md.values())
    key = list(md.keys())
    length = len(value)
    for i in range(0,length):
        answer = Counter(value[i])
        print(key[i])
        print(answer)
    


fp = reader()
hi = (ugh(fp))
fp = reader()
md = genres(fp,hi)
print("Most common number of genres listened to by each ethnicity")
(make_list(md))

