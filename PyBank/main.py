# Import Libraries
import os
import csv

csvpath = os.path.join("PyBank", "Resources", "BudgetData.csv")
txtpath = os.path.join("PyBank", "Analysis", "Analysis.txt")

difference = 0
avg_calc = []
diff_calc = []
summary_report = {"Total Observations": 0, "Total Profit": 0, "Average Change": 0, "Greatest Increase": 0, "Greatest Decrease": 0}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        print(row)
        summary_report["Total Observations"] = summary_report["Total Observations"] + 1
        summary_report["Total Profit"]  = summary_report["Total Profit"]  + int(row[1])
        avg_calc.append(int(row[1]))
    for i in range(1,len(avg_calc)):
        difference = avg_calc[i]-avg_calc[i-1]
        diff_calc.append(difference)
    summary_report["Greatest Increase"] = max(diff_calc)
    summary_report["Greatest Decrease"] = min(diff_calc)
    summary_report["Average Change"] = sum(diff_calc)/len(diff_calc)
    print(summary_report)

opentxt = open(txtpath, "w")
opentxt.write(str(summary_report))