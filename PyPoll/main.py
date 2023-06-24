import os
import csv

# defining variables
total_votes = 0
candidates_list = []
candidate_dict = {}
winner_name = ""
winner_count = 0
   


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
        # Collect candidates name and count their votes
        candidate = row[2]
        
        
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidate_dict[candidate] = 0
            
        candidate_dict[candidate] = candidate_dict[candidate] + 1
        
#Write to txt and print the total votes

output_path = os.path.join('python-challenge','PyPoll','analysis','election.txt')

with open(output_path,'w') as result:
    
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

    print(election_results, end="") 
    
    result.write(election_results)
 
 #Extract candidate from the dictonary created and calculate the percentages
    
    for candidate in candidates_list:
        votes = candidate_dict[candidate]
        percentage = votes/total_votes *100
        
        #Using if funtion to find the winner/candidate with most votes
        if votes > winner_count:
            winner_count = votes
            winner_name = candidate

        #printing the candidates name with percent and vote count
        
        voter_output = f"{candidate}: {percentage:.3f}% ({votes:,})\n"
        print(voter_output)
        
        result.write(voter_output)
    
    #Printing the winner    
    winning_summary = (
        f"-------------------------\n"
        f"Winner: {winner_name}\n"
        f"-------------------------\n")
    
    print(winning_summary)
    
    result.write(winning_summary)