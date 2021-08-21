# This is the main python file to work with the week 3 homework
import os
import csv
# Part 1: PyBank:
# Your task is to create a Python script that analyses the records to calculate each of the following:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

pybank_csv = os.path.join("Resources", "budget_data.csv")
# Open and read csv file-->budget_data.scv
with open(pybank_csv) as csv_file_pybank:
    csv_reader_pybank = csv.reader(csv_file_pybank, delimiter=",")
    # read and print out the header row
    csv_header_pybank = next(csv_reader_pybank)

    # Define few variables to hold counts/ total amounts/ average changes/maximun and minimum values
    month_count = 0 # initially set the month counter to 0 for further adding up
    total_amount = 0
    change_value = 0
    # hard coding to insert the first value for the profit/loss
    # not sure is there better way to get first row value
    pre_value = 867884
    sum_change_value = 0
    average_change = 0
    max_change = 0
    max_change_date = ""
    min_change = 0
    min_change_date = ""

    # Get the data from each row after the header
    for row1 in csv_reader_pybank:
        # to run through each row in csv file, add one to the month counter
        month_count += 1
        # get the second column's data in excel (profit/loss) and add into total amount
        total_amount += int(row1[1])
        # the change value is the second month's profit/loss - first month's
        change_value = int(row1[1]) - pre_value
        # to reset the previous month's value as this row's value
        pre_value = int(row1[1])
        # sum up all the change values of profit/ loss
        sum_change_value += change_value

        # To compare the change value of profit/ loss with pre-defined value which is 0
        if change_value > max_change:
            # if the new change value is larger than origin one, then replace the value and record the date
            max_change = change_value
            max_change_date = row1[0]

        if change_value < min_change:
            min_change = change_value
            min_change_date = row1[0]
    # To calculate the average change of profit/ loss, the -1 is to minus the first date's
    average_change = round(sum_change_value / (month_count - 1), 2)

    # print the results
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_amount}")
    print(f"Average  Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})")


