import csv
import os

#Create lists to store the contents in each column
months = []
pro_losses = []

 #Define variables and set to 0 outside of the loop
month_count = 0
net_P_L = 0
current_month_P_L = 0
prev_month_P_L = 0
pro_loss_change = 0

#Define path for file to be read
budget_path = os.path.join("PyBank", "Resources", "budget_data.csv")

#Read csv file & skip header
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
          #Increase month counter by 1
          month_count = month_count + 1
          #Find current month profit/losses & add to net total
          current_month_P_L = int(row[1])
          net_P_L = net_P_L + current_month_P_L
          #In the first month set current month equal to previous month
          if (month_count == 1):
               prev_month_P_L = current_month_P_L  
          #In every other month, profit/loss change is equal to current month - previous month
          else:
               pro_loss_change = current_month_P_L - prev_month_P_L
               #Use append function to update months[] & pro_loss_change[]
               months.append(row[0])
               pro_losses.append(pro_loss_change)
               #Reset previous month to equal current month profit/losses
               prev_month_P_L = current_month_P_L

    #Use max/min function to find best & worst months
    greatest_increase = max(pro_losses)
    greatest_decrease = min(pro_losses)

    #Use index function to determine which row those months occur 
    increase_index = pro_losses.index(greatest_increase)
    decrease_index = pro_losses.index(greatest_decrease)

    #Convert index values to dates using months[]
    greatest_profit = months[increase_index]
    greatest_loss = months[decrease_index]

    #Calculate total profit/loss changes 
    total_P_L = sum(pro_losses)

    #Use newly calculated sum to find average profit/loss per month
    average_P_L = round(total_P_L/(month_count - 1), 2)

#Print output to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {month_count}")
print(f"Total:  ${net_P_L}")
print(f"Average Change:  ${average_P_L}")
print(f"Greatest Increase in Profits:  {greatest_profit} (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {greatest_loss} (${greatest_decrease})")

budget_analysis = os.path.join("PyBank", "Output", "budget_data.txt")
with open(budget_analysis, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {month_count}\n")
    outfile.write(f"Total:  ${net_P_L}\n")
    outfile.write(f"Average Change:  ${average_P_L}\n")
    outfile.write(f"Greatest Increase in Profits:  {greatest_profit} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {greatest_loss} (${greatest_decrease})\n")







