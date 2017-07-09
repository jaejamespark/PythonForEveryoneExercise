handle = open('mbox-short.txt')
hours = list()
hour_dict = dict()
hours_list = list()


for line in handle:
    if line.startswith('From '):
        word = line.split()
        time = word[5]
        time_elements = time.split(':')
        hours.append(time_elements[0])
        
        
#print(hours)       
for hour in hours:
    hour_dict[hour] = hour_dict.get(hour, 0) + 1
                    
#print(hour_dict)

for k, v in hour_dict.items():
    newtup = (k, v)
    hours_list.append(newtup)
        
hours_list = sorted(hours_list)

#print(hours_list)

for k, v in hours_list:
    print(k, v)


# Sort by value practice
#for k, v in hour_dict.items():
#    hour_tup = (v, k)
#    hours_list.append(hour_tup)
    
#hours_list = sorted(hours_list)

#print(hours_list)


        