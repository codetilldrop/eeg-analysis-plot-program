# Author: Dillon de Silva

def fetch_coordinates():
  # This is a stub

passed_x_coordinates = tuple()
passed_y_coordinates = tuple()

results_data = {}

# Deals with storing the data from the results.txt file
eeg_results = open("eeg-data/eeg-results.txt")
for line in eeg_results:
 index, sf, uxf, uyf, bf = line.split(',')

 # Setting our variables to integer data types
 index = int(index)
 sf = int(sf)
 uxf = int(uxf)
 uyf = int(uyf)
 bf = int(bf)
 
 results_data[index] = [sf, uxf, uyf, bf]

coordinates = []

# Finding out whether Non-Linear Independence
# signals for a pair of x, y signals passed
for record in results_data:
  if results_data[record][3] == 1:
    # This is a stub
    fetch_coordinates(results_data[record])
    print('Pass for non linear independence')
  else:
    print('Fail for non linear independence')