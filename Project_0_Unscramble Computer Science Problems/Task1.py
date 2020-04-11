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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
up=set()  #updated list with set

for text in texts:
	up.add(text[0])
	up.add(text[1])
for call in calls:
	up.add(call[0])
	up.add(call[1])
print("There are %d different telephone numbers in the records."%(len(up)))


'''for text in texts:
	if text[0] not in up:
		up.append(text[0])
	if text[1] not in up:
		up.append(text[1])
for call in calls:
	if call[0] not in up:
		up.append(call[0])
	if call[1] not in up:
		up.append(call[1])'''


