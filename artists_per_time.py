#find most common artists for each amount spent listening then test on spotify to get ranking
#see if those who listen more often are generally listening to artists that are less popular
'''method: get all artists for each listening period
then try/except them into dictionary sort by most frequent'''
#Check to see what percentage of each time group artists are ranked on spotify
#Interested in seeing if the people who listen more listen to lower ranked artists
import csv
from collections import Counter

def reader():
    
    plz = open('cleaned_survey.csv')
    fp = csv.DictReader(plz, delimiter=',')
    return(fp)


def ugh(reader):
    time_periods = []
    for row in reader:
        time_period = (row["How often do you use a music streaming service?(Hours a day)"])
        if time_period not in time_periods:
            time_periods.append(time_period)
    return(time_periods)
    
def step2(reader, time_periods):
    md = {}
    end = (len(time_periods))
    for row in reader:
        time_period = (row["How often do you use a music streaming service?(Hours a day)"])
        artists = (row["What are the top 3 artists you listen to? (Please list them in order from most to least.)"])
        artists = artists.lower()
        for i in range(0,end):
            if time_period == time_periods[i]:
                try:
                    md[time_period] += artists
                except KeyError as e:
                    md[time_period] = artists
    return(md)
    
def make_list(dictionary):
    for k,v in md.items():
        help1 = v.split(",")
        answer = Counter(help1)
        print(k)
        print(answer)

    
fp = reader()
time = (ugh(fp))
fp = reader()
md = (step2(fp,time))
print(md)
make_list(md)