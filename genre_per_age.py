import csv
from collections import Counter
 
with open('finalnotfixed.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    female,male,counter,female_dict,male_dict = [],[],0,{},{}
    genres = ('0 - 30 minutes','30 - 60 minutes','1 - 2 hours','2 - 4 hours','5 or more hours')
    for row in reader:
        counter += 1
        gender = (row["What is your gender?"])
        num_of_genres = (row["How many genres do you listen to?"])
        if gender == "Female":
            female.append(num_of_genres)
        if gender == "Male":
            male.append(num_of_genres)
    for item in female:
        try:
            female_dict[item] += 1
        except KeyError as e: 
            female_dict[item] = 1
            
    for item in male:
        try:
            male_dict[item] += 1
        except KeyError as e:
            male_dict[item] = 1
    
female_ordered=(sorted(female_dict.items(), key=lambda x: x[1], reverse=True))
male_ordered=(sorted(male_dict.items(), key=lambda x: x[1], reverse=True))

print('Number of genres listened to by females')
for i in range(0,10):
    print(female_ordered[i])
print('Number of genres listened to by males')
for i in range(0,8):
    print(male_ordered[i])

    
