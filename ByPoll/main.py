# Creating and reading CSV file
import os
import csv

# Declaring the location of the CSV file
election_data_csv = os.path.join("..", "Resources", "election_data.csv")

# creating a list for candidates that were voted for
candidates = []

# opening csv file
with open(election_data_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Defining the header row so we can skip the header when iterating through the data
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # linking the rows to their corresponding lists
    for row in csvreader:
        candidates.append(row[2])

# Calculating the total number of votes for all candidates
total_votes = len(candidates)
# print(total_votes)

# Creating a dictionary to store candidate names with their vote counts
candidate_list = {}

# Iterating through the candidates
# Checks candidates are in the list, they are added to the dictionary
# If not they are added, also adding 1 count to the votes when looping through the row
for candidate in candidates:
    if candidate in candidate_list:
        candidate_list[candidate] += 1
    else:
        candidate_list[candidate] = 1
# print(candidate_list)

# Using the dictionary that was created, calculating the percentage with respect to the name and vote count from the dictionary
candidate_percentages = {name: (votes / total_votes) * 100 for name, votes in candidate_list.items()}
# print(candidate_percentages)

# Finding the most number of votes and using key to name the corresponding candidate
winner = max(candidate_list, key=candidate_list.get)
# print(winner)

# Printing the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_list.items():
    percentage = candidate_percentages[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Decaring a location to export and store results as a text file
election_data_csv = os.path.join("..", "analysis", "PyPoll_analysis.txt")
with open(election_data_csv, "w") as text_file:

    text_file.write("\n")
    text_file.write("Election Results")
    text_file.write("\n\n")
    text_file.write("-------------------------")
    text_file.write("\n\n")
    text_file.write(f"Total Votes: {total_votes}")
    text_file.write("\n\n")
    text_file.write("-------------------------")
    text_file.write("\n\n")
    for candidate, votes in candidate_list.items():
        percentage = candidate_percentages[candidate]
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})")
        text_file.write("\n\n")
    text_file.write("-------------------------")
    text_file.write("\n\n")
    text_file.write(f"Winner: {winner}")
    text_file.write("\n\n")
    text_file.write("-------------------------")