import os
import csv

#setting the path to collect data from the REsource folder
budget_csv = os.path.join( 'Resources', 'budget_data.csv')

#Defining the function and it accepts profit_loss as its sole parameter
def pyBank(profit_loss_data):

   
    total_months = 0
    net_amount = 0 
    prev_profit_loss = 0
    change = 0

    # Creating a dictionary for greatest_increased_profit and greatest_decreased_profit to hold the change and date
    greatest_increased_profit = {'Date': '', 'Change': 0}
    greatest_decreased_profit = {'Date': '', 'Change': 0}

    average_change = []
    i = 0

    #looping through the 
    for rows in profit_loss_data:

        date = rows[0]
        
        profit_loss = int(rows[1])

        #Counting the number of months
        total_months = total_months + 1 

        #Adding the profit/loss column
        net_amount = net_amount + profit_loss

        if i > 0:
            change = profit_loss - prev_profit_loss
            average_change.append(change)

            #finding the greatest increase in profit change
            if change > greatest_increased_profit['Change']:

                greatest_increased_profit['Date'] = date
                greatest_increased_profit['Change'] = change
                
            #finding the greatest decrease in profit change
            if  change < greatest_decreased_profit['Change']:

                greatest_decreased_profit['Date'] = date
                greatest_decreased_profit['Change'] = change
                

        prev_profit_loss = profit_loss

        i = i + 1

    average = sum(average_change) / len(average_change)
            

    print(f'Total Months: {total_months}')
    print(f'Total: ${net_amount}')
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {greatest_increased_profit["Date"]} (${greatest_increased_profit["Change"]})')
    print(f'Greatest Decrease in Profits: {greatest_decreased_profit["Date"]} (${greatest_decreased_profit["Change"]})')



# Read in the CSV file
with open(budget_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    print('Financial Analysis')
    print('--------------------------')
    pyBank(csvreader)