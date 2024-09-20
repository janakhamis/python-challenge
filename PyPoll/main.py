#First we'll import the os module which will allow us to create file paths across operating systems
import os

#Importing csv module for reading and processing CSV files
import csv

#Setting the path to collect data from the Resource folder
election_csv = os.path.join( 'Resources', 'election_data.csv')

#Specifying the file path for writing the analysis results to a text file 
analysis_file = os.path.join( 'Analysis', 'election_analysis.txt')

#Defining the function poypoll that takes election_data as input 
def pypoll(election_data):

    #Initializing total_votes to 0 to keep track of the total number of votes
    total_votes = 0

    #Creating an empty dictionary to store each candidates's name as the key and their vote count as the Value 
    candidates_list = {}

    #Initializing winner_vote to 0 to store the maximum vote between the candidates
    winner_vote = 0

    #Initializing winner_candidate to an empty string to store the name of the candidate with the most votes
    winner_candidate = ""

    #created an empty list to store analysis information for later printing and writing to the file
    analysis_info = []

    #loop through each row in the election_data to process votes
    for rows in election_data:

        #Extract the candidate name from the third column of each row
        candidate = rows[2]

        #Adding the total_votes by 1 to be able to get the total number of votes 
        total_votes = total_votes + 1

        #Checking if the candidate is already found in the candidates_list then we add their votes by 1
        if candidate in candidates_list:
            #Adding the candidtaes votes by 1 
            candidates_list[candidate] = candidates_list[candidate] + 1
        #If the statement above is not correct then the candidate is added and set the vote to 1 
        else:
            candidates_list[candidate] = 1

        #Checking if the current candidate has more votes than the winner_vote
        if candidates_list[candidate] > winner_vote:
            #Updating the winner_vote to the highest candidate's vote
            winner_vote = candidates_list[candidate]
            #Updating winner_candidate with the candidate name that has the maximum vote
            winner_candidate = candidate

    #Append the analysis information to the list for later output
    analysis_info.append('Election Results')
    analysis_info.append('-------------------------')
    #Append the total number of votes to the analysis_info list
    analysis_info.append(f'Total Votes: {total_votes}')
    analysis_info.append('-------------------------')

    #Looping through the candidate_list to calculate their percentage_change
    for candidate, votes in candidates_list.items():
        #calculating the percentage change of votes for each candidate 
        percentage_change = (votes/total_votes)*100

        #Append the candidate's name, percentage_change, and total votes to the analysis_info list
        #Researched how to format numbers to 3 decimal places using Python
        analysis_info.append(f'{candidate}: {percentage_change:.3f}% ({votes})')

    # Append the lines for the winner and closing separator
    analysis_info.append('-------------------------')    
    analysis_info.append(f'Winner: {winner_candidate}')
    analysis_info.append('-------------------------') 

    #Looping through the analysis_info list and print each line to the terminal 
    for rows in analysis_info:
        #printing the analysis_info list
        print(rows)

    #Open the file using "write" mode, which will write in the text file.
    with open(analysis_file, 'w') as txt_file:
        #Loop through each line in the analysis_info list and write it to the text file
        for rows in analysis_info:
            #Write each row on a newline 
            #I searched how to write each row on a line and found that I need to add '+ '\n''
            txt_file.write(rows + '\n')


# Read in the CSV file
with open(election_csv) as csvfile:

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row in the CSV file
    header = next(csvreader)
    
    #Calling the pypoll function and passing the csvreader as an argument 
    pypoll(csvreader)