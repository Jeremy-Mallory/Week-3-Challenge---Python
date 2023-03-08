import csv
import os
import collections
from collections import Counter

#Create lists for output variables
candidates = []
votes_for_candidate = []

#Define path for csv file to be read
election_path = os.path.join("PyPoll", "Resources", "election_data.csv")

#Read csv file & skip header
with open(election_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        
        #Add contents of candidates column to list
        candidates.append(row[2])
        
    #Use sorted function to sort list of candidates by alphabetical order
    candidates_sorted = sorted(candidates)

    #Use counter function to create dictionary containing name of candidate(key) & votes received (value)
    count_candidate = Counter(candidates_sorted) 

    #Use most_common function to sort candidates by votes received from highest to lowest
    votes_for_candidate.append(count_candidate.most_common())
    
    #Calculate percentage of total votes for all candidates & format output as % to 3 decimal places
    for item in votes_for_candidate:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
      
    #Write output to terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes:  {sum(count_candidate.values())}")
    print("-------------------------")
    print(f"{votes_for_candidate[0][0][0]}: {first}% ({votes_for_candidate[0][0][1]})")
    print(f"{votes_for_candidate[0][1][0]}: {second}% ({votes_for_candidate[0][1][1]})")
    print(f"{votes_for_candidate[0][2][0]}: {third}% ({votes_for_candidate[0][2][1]})")
    print("-------------------------")
    print(f"Winner:  {votes_for_candidate[0][0][0]}")
    print("-------------------------")
    
    #Write output to text file and place in directory PyPoll->output
    election_analysis = os.path.join("PyPoll", "Output", "election_data.txt")
    with open(election_analysis, "w") as outfile:

     outfile.write("Election Results")
     outfile.write("-------------------------")
     outfile.write(f"Total Votes:  {sum(count_candidate.values())}")
     outfile.write("-------------------------")
     outfile.write(f"{votes_for_candidate[0][0][0]}: {first}% ({votes_for_candidate[0][0][1]})")
     outfile.write(f"{votes_for_candidate[0][1][0]}: {second}% ({votes_for_candidate[0][1][1]})")
     outfile.write(f"{votes_for_candidate[0][2][0]}: {third}% ({votes_for_candidate[0][2][1]})")
     outfile.write("-------------------------")
     outfile.write(f"Winner:  {votes_for_candidate[0][0][0]}")
     outfile.write("-------------------------")









    
  






