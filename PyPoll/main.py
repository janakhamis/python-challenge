import os
import csv

#setting the path to collect data from the REsource folder
election_csv = os.path.join( 'Resources', 'election_data.csv')

def pypoll(election_data):

    total_votes = 0
    candidates_list = {}
    winner_vote = 0
    winner_candidate = {'Candicate': ''}

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


    print('Election Results')
    print('-------------------------')

    print(f'Total Votes: {total_votes}')
    print('-------------------------')

    for candidate, votes in candidates_list.items():

        percentage_change = (votes/total_votes)*100

        print(f'{candidate}: {percentage_change:.3f}% ({votes})')

    print('-------------------------')    
    print(f'Winner: {winner_candidate["Candicate"]}')
    print('-------------------------') 



# Read in the CSV file
with open(election_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    pypoll(csvreader)