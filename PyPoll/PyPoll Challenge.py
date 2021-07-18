#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PyPoll Challenge

#incorporated the dependencies
import csv
import os

election_data = os.path.join("election_data.csv.crdownload")
election_analysis = os.path.join("election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = { }
winning_candidate = ""
winning_count = 0

with open(election_data) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    print(header)
    
    for row in reader:
        #print(". ", end="")
        
        total_votes = total_votes + 1
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    
with open(election_analysis, "w") as txt_file:
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: str(total_votes) + \n"
        f"----------------------\n"
    )
    
    print(election_results, end="")

    txt_file.write(election_analysis)
    
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.2f}% ({votes})\n"
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)
    
    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"------------------------\n"
    )
    
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)



# In[ ]:




