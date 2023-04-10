# Import 
import os, csv
from pathlib import Path
# file location
input_file = Path("python-challenge", "PyBank", "Resources" "budget_data.csv")
# Create empty lists to iterate through specific rows for the following variables
months = []
profit = []
monthly_profit_change = []
csvpath = "./Resources/budget_data.csv"
# Open csv 
with open(csvpath, "r") as csvfile:
     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(csvfile,delimiter=",")
    # Skip header labels
    header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        monthly_profit_change.append(profit[i+1]-profit[i])
# Obtain the max and min of the the montly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)
# Correlate max and min to month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1
#Print Statements
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")
# Output files
output_file = "./Analysis/budget_analysis.csv"
with open(output_file,"w") as file:
# Write methods to print to Financial_Analysis_Summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")