# Author: Dillon de Silva

passed_x_coordinates = tuple()
passed_y_coordinates = tuple()

results_data = {}

eeg_results = open("eeg-data/eeg-results.txt")
for line in eeg_results:
  index, sf, uxf, uyf, bf = line.split()
  results_data[index] = [sf, uxf, uyf, bf]

print(results_data)