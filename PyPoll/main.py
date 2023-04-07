import os 
import csv 
election_data = os.path.join("Resources" , "election_data.csv")
output_data = os.path.join("output.txt")
candidate_votes = {}
number_votes = []
count_votes = 0
candidate = ""
unique_candidates = []
percent_votes = []
winning_count = 0
winning_candidate = ""
with open (election_data, newline = "") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter= ",")
        csv_header = next(csvfile)
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote
        for row in csv_reader:
                count_votes += 1
                candidate = row[2]
                if candidate not in unique_candidates:
                        unique_candidates.append(candidate)
                        candidate_votes[candidate] = 0
                candidate_votes[candidate] += 1
   
        

print("Election Results")
print("---------------------")
print(f"Total Votes: {count_votes}")
print("---------------------")
for candidate in unique_candidates:
        percent_votes = (candidate_votes[candidate] / count_votes) * 100
        print(f"{candidate}: {round(percent_votes, 3)}% ({candidate_votes[candidate]})")
        if percent_votes > winning_count:
                winning_count = percent_votes
                winning_candidate = candidate    
print("---------------------")

print(f"Winner: {winning_candidate}")
print("---------------------")



with open (output_data, "w") as txtfile:
        txtfile.write("Election Results\n")
        txtfile.write("---------------------\n")
        txtfile.write(f"Total Votes: {count_votes}\n")
        txtfile.write("---------------------\n")
        for candidate in unique_candidates:
                percent_votes = (candidate_votes[candidate] / count_votes) * 100
                txtfile.write(f"{candidate}: {round(percent_votes, 3)}% ({candidate_votes[candidate]})\n")
    
        txtfile.write("---------------------\n")
        txtfile.write(f"Winner: {winning_candidate}\n")
        txtfile.write("---------------------\n")
