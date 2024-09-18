import os
import csv

#setting the path to collect data from the REsource folder
budget_csv = os.path.join( 'Resources', 'budget_data.csv')

#Defined the pyBank function to analyze profit/loss data
def pyBank(profit_loss_data):

   #Initialize variables for counting total months and net profit/loss amount
    total_months = 0
    net_amount = 0 
    prev_profit_loss = 0
    change = 0

    # Creating a dictionary for greatest_increased_profit and greatest_decreased_profit to hold the change and date
    greatest_increased_profit = {'Date': '', 'Change': 0}
    greatest_decreased_profit = {'Date': '', 'Change': 0}

    # List to store monthly changes in profit/loss
    average_change = []

    #Counter for tracking the row position
    i = 0

    #looping through the profit/loss data
    for rows in profit_loss_data:

        #Extract date and profit/loss value from each row
        date = rows[0]
        profit_loss = int(rows[1])

        #Counting the number of months
        total_months = total_months + 1 

        #Adding the profit/loss column
        net_amount = net_amount + profit_loss

        #
        if i > 0:
            #calculate the change from the previous month
            change = profit_loss - prev_profit_loss

            #Store the calculated change in the average_change list
            average_change.append(change)

            #checks if the current change is greater than the previous greatest increase in profit change
            if change > greatest_increased_profit['Change']:

                #Update the greatest increase in profit with the current date and change
                greatest_increased_profit['Date'] = date
                greatest_increased_profit['Change'] = change
                
            #checks if the current change is greater than the previous greatest decrease in profit change
            if  change < greatest_decreased_profit['Change']:

                #Update the greatest decrease in profit with the current date and change
                greatest_decreased_profit['Date'] = date
                greatest_decreased_profit['Change'] = change
                

        #Setting the previous profit_loss value to the current value for the next iteration
        prev_profit_loss = profit_loss

        #Increment the row counter
        i = i + 1

    #Calculating the average change by adding up the change value and dividing it by the number of changes 
    average = sum(average_change) / len(average_change)
            
    # Print the final analysis results
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_amount}')
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {greatest_increased_profit["Date"]} (${greatest_increased_profit["Change"]})')
    print(f'Greatest Decrease in Profits: {greatest_decreased_profit["Date"]} (${greatest_decreased_profit["Change"]})')



# Read in the CSV file
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header row in the CSV file
    header = next(csvreader)
    
    print('Financial Analysis')
    print('--------------------------')

    #Calling the pyBank function to analyze the CSV data
    pyBank(csvreader)