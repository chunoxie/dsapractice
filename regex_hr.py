import re

lst=[]
for a0 in range(int(input("Enter how many records to input: "))):
    firstName, emailID = [str(s) for s in input("Enter name email address: ").split()]
    if re.search('@gmail\.com$', emailID):
   	    lst.append(firstName)
print(*sorted(lst), sep='\n')

names = []
N = int(input().strip())
for a0 in range(N):
    firstName, emailID = input().strip().split(' ')
    if '@gmail.com' in emailID:
        names.append(firstName)
print(*sorted(names), sep='\n')