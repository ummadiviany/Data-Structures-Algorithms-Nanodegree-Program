"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

numbers=[]
telenum=[]
for text,call in zip(texts,calls):
	numbers.append(text[0])
	numbers.append(text[1])
	numbers.append(call[1])
	if call[0].startswith("140"):
		telenum.append(call[0])

for call in calls:
	if call[0] not in numbers:
		telenum.append(call[0])
telenum.sort()
#print(len(numbers))
#print(len(telenum))
print("These numbers could be telemarketers: ")
print(*telenum,sep="\n")


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

