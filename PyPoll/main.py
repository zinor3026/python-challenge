import os
import csv

# defining variables
total_votes = 0
candidates_list = []
percent_vote1 = 0
percent_vote2 = 0
percent_vote2 = 0
vote_count1 = 0
vote_count2 = 0
vote_count3 = 0 


#defining path to csv file in resources
path = os.path.join('python-challenge','PyPoll','Resources','election_data.csv')
    
# Reading the csv file 
with open(path) as election:
    election_reader = csv.reader(election, delimiter = ',')
    
    #read the header row first
    header= next(election_reader)
    
    for row in election_reader:

        #Calculate total votes
        total_votes += 1
        # Calculate percentage of vote and vote count for each canditate
        #candidates = row[2]
        #candidates_list.append(candidates)
        
        if row[2] == "Charles Casper Stockham":
            vote_count1 += 1
            
        elif row[2] == "Diana DeGette":
            vote_count2 += 1
            
        elif row[2] == "Raymon Anthony Doane":
            vote_count3 += 1
    percent_vote1 = round((vote_count1/ (vote_count1+ vote_count2+ vote_count3)) * 100, 3)
    percent_vote2 = round((vote_count2/ (vote_count1+ vote_count2+ vote_count3)) * 100,3)
    percent_vote3 = round((vote_count3/ (vote_count1+ vote_count2+ vote_count3)) * 100, 3)

# for candidates in candidates_list :
    
        
    
    
    
print(f"Total Votes : {total_votes}")
print(f"{vote_count1}, {vote_count2}, {vote_count3}")
print(f"{percent_vote1}, {percent_vote2}, {percent_vote3}")
print(f"")
print(f"Winner :")

output_path = os.path.join('python-challenge','PyPoll','analysis','election.txt') 

with open(output_path,'w') as result:
    result.write(f"Total Votes : {total_votes}\n")
    result.write(f"\n")
    result.write(f"\n")
    result.write(f"\n")
    result.write(f"\n")