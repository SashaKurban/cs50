import csv
from sys import argv
# if user didn't input database and text to analyse, show error
if len(argv) < 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)
# create an empty list for STRs names and dictionary for people and their dna
people_dict = {}
STRs = []
# from database copy the names of STRs into an empty list
with open(argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        STRs = row
        STRs.remove('name')  # remove name from the list of STRs
        break
# count the number of STRs to be found
STRs_number = len(STRs)
# from database copy nams and corresponding dna into an empty dictionary
with open(argv[1], newline='') as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile)
    for row in reader:
        people_dict[row[0]] = row
        row.pop(0)  # remove firs row with names of STRs
# open a sequences file to analyse dna sample
with open(argv[2], 'r') as sample_file:
    sample = sample_file.read()
# create an empty list for dna data from sequences sample
dna_count = []
# iterate through dna sample to count each STRs repetition
for x in range(STRs_number):
    temp_value = 0  # temporary value of STRs repetition
    max_value = 0  # maximum value of STRs repetition
    start = 0
    end = len(sample)
    STR_len = len(STRs[x])
    while True:
        # if temporaty value is more than max, update max
        if temp_value > max_value:
            max_value = temp_value
        # find the begining of STRs repetition 
        sequence = sample.find(STRs[x], start, end)
        # if no STRs found, stop
        if sequence == -1:
            break
        # if next STR is not right after the one found, reset temp value and look further for repetition
        elif temp_value > 0 and not sequence == start:
            temp_value = 0
            start = sequence
        # if it is a first STR in a string, move by a length of STR and look for the next one
        else:
            temp_value += 1  # update the temp value
            start = sequence + STR_len 
    # add the found STRs values into a list for late analysys     
    dna_count.append(str(max_value))
# compare the list of STRs from sample with values in the given database
for name, dna in people_dict.items():
    if dna_count == dna:
        print(name)  # print name if an identical match found
        exit(1)
print("No match")  # if no match found