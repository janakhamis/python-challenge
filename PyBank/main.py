#First we'll import the os module which will allow us to create file paths across operating systems
import os

#Importing csv module for reading and processing CSV files
import csv

#Setting the path to collect data from the Resource folder
budget_csv = os.path.join( 'Resources', 'budget_data.csv')

#Specifying the file path for writing the analysis results to a text file 
analysis_file = os.path.join( 'Analysis', 'budget_analysis.txt')

#Defined the pyBank function to analyze profit/loss data
def pyBank(profit_loss_data):

   #Initializing variables for counting total months and net profit/loss amount
    total_months = 0
    net_amount = 0 

    #Initializing prev_profit_loss to 0 to store the previos month for calculating change
    prev_profit_loss = 0

    #Initializing change to 0 to store the change in the profit/loss between months
    change = 0

    #Creating a dictionary for greatest_increased_profit and greatest_decreased_profit to hold the date and profit
    greatest_increased_profit = {'Date': '', 'Profit': 0}
    greatest_decreased_profit = {'Date': '', 'Profit': 0}

    #Created an average_change List to store monthly changes in profit/loss and to be able to calculate the average change 
    average_change = []

    #Counter for tracking the row position
    i = 0

    #Created an empty list to store analysis information for later printing and writing to the file
    analysis_info = []

    #Looping through the profit_loss_data
    for rows in profit_loss_data:

        #Extract the date from the first column of each row
        date = rows[0]
        #Extract the profit/loss from the second column of each row and converted it to interger for calculations 
        profit_loss = int(rows[1])

        #Counting the total number of months
        total_months = total_months + 1 

        #Adding the profit/loss column to get the net amount
        net_amount = net_amount + profit_loss

        #Skipping the first row since there wasn't any previous month to compare
        if i > 0:
            #Calculating the change in profit/loss from the previous month
            change = profit_loss - prev_profit_loss

            #Storing the calculated change in the average_change list
            average_change.append(change)

            #Checking if the current change is greater than the greatest_increased_profit
            if change > greatest_increased_profit['Profit']:

                #Updating the greatest increase in profit with the current date and profit value
                greatest_increased_profit['Date'] = date
                greatest_increased_profit['Profit'] = change
                
            #Checking if the current change is less than the greatest_decreased_profit
            if  change < greatest_decreased_profit['Profit']:

                #Updating the greatest decrease in profit with the current date and profit value
                greatest_decreased_profit['Date'] = date
                greatest_decreased_profit['Profit'] = change
                

        #Setting the previous profit_loss value to the current value for the next iteration
        prev_profit_loss = profit_loss

        #Adding the row counter by 1
        i = i + 1

    #Calculating the average change by adding up the change value and dividing it by the number of changes 
    average = sum(average_change) / len(average_change)

    #Append the results in the analysis_info list
    analysis_info.append('Financial Analysis')
    analysis_info.append('--------------------------')
    analysis_info.append(f'Total Months: {total_months}')
    analysis_info.append(f'Total: ${net_amount}')
    analysis_info.append(f'Average Change: ${average:.2f}') #Researched how to format numbers to 2 decimal places using Python
    analysis_info.append(f'Greatest Increase in Profits: {greatest_increased_profit["Date"]} (${greatest_increased_profit["Profit"]})')
    analysis_info.append(f'Greatest Decrease in Profits: {greatest_decreased_profit["Date"]} (${greatest_decreased_profit["Profit"]})')

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
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row in the CSV file
    header = next(csvreader)

    #Calling the pyBank function and passing the csvreader as an argument 
    pyBank(csvreader)