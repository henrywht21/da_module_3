# Modules
import csv

# Set the File Path
file_path = "Resources/election_data.csv"

#initialize a dict to hold results
tally = {}

# Read the file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read Header Row
    csv_header = next(csvreader)

    print(f"File Header: {csv_header}")

    # Loop through file to tally votes
    for row in csvreader:
        candidate = row[2]

        if candidate in tally.keys():
            tally[candidate] += 1

        else:
            tally[candidate] = 1


    print("Election Results")
    print("----------------------")

    #Code section generated with assistance from Xpert AI
    #total of votes
    total_votes = sum(tally.values())
    print(f"Total Votes: {total_votes}")
    print("----------------------")

    for key, value in tally.items():
        percent_vote = value/total_votes
        print(f"{key}: {percent_vote:.3%} ({value})")

    print("----------------------")
    # Determine Winner
    winner = max(tally, key=tally.get)
    print(f"Winner: {winner}")
    print("----------------------")

# Write results to a text file
write_file = "analysis/pypoll_output.txt"

with open(write_file, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------\n")
    
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------\n")

    for key, value in tally.items():
        percent_vote = value/total_votes
        file.write(f"{key}: {percent_vote:.3%} ({value})\n")

    file.write("----------------------\n")
    # Determine Winner
    winner = max(tally, key=tally.get)
    file.write(f"Winner: {winner}\n")
    file.write("----------------------\n")
    



