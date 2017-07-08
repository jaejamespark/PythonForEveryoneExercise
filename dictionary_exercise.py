name = input('enter file name: ')
handle = open(name)
email_list = list()
histo_email = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        email_list.append(words[1])
        
#print(email_list)

for email in email_list:
    histo_email[email] = histo_email.get(email, 0) + 1
    
#print(histo_email)

most_email = None
most_email_count = None

#print('xxxxx', histo_email.items())

for email, count in histo_email.items():
    if most_email_count == None:
        most_email_count = count
        most_email = email
    else:
        if most_email_count < count:
            most_email = email
            most_email_count = count
            
            
print(most_email, most_email_count)
    