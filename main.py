# This is the main python file to work with the week 3 homework
import os
import csv

# Part 1: PyBank:

pybank_csv = os.path.join("Resources", "budget_data.csv")
# Open and read csv file-->budget_data.scv
with open(pybank_csv) as csv_file_pybank:
    csv_reader_pybank = csv.reader(csv_file_pybank, delimiter=",")
    # read the header row
    csv_header_pybank = next(csv_reader_pybank)
    # skip the first row for change of profit/loss in later calculation
    pybank_first_date = next(csv_reader_pybank)

    # Define few variables to hold counts/ total amounts/ average changes/maximum and minimum values
    # initially set the month counter to 1 as skip the first row of data
    month_count = 1
    # add the first row's profit/loss into total_amount
    total_amount = int(pybank_first_date[1])
    change_value = 0
    # pre_value = previous value, which is the difference of profit/loss = current month's - previous month's
    pre_value = int(pybank_first_date[1])
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
    print(f"----------------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_amount}")
    print(f"Average  Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_change_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n\n\n")

    # export the pybank analysis results into text file
    output_path = os.path.join("analysis", "analysis_results.txt")
    analysis_result = open(output_path, "w", newline="")
    analysis_result.write(f"Financial Analysis\n")
    analysis_result.write(f"----------------------------------------\n")
    analysis_result.write(f"Total Months: {month_count}\n")
    analysis_result.write(f"Total: ${total_amount}\n")
    analysis_result.write(f"Average  Change: ${average_change}\n")
    analysis_result.write(f"Greatest Increase in Profits: {max_change_date} (${max_change})\n")
    analysis_result.write(f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n\n\n\n\n")


# Part 2: PyPoll:
pypoll_csv = os.path.join("Resources", "election_data.csv")
# Open and read csv file-->election_data.scv
with open(pypoll_csv) as csv_file_pypoll:
    csv_reader_pypoll = csv.reader(csv_file_pypoll, delimiter=",")
    # read the header row
    csv_header_pypoll = next(csv_reader_pypoll)
    # create an empty dictionary to hold candidate and their votes later
    candi_dict = {}
    # initially set the total vote count to 0
    total_vote_count = 0

    for row in csv_reader_pypoll:
        total_vote_count += 1
        # if the candidate's name not exist in the candidate dictionary, add the name in
        if row[2] not in candi_dict:
            candi_dict[row[2]] = 1
        # if the candidate's name already exist, add the vote to the candidate's name by matching the key(row[2])
        else:
            # current_vote = candi_dict[row[2]]
            # candi_dict[row[2]] = current_vote + 1
            candi_dict[row[2]] += 1

    print("Election Results")
    print("----------------------------------------")
    print(f"Total Votes: {total_vote_count}")
    print("----------------------------------------")
    # using a for loop here to repeat the calculation of vote percentage for each candidate,
    # candidate's vote is found by matching their name(key) in dictionary
    for candidate in candi_dict:
        print("{}: {:.3f}% ({})".format(str(candidate), float(candi_dict[candidate]/total_vote_count*100), candi_dict[candidate]))
    print("----------------------------------------")
    # using the build-in max function to find the maximum vote's candidate
    # using build-in get function to grab the name of the winner candidate
    print(f"Winner: {max(candi_dict, key=candi_dict.get)}")
    print("----------------------------------------")

    # export the pypoll analysis results into text file
    analysis_result.write(f"Election Results\n")
    analysis_result.write(f"----------------------------------------\n")
    analysis_result.write(f"Total Votes: {total_vote_count}\n")
    analysis_result.write(f"----------------------------------------\n")
    for candidate in candi_dict:
        analysis_result.write("{}: {:.3f}% ({})\n".format(str(candidate), float(candi_dict[candidate] / total_vote_count * 100), candi_dict[candidate]))
    analysis_result.write(f"----------------------------------------\n")
    analysis_result.write(f"Winner: {max(candi_dict, key=candi_dict.get)}\n")
    analysis_result.write(f"----------------------------------------\n")

