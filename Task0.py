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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

""" 
text first record
"""
first_record_text = texts[0]
text_incoming_number = first_record_text[0]
text_answering_number = first_record_text[1]
text_time = first_record_text[2]

print("First record of texts, {} texts {} at time {}"\
    .format(text_incoming_number,text_answering_number,text_time))




""" 
calls last record
"""


last_record_calls = calls[-1]
call_incoming_number = last_record_calls[0]
call_answering_number = last_record_calls[1]
call_time = last_record_calls[2]
call_duration = last_record_calls[3]

print("Last record of calls, {} calls {} at time {}, lasting {} seconds"\
    .format(call_incoming_number,call_answering_number,call_time,call_duration))