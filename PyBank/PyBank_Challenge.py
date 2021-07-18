#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv
import os

budget_data = os.path.join("budget_data.csv")
budget_analysis = os.path.join("budget_analysis.txt")

#calculations
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999999]
total_net = 0

with open(budget_data) as financial_data:
    reader = csv.reader(financial_data)
    
    header = next(reader)
    #print(header)
    
    first_row = next(reader)
    #print (first_row)
    
    #The total number of months included in the dataset
    total_months = total_months + 1
                   
    #The net total amount of “Profit/Losses” over the entire period
    total_net = total_net = int(first_row[1])
    prev_net = int(first_row[1])
    #print(prev_net)
    
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])
        #print(total_months)
        #print(total_net)
        
    
    #Calculate the changes in “Profit/Losses” over the entire period, then find the average of those changes
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1]) 
        net_change_list = net_change_list + [net_change]
        #print(net_change_list)
    
    #The greatest increase in profits (date and amount) over the entire period
    
        month_of_change = month_of_change + [row[0]]
        #print(month_of_change)
    
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
#         print("Greatest Increase")
#         print(greatest_increase)

        #The greatest decrease in losses (date and amount) over the entire period
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

    #Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    
    output = (
        f"\nFinancial Analysis\n"
        f"======================\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net}\n"
        f"Average Change: ${net_monthly_avg:.2f}\n"
        f"Greatest Increase In Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
        f"Greatest Decrease In Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n")
    
    print(output)

with open(budget_analysis, "w") as txt_file:
    txt_file.write(output)
            
   


# In[ ]:




