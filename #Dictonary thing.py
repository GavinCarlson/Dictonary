#Dictonary thing

Names = {'Steve': 99, 'Larry': 78, 'Gavin': 0, 'joe': 45, 'iguana': 88}
print(Names)
Names['Sam'] = 78
Names['Marrie'] = 92
Names['Ria'] = 88
print(len(Names))

for x in Names.values():
    print(x)

import statistics 
def Mean(Names):
    list_avg = statistics.mean(Names)
    return(list_avg)

