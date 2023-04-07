import os
import csv
budget_data = os.path.join("Resources" , "budget_data.csv")
months = []
count_months = 0
profit_losses = []
net_total_profit_loss = 0
previous_month_profit_loss = 0
next_month_profit_loss = 0
change_profit_loss = []
output_data = os.path.join("output.txt")
with open(budget_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    for row in csv_reader:
        count_months += 1
        months.append(row[0])
        next_month_profit_loss = int(row[1])
        net_total_profit_loss += next_month_profit_loss
        if (count_months == 1):
            previous_month_profit_loss = next_month_profit_loss
            continue
        else:
            changes_profit_loss = next_month_profit_loss - previous_month_profit_loss
            change_profit_loss.append(changes_profit_loss)
            previous_month_profit_loss = next_month_profit_loss
            sum_profit_loss = sum(change_profit_loss)
            average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)
            greatest_increase = max(change_profit_loss)
            greatest_decrease = min(change_profit_loss)
            month_greatest_increase_index = change_profit_loss.index(greatest_increase)
            month_greatest_decrease_index = change_profit_loss.index(greatest_decrease)
            month_greatest_increase = months[month_greatest_increase_index+1]
            month_greatest_decrease = months[month_greatest_decrease_index+1]

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {count_months}")
print(f"Total:  ${net_total_profit_loss}")
print(f"Average Change:  ${round(sum(change_profit_loss) / (count_months - 1), 2)}")
print(f"Greatest Increase in Profits:  {month_greatest_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits:  {month_greatest_decrease} (${greatest_decrease})")

with open (output_data, "w") as txtfile:
        financial_analysis = (f"Financial Analysis\n"
                f"-----------------\n"
                f"Total Months: {count_months}\n"
                f"---------------------\n"
                f"Total: ${net_total_profit_loss}\n"
                f"Average Change:  ${round(sum(change_profit_loss) / (count_months - 1), 2)}\n"
                f"Greatest Increase in Profits:  {month_greatest_increase} (${greatest_increase})\n"
                f"Greatest Decrease in Profits:  {month_greatest_decrease} (${greatest_decrease})\n"
                        )
        txtfile.write(financial_analysis)
