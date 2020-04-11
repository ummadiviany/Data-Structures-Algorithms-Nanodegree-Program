"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

timeSpentOnPhone=dict()

'''for call in calls:
	if call[0] not in timeSpentOnPhone:
		timeSpentOnPhone[call[0]]=int(call[3])
	# Update two if statements with if-else statements
	# Thank for the review
	else:
		timeSpentOnPhone[call[0]]+=int(call[3])
	if call[1] not in timeSpentOnPhone:
	# Update two if statements with if-else statements
		timeSpentOnPhone[call[1]]=int(call[3])
	else:
		timeSpentOnPhone[call[1]]+=int(call[3])'''

for call in calls:
    timeSpentOnPhone[call[0]] = timeSpentOnPhone.get(call[0], 0) + int(call[3])
    timeSpentOnPhone[call[1]] = timeSpentOnPhone.get(call[1], 0) + int(call[3])
number=max(timeSpentOnPhone,key=timeSpentOnPhone.get)

print("%s spent the longest time, %d seconds, on the phone during September 2016."%(number,int(timeSpentOnPhone[number])))
#print(max(timeSpentOnPhone))
#print(sorted(timeSpentOnPhone,key=timeSpentOnPhone.get,reverse=True)[0])
