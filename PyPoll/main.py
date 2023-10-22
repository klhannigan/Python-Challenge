import os
import csv
from pathlib import Path

csv_path = Path(r"C:\Users\Kylez\Desktop\Python-Challenge\PyPoll\Resources\election_data.csv")

total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0

with open(csv_path, newline = "", encoding = "utf-8") as elections:
    csvreader = csv.reader(elections, delimiter = ",")
    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

        if row [2] == "Charles Casper Stockham":
            charles_votes = charles_votes + 1
        elif row [2] == "Diana DeGette":
            diana_votes = diana_votes + 1
        elif row [2] == "Raymon Anthony Doane":
            raymon_votes = raymon_votes + 1

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [charles_votes, diana_votes, raymon_votes]

dict_values = dict(zip(candidates, votes))
key = max(dict_values, key = dict_values.get)

charles_percent = (charles_votes / total_votes) * 100
diana_percent = (diana_votes / total_votes) * 100
raymon_percent = (raymon_votes / total_votes) * 100

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

export_file = os.path.join(r"C:\Users\Kylez\Desktop\Python-Challenge\PyPoll\Analysis\Election_Results.txt")
with open(export_file, "w") as txtfile:
    txtfile.write(f"Election Results")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f'Total Votes: {total_votes}')
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f'Charles Casper Stockham: {charles_percent: .3f}% ({charles_votes})')
    txtfile.write("\n")
    txtfile.write(f'Diana DeGette: {diana_percent: .3f}% ({diana_votes})')
    txtfile.write("\n")
    txtfile.write(f'Raymon Anthony Doane: {raymon_percent: .3f}% ({raymon_votes})')
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f'Winner: {key}')
    txtfile.write("\n")
    txtfile.write(f"----------------------------")