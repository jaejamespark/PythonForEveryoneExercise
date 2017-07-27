import re

handle = open('regex_sum_4571.txt')
numlist = list()
inumlist = list()

for line in handle:
     number = re.findall('[0-9]+', line)
     if number:     
        print(number)
        numlist.append(number)
    
    
for element in numlist:
    for num in element:
        num = int(num)
        inumlist.append(num)
        
    
print(inumlist)
print(sum(inumlist))



