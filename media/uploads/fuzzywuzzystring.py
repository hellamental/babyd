import pandas as pd
import csv
from fuzzywuzzy import fuzz

df = pd.read_csv (r'testfzzy.csv')
df.head()

ans_desc = df['Ancillary Network Services'].to_list()
new_desc = df['*Description'].to_list()

#create new dictionary
matchup = []

#for loop to match services
for i in ans_desc:
    line = [i]
    for j in new_desc:
        ratio = fuzz.token_sort_ratio(str(i),str(j)) 
        if ratio > 60: 
            print(ratio,i,j)
            line.append(j)
        else:
            pass
    matchup.append(line)

print(matchup)

# opening the csv file in 'w+' mode
file = open('g4g.csv', 'w+', newline ='')

with file:    
    write = csv.writer(file)
    write.writerows(matchup)



    