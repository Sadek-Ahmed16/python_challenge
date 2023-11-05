# Creating and reading CSV file
import os
import csv

# Declaring the location of the CSV file
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

# Creating list to store the row data/values
date = []
profit_loss = []
profit_change = []


with open(budget_data_csv, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Defining the header row so we can skip the header when iterating through the data
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # linking the rows to their corresponding lists
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(int(row[1]))
        
# Calculating the total count of the months
total_months = len(date)
#print(total_months)

# Calculating the net total profit for all months
total_profit = sum(profit_loss)
#print(total_profit)

# Calculating the change in profit for each month by iterating through the months, finding the difference from the month before
# First month will have no difference hence i>0
# linking the profit change of each month to a new list
for i in range(len(profit_loss)):
    if i > 0:
        previous_change = profit_loss[i-1]
        profit_change.append(profit_loss[i]-previous_change)
        #print(profit_change)
    
# Calculating the Average profit change for all months
total_profit_change = sum(profit_change)
average_profit_change = total_profit_change/(len(profit_change))
#print(average_profit_change)

# Getting the max value for change in profit and the month it is associated with
max_profit = max(profit_change)
max_profit_month = profit_change.index(max_profit) + 1
#print(f"{date[max_profit_month]} ${max_profit}")

# Getting the max value for change in profit and the month it is associated with
min_profit = min(profit_change)
min_profit_month = profit_change.index(min_profit) + 1
#print(f"{date[min_profit_month]} ${min_profit}")

# *We are using + 1 as we are not taking the change of the first month into consideration when creating a list for profit change


# Printing out the results
print(" ")
print("Financial Analysis")
print(" ")
print("----------------------------")
print(" ")
print(f"Total months: {total_months}")
print(" ")
print(f"Total: ${total_profit}")
print(" ")
print(f"Average Change: ${round(average_profit_change, 2)}")
print(" ")
print(f"Greatest Increase in Profits: {date[max_profit_month]} (${max_profit}) ")
print(" ")
print(f"Greatest Decrease in Profits: {date[min_profit_month]} (${min_profit})")


# Decaring a location to export and store results as a text file
budget_data_csv = os.path.join("..", "analysis", "PyBank_analysis.txt")
with open(budget_data_csv, "w") as text_file:

    text_file.write("\n")
    text_file.write("Financial Analysis")
    text_file.write("\n\n")
    text_file.write("----------------------------")
    text_file.write("\n\n")
    text_file.write(f"Total months: {total_months}")
    text_file.write("\n\n")
    text_file.write(f"Total: ${total_profit}")
    text_file.write("\n\n")
    text_file.write(f"Average Change: ${round(average_profit_change, 2)}")
    text_file.write("\n\n")
    text_file.write(f"Greatest Increase in Profits: {date[max_profit_month]} (${max_profit}) ")
    text_file.write("\n\n")
    text_file.write(f"Greatest Decrease in Profits: {date[min_profit_month]} (${min_profit})")
