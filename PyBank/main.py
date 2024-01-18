import os
import csv

# Module for reading CSV files
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# variables
Total_months = 0
Net_total = 0
Changes_profit_loss = 0
Average_changes_PL = 0
Changes = []
Months = []
# Open file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
# Loop through the rows in the CSV file
    for row in csvreader:
        # Count total months
        Total_months += 1

        # Calculate net total
        Net_total += int(row[1])

        # Calculate change in profit or loss
        if Total_months > 1:
           Changes_profit_loss = int(row[1]) - Average_changes_PL
           Changes.append(Changes_profit_loss)
           Months.append(row[0])

        # Set the current profit or loss as the previous for the next iteration
        Average_changes_PL = int(row[1])

# Calculate average change
average_change = round(sum(Changes) / len(Changes), 2)

# Find the greatest increase and decrease in profits
greatest_increase_profit = max(Changes)
greatest_increase_month = Months[Changes.index(greatest_increase_profit)]
greatest_decrease_profit = min(Changes)
greatest_decrease_month = Months[Changes.index(greatest_decrease_profit)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${Net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})")


# Results to a text file
output_path = os.path.join("Analysis","Analysis.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {Total_months}\n")
    output_file.write(f"Total: ${Net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_profit})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_profit})\n")    