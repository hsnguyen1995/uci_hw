import os
import csv
import sys

budget_data_csv = os.path.join("Resources", "budget_data.csv")


dates = []
monthlyRev = []
profitChange = []

with open(budget_data_csv, newline="") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")
    next(csvReader)

    summaryHeader = "Financial Analysis \n----------------------------"
    totalMonths = 0
    totalAmount = 0
    for row in csvReader:
#   * The total number of months included in the dataset
        totalMonths += 1
    
#   * The net total amount of "Profit/Losses" over the entire period
        totalAmount += int(row[1])

#   * The average of the changes in "Profit/Losses" over the entire period
        dates.append(row[0])
        monthlyRev.append(int(row[1]))

    for i in range(1,len(monthlyRev)):
        profitChange.append(monthlyRev[i] - monthlyRev[i-1])
        avgOfChanges = sum(profitChange) / len(profitChange)

#   * The greatest increase in profits (date and amount) over the entire period
        maxProfit = max(profitChange)
        dateMaxProfit = dates[profitChange.index(maxProfit) + 1] 

#   * The greatest decrease in losses (date and amount) over the entire period
        maxLoss = min(profitChange)
        dateMaxLoss = dates[profitChange.index(maxLoss) + 1]

# * As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)


print(f'{summaryHeader} \nTotal Months: {totalMonths}')
print(f'Total: ${totalAmount}')
print(f'Average  Change: ${round(float(avgOfChanges),2)}')
print(f'Greatest Increase in Profits: {dateMaxProfit} (${maxProfit})')
print(f'Greatest Decrease in Profits: {dateMaxLoss} (${maxLoss})')

sys.stdout = open("main.txt", 'w')  

print(f'{summaryHeader} \nTotal Months: {totalMonths}')
print(f'Total: ${totalAmount}')
print(f'Average  Change: ${round(float(avgOfChanges),2)}')
print(f'Greatest Increase in Profits: {dateMaxProfit} (${maxProfit})')
print(f'Greatest Decrease in Profits: {dateMaxLoss} (${maxLoss})')