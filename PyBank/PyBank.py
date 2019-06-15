
import os
import csv

Bank_Data = os.path.join('PyBank.csv')

 # declare an empty list
date = 0
TotalProfit = 0
TotalLoss = 0
MaxProfit = 0
MinProfit = 0
Average_change = 0
MinProfitDate = ""
MaxProfitDate = ""

with open(Bank_Data, newline="") as csvfile:
 csvreader= csv.reader(csvfile, delimiter = ",")

 csvheader = next(csvreader)
 print(csvreader)

 print(date)
 print(TotalProfit)

 for row in csvreader:

  date+= 1
 Profit = int(row[1])
 if Profit >0 :
   TotalProfit += Profit
 else:
  TotalLoss += Profit

 # fix the second row second column as previous value
 # create a variable to calculate the changes over the period
 # current value minus previous value
 # append the change value to empty list (change)
 # reset the previous value

 if(date==1):
   MaxProfitDate= row[0]
   MaxProfit= Profit
   MinProfitDate = row[0]
   MinProfit = Profit
 elif Profit> MaxProfit:
  MaxProfitDate = row[0]
  MaxProfit = Profit
 elif Profit< MinProfit:
   MinProfitDate=row[0]
   MinProfit = Profit


# Print
output= ["", "", "", "", "", "", ""]
output[0]="Financial Analysis"
output[1]= "---------------------"
output[2]= "Total Months:"+ str(date)
output[3]= "Total:"+ str(TotalProfit+TotalLoss)

# calculate the average of the change list
output[4]= "Average Change:" + str (round((TotalProfit+TotalLoss)/date,2))

# min and max according to respective month
output[5]= "Greatest Increase in Profits:" + MaxProfitDate + str(MaxProfit)
output[6]= "Greatest Decrease in Profits:" + MinProfitDate + str(MinProfit)

for out in output:
  print (out)

outputFile =("PyBank.txt","w")
for out in output:
 outputFile.write(out+ "\n")