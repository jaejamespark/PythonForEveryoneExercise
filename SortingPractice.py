
#print(parse_substring("I am a student", "am"))
#print(parse_substring("I am a student", "student"))

from random import randint

slist = []
for x in range(100):
    slist.append((randint(0, 100)))
print(slist)

#list = [3, 1, 6, 0, 5]

#[3, 1, 6, 0 5]
#3 1 6 0 5
#1 3 6 0 5
#0 3 6 1 5
#0 1 6 3 5
#0 1 3 6 5
#0 1 3 5 6

k = 1
for i in range(len(slist)):
    for j in range(len(slist)-k):
        if slist[i] > slist[j+k]:
            temp = slist[i]
            slist[i] = slist[j+k]
            slist[j+k] = temp
    k = k + 1

print(slist)
    
    
    #print(i)