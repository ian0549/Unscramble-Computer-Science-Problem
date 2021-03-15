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


dictionary = {}



def sum_time_spent(dictionary,incoming_number, duration):
    """calculate total time spent for each telephone number"""

    dictionary[incoming_number] = dictionary.get(incoming_number, 0) + int(duration)

    return dictionary



for record in calls:
    incoming_number = record[0]
    answering_number = record[1]
    time = record[2]
    duration = record[3]

    dictionary = sum_time_spent(dictionary,incoming_number,duration)
    dictionary = sum_time_spent(dictionary,answering_number,duration)



phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))

print("{} spent the longest time, {} seconds, on the phone during September 2016."\
        .format(phoneMax[0],phoneMax[1]))