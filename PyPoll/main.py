# First we'll import the os module which will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#setting the path to collect data from the REsource folder
election_csv = os.path.join( 'Resources', 'election_data.csv')

#Specifying the file to write to  
analysis_file = os.path.join( 'Analysis', 'election_analysis.txt')

def pypoll(election_data):

    total_votes = 0
    candidates_list = {}
    winner_vote = 0
    winner_candidate = {'Candicate': ''}

    analysis_info = []

    for rows in election_data:

        candidate = rows[2]

        total_votes = total_votes + 1

        if candidate in candidates_list:
            candidates_list[candidate] = candidates_list[candidate] + 1
        else:
            candidates_list[candidate] = 1

        if candidates_list[candidate] > winner_vote:
            winner_vote = candidates_list[candidate]
            winner_candidate['Candicate'] = candidate


    analysis_info.append('Election Results')
    analysis_info.append('-------------------------')

    analysis_info.append(f'Total Votes: {total_votes}')
    analysis_info.append('-------------------------')

    for candidate, votes in candidates_list.items():

        percentage_change = (votes/total_votes)*100

        analysis_info.append(f'{candidate}: {percentage_change:.3f}% ({votes})')

    analysis_info.append('-------------------------')    
    analysis_info.append(f'Winner: {winner_candidate["Candicate"]}')
    analysis_info.append('-------------------------') 

    for rows in analysis_info:
        print(rows)


    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(analysis_file, 'w') as txt_file:

        for rows in analysis_info:
            # Write the second row
            txt_file.write(rows + '\n')




# Read in the CSV file
with open(election_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row in the CSV file
    header = next(csvreader)
    
    pypoll(csvreader)