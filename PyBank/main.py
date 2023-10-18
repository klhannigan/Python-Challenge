import os
import csv

budget_data_csv = os.path.join(r"C:\Users\Kylez\Desktop\Python-Challenge\PyBank\Resources\budget_data.csv")

total_months = []
total_profit = []
profit_changes = []

with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)

    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit) - 1):
        profit_changes.append(total_profit[i + 1] - total_profit[i])

max_increase_value = max(profit_changes)
max_decrease_value = min(profit_changes)

max_increase_month = profit_changes.index(max(profit_changes)) + 1
max_decrease_month = profit_changes.index(min(profit_changes)) + 1

print(f'Total Months:{len(total_months)}')
print(f'Total: ${sum(total_profit)}')
print(f'Average Change: {len(profit_changes)}')
print(f"Average Change: {round(sum(profit_changes)/len(profit_changes), 2)}")
print(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})')
print(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})')

export_file = os.path.join(r"C:\Users\Kylez\Desktop\Python-Challenge\PyBank\Analysis\Financial_Analysis.txt")
with open(export_file, "w") as txtfile:
    
    txtfile.write("Financial Analysis")
    txtfile.write("\n")
    txtfile.write("----------------------------")
    txtfile.write("\n")
    txtfile.write(f'Total Months: {len(total_months)}')
    txtfile.write("\n")
    txtfile.write(f'Total: ${sum(total_profit)}')
    txtfile.write("\n")
    txtfile.write(f'Average Change: {len(profit_changes)}')
    txtfile.write("\n")
    txtfile.write(f'Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})')
    txtfile.write("\n")
    txtfile.write(f'Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})')