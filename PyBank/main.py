
import csv

csvpath ="Resources/budget_data.csv"

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    print(csv_header)


    row_total = 0 # count of rows
    run_total = 0 # running total of profit
    change_total = 0 #running sum of changes in profit

    #store info about month to month changes
    m2m_change = []
    prev_month = 0

    #initialize the tracker for max and min
    max_inc_date = ""
    max_inc = 0
    max_dec_date = ""
    max_dec = 0
    
    change= 0

    for row in csvreader:
        change= int(row[1])-prev_month
        m2m_change.append(change)
        prev_month = int(row[1])
        row_total = row_total + 1
        run_total = run_total + int(row[1])

        if change > max_inc:
            max_inc_date = row[0]
            max_inc = change

        if change < max_dec:
            max_dec_date = row[0]
            max_dec = change

        # store an adjustment term for the first change recorded
        if len(m2m_change) == 1:
            change_adj = int(m2m_change[0])

        #sum of changes
        change_total=change_total+change


    av_change = (change_total - change_adj)/len(m2m_change)



    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {row_total}")
    print(f"Total: ${run_total}")
    print(f"Average Change: ${av_change}")
    print(f"Greatest Increase in Profits: {max_inc_date} ({max_inc})")
    print(f"Greatest Decrease in Profits: {max_dec_date} $({max_dec})")


# Code to write to a txt file generated with assistance from Xpert AI   
# Open the file in write mode
file_path = "analysis/pybank_results.txt"
with open(file_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {row_total}\n")
    file.write(f"Total: ${run_total}\n")
    file.write(f"Average Change: ${av_change}\n")
    file.write(f"Greatest Increase in Profits: {max_inc_date} ({max_inc})\n")
    file.write(f"Greatest Decrease in Profits: {max_dec_date} $({max_dec})\n")

print("Results have been written to 'analysis/pybank_results.txt'")