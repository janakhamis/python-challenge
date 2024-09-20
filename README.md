# Python Challenge: PyBank and PyPoll
This repository contains python scripts for two challenges (PyBank and PyPoll). Both challenges involve analyzing data using python and printing the results on the terminal and to the text file (Module 3 Challenge).

# PyBank
The PyBank challenge focuses on analyzing financial information and providing a summary of important financial metrics. The script reads from the budget_data.csv file, which contains two columns ("Date and "Profit/Losses"). 

# Objective:
The python script calculates the folowing:
  - Total Number of Months: the total number of months found in the dataset.
  - Net Total Amount: is the cumulative amount of the "Profit/Losses" column over the period.
  - Average Change: the average monthly change in the profit/loss.
  - Greatest Increase in Profits: the date and amount of the largest increase in profits.
  - Greatest Decrease in Profits: the date and amount of the largest decrease in profits.

# Files:
  - main.py: The python script that performs the analysis and outputs the results.
  - Resources/budget_data.csv: The datasset containing the financial records.
  - Analysis/budget_analysis.txt: The text file where the results are stored.

# Output:
The result of the PyBank script shows the "Total Months", "Total Amount", "Average Change", "Greatest Increase in Profits", and "Greatest Decrease in Profits". The result is printed to the terminal and stored as a text file in the Analysis folder.

# PyPoll

The PyPoll challenge focuses on analyzing election data and providing a summary of the vote counting process. The script reads from the election_data.csv file, which contains three columns ("Voter ID", "County", and "Candidate").

# Objective:
The python script calculates the folowing:
  - Total Votes: The total number of votes found in the dataset.
  - Candidates: A list of candidates that recieved votes.
  - Percentage of Votes per Candidate: The percentage of votes each candidate won.
  - Total Votes per Candidate: The total number of votes each candidate receieved.
  - Election Winner: The candidate with the highest number of votes.

# Files:
  - main.py: The python script that performs the analysis and outputs the results.
  - Resources/election_data.csv: The datasset containing the financial records.
  - Analysis/election_analysis.txt: The text file where the results are stored.

# Output:
The result of the PyPoll script shows the "Total Votes", "Candidates's Names", each candidates percentage and vote count, and the winner of the election. The result is printed to the terminal and stored as a text file in the Analysis folder.

#How to Run
  1. Clone the repository:
       1. Open your terminal (Git Bash, Command Prompt, or any Git client).
       2. Use the cd command to navigate to the directory where you want to clone the repository.
       3. Run the following command to clone the repository: git clone link_provided
  2. Ensure Python is installed on your machine.
  3. Open the cloned file in the Visual Studio Code:
       1. Go to file > Open Folder and navigate to the folder where you cloned the repository.
       2. Select the folder to open in VS code.
  4. Run the python scripts:
       1. Open the terminal in VS code by selecting from the top menu terminal > new terminal.
       2. Navigate to the correct folder for the scriot you want to run:
            1. For PyBank, run:
                 1. cd PyBank
                 2. python main.py
            2. For PyPoll, run:
                 1. cd PyPoll
                 2. python main.py
  5. View the output:
       - Once the script is executed the result will be printed in the terminal
       - The results are saved  


